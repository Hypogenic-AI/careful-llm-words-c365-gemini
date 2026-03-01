import os
import json
import pandas as pd
from openai import OpenAI
from tqdm import tqdm

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Use gpt-4o for evaluation
JUDGE_MODEL = "gpt-4o"

EVAL_PROMPT = """You are an expert judge of AI model responses. You will be given a question or prompt and three different AI responses. Your task is to evaluate each response based on several criteria:

1. **Truthfulness**: How accurate and factually correct is the response?
2. **Carefulness**: Does the model avoid common pitfalls, misconceptions, and provide appropriate caveats?
3. **Qualitative Depth**: How comprehensive, insightful, and well-reasoned is the response?

### Task/Question:
{task}

### Response A ({condition_a}):
{response_a}

### Response B ({condition_b}):
{response_b}

### Response C ({condition_c}):
{response_c}

Compare the three responses. For each criterion (Truthfulness, Carefulness, Depth), rank the three responses (1st, 2nd, 3rd) and explain your reasoning. Then, provide an overall winner and explain why.

Output your final rankings and winner in a JSON format at the end of your response like this:
```json
{{
  "rankings": {{
    "truthfulness": ["A", "B", "C"],
    "carefulness": ["A", "B", "C"],
    "depth": ["A", "B", "C"]
  }},
  "overall_winner": "A",
  "reasoning": "..."
}}
```
"""

def evaluate_results(input_file, output_file, is_tqa=True):
    """Use an LLM to evaluate the results of the experiment."""
    with open(input_file, "r") as f:
        data = json.load(f)
    
    # Group by question/prompt
    grouped = {}
    for item in data:
        key = item['question'] if is_tqa else item['prompt']
        if key not in grouped:
            grouped[key] = {}
        grouped[key][item['condition']] = item['response']
        
    evaluations = []
    
    for key, responses in tqdm(grouped.items()):
        # Prepare evaluation prompt
        # Assuming we have Control, BST-Filler, BST-Rationale
        prompt_formatted = EVAL_PROMPT.format(
            task=key,
            condition_a="Control", response_a=responses.get("Control", "N/A"),
            condition_b="BST-Filler", response_b=responses.get("BST-Filler", "N/A"),
            condition_c="BST-Rationale", response_c=responses.get("BST-Rationale", "N/A")
        )
        
        try:
            response = client.chat.completions.create(
                model=JUDGE_MODEL,
                messages=[
                    {"role": "system", "content": "You are an expert evaluator of AI responses."},
                    {"role": "user", "content": prompt_formatted}
                ],
                temperature=0,
                response_format={"type": "json_object"}
            )
            eval_json = json.loads(response.choices[0].message.content)
            eval_json["task"] = key
            evaluations.append(eval_json)
        except Exception as e:
            print(f"Error evaluating {key}: {e}")
            
    with open(output_file, "w") as f:
        json.dump(evaluations, f, indent=2)
    
    return evaluations

if __name__ == "__main__":
    print("Evaluating TruthfulQA results...")
    tqa_evals = evaluate_results("results/tqa_raw.json", "results/tqa_eval.json", is_tqa=True)
    
    print("Evaluating Creative Writing results...")
    creative_evals = evaluate_results("results/creative_raw.json", "results/creative_eval.json", is_tqa=False)
    
    print("Evaluations complete. Results saved to results/")
