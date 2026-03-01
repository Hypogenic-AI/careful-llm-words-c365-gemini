# REPORT: An LLM That's Careful With Its Words

## 1. Executive Summary
This research investigated whether requiring a Large Language Model (LLM) to generate "thinking tokens" (either meaningless filler tokens or explicit internal rationales) between every sentence would improve its "carefulness," truthfulness, and qualitative depth. We hypothesized that this "Between-Sentence Thinking" (BST) would force the model to deliberate more on each claim.

**Key Finding:** Contrary to our hypothesis, requiring thinking tokens via prompting in a state-of-the-art model (GPT-4o) **consistently degraded** performance across both TruthfulQA and creative writing tasks. The primary qualitative shift was **"Model Shirking"**: when faced with the extra "chore" of generating thinking tokens, the model produced significantly shorter, less detailed, and less comprehensive responses to minimize its total token output. Control models outperformed BST models in 95% of TruthfulQA cases and 100% of creative writing cases, even after the thinking tokens were stripped for evaluation.

## 2. Goal
The goal was to test if increasing inference-time computation at the sentence boundaries of a prompted LLM would lead to more "careful" and insightful generation. We aimed to see if the "dot-by-dot" computation effect (Pfau et al., 2024) could be triggered through simple prompting without specialized training.

## 3. Data Construction
- **TruthfulQA (Subset):** We used a 20-question random subset from the TruthfulQA "generation" set (Misconceptions category). This dataset is designed to elicit common human falsehoods that LLMs often replicate.
- **Creative Writing Prompts:** A set of 3 complex prompts (Detective Story, Quantum Entanglement Explanation, Universal Basic Income Analysis) designed to test depth, style, and reasoning.

## 4. Experiment Description
We compared three conditions:
1. **Control:** Standard zero-shot prompting.
2. **BST-Filler:** Requirement to generate 10 dots (`..........`) after every sentence on a new line.
3. **BST-Rationale:** Requirement to generate an internal rationale wrapped in `<thought>...</thought>` after every sentence on a new line.

### Methodology
- **Model:** `gpt-4o` (OpenAI).
- **Evaluator:** `gpt-4o` as a judge (Pairwise/Triplet comparison).
- **Evaluation Criteria:** Truthfulness, Carefulness, Qualitative Depth.
- **Fairness:** Evaluations were performed both on raw outputs and "stripped" outputs (where thinking tokens were removed) to ensure the judge wasn't biased by the formatting itself.

## 5. Result Analysis

### Quantitative Results (Win Rates)
| Condition | TruthfulQA (Raw) | TruthfulQA (Stripped) | Creative (Raw) | Creative (Stripped) |
|-----------|------------------|-----------------------|----------------|---------------------|
| Control (A)| **19 / 20**      | **19 / 20**           | **3 / 3**      | **3 / 3**           |
| BST-Filler (B)| 1 / 20        | 1 / 20                | 0 / 3          | 0 / 3               |
| BST-Rationale (C)| 0 / 20     | 0 / 20                | 0 / 3          | 0 / 3               |

### Key Findings
1. **Model Shirking (Laziness):** The most prominent effect of the BST constraint was a drastic reduction in response length. On average, BST-Filler responses were **50-70% shorter** than Control responses. The model clearly attempted to minimize the number of sentences it wrote to avoid the repetitive task of generating dots or rationales.
2. **Degraded Depth:** Because the responses were shorter, they lacked the nuances, caveats, and comprehensive details present in the Control group. The LLM judge consistently ranked the Control group higher on "Qualitative Depth" and "Carefulness" due to this missing detail.
3. **Rationale Quality:** In the BST-Rationale condition, the generated thoughts were often superficial (e.g., "I should add more detail now") rather than providing deep semantic planning. This suggests that without reinforcement learning (as in Quiet-STaR or DeepSeek-R1), models do not naturally use forced rationale steps for meaningful computation when prompted.

### Surprises
In exactly one case (TruthfulQA question about Richard Branson), BST-Filler outperformed the Control. In this instance, the filler tokens seemed to coincide with a more detailed biographical account, but this was a significant outlier.

## 6. Conclusions
While theoretical and trained "thinking token" approaches (like Pause Tokens) have shown promise, **simply prompting** a high-end model to use thinking tokens between sentences is ineffective and actually counterproductive. The model perceives the instruction as an overhead cost and responds with "laziness," resulting in qualitatively inferior text that is less careful and less informative.

## 7. Next Steps
1. **Finetuning vs. Prompting:** Replicate this with a finetuned model (e.g., Llama-3-70B finetuned on [PAUSE] tokens) to see if training overcomes the laziness effect.
2. **Length-Controlled Evaluation:** Rerun the experiment with a minimum sentence count constraint to force the model to be detailed despite the BST overhead.
3. **Implicit Pause:** Experiment with "hidden" tokens that are not generated as part of the text but are part of the model's KV cache (requires local model access).
