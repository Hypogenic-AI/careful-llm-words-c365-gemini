import os
import json
import time
import pandas as pd
from openai import OpenAI
from datasets import load_dataset
from tqdm import tqdm

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Use gpt-4o as it's the standard for research in 2025
MODEL_NAME = "gpt-4o"

def get_response(prompt, system_message="You are a helpful assistant."):
    """Wrapper for OpenAI API calls."""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling API: {e}")
        return None

# BST Prompts
BST_FILLER_SYSTEM = (
    "You are a helpful assistant. After every sentence you write, you MUST write exactly 10 '.' (dots) "
    "on a new line. These dots represent your internal thinking process before you continue to the next sentence."
)

BST_RATIONALE_SYSTEM = (
    "You are a helpful assistant. After every sentence you write, you MUST write an internal rationale "
    "for what you should say next, preceded by '<thought>' and followed by '</thought>' on a new line. "
    "Then continue with your next sentence on a new line."
)

CONTROL_SYSTEM = "You are a helpful assistant."

def run_truthful_qa(subset_size=20):
    """Run a subset of TruthfulQA under different BST conditions."""
    print(f"Running TruthfulQA (subset size: {subset_size})...")
    # Using the local truthful_qa dataset if possible, otherwise loading from HF
    # The resources catalog mentioned datasets/truthful_qa/
    try:
        dataset = load_dataset("arrow", data_files="datasets/truthful_qa/data-00000-of-00001.arrow", split="train")
    except:
        dataset = load_dataset("truthful_qa", "generation", split="validation")
    
    subset = dataset.shuffle(seed=42).select(range(subset_size))
    
    results = []
    
    for item in tqdm(subset):
        question = item['question']
        best_answer = item['best_answer']
        
        # Conditions
        conditions = [
            ("Control", CONTROL_SYSTEM),
            ("BST-Filler", BST_FILLER_SYSTEM),
            ("BST-Rationale", BST_RATIONALE_SYSTEM)
        ]
        
        for name, system in conditions:
            response = get_response(question, system)
            results.append({
                "question": question,
                "best_answer": best_answer,
                "condition": name,
                "response": response
            })
            
    return results

def run_creative_writing():
    """Run creative writing prompts."""
    prompts = [
        "Write a short story about a detective who finds a clue in a library. The clue is a bookmark from a long-lost book.",
        "Explain the concept of quantum entanglement to a 10-year-old using a sports analogy.",
        "What are the long-term economic consequences of a universal basic income?"
    ]
    
    results = []
    print("Running Creative Writing...")
    for prompt in tqdm(prompts):
        conditions = [
            ("Control", CONTROL_SYSTEM),
            ("BST-Filler", BST_FILLER_SYSTEM),
            ("BST-Rationale", BST_RATIONALE_SYSTEM)
        ]
        
        for name, system in conditions:
            response = get_response(prompt, system)
            results.append({
                "prompt": prompt,
                "condition": name,
                "response": response
            })
            
    return results

if __name__ == "__main__":
    # Pilot run
    tqa_results = run_truthful_qa(subset_size=20)
    with open("results/tqa_raw.json", "w") as f:
        json.dump(tqa_results, f, indent=2)
        
    creative_results = run_creative_writing()
    with open("results/creative_raw.json", "w") as f:
        json.dump(creative_results, f, indent=2)
    
    print("Experiments complete. Results saved to results/")
