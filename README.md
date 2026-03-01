# Careful LLM Words (BST Research)

This project investigates the effects of "Between-Sentence Thinking" (BST) on LLM text quality, specifically using GPT-4o.

## Key Findings
- **Model Shirking:** Requiring thinking tokens (dots or rationales) between sentences via prompting consistently **degrades** performance by making the model more concise and less detailed.
- **Control Wins:** In 95% of TruthfulQA cases and 100% of creative writing cases, the control model (no thinking tokens) was preferred by an LLM-as-a-judge (even after stripping thinking tokens).
- **Instruction Overhead:** Forcing an LLM to generate extra tokens for "thinking" at the prompt level is perceived as a cost to be minimized, leading to shorter and less careful responses.

## Repository Structure
- `src/`: Python scripts for experiments, evaluation, and analysis.
- `results/`: Raw and evaluated results in JSON format.
- `figures/`: Visualizations of winner counts and rankings.
- `planning.md`: Initial research plan and hypothesis.
- `REPORT.md`: Full research report with detailed findings.

## How to Reproduce
1. Install dependencies: `uv pip install -r requirements.txt`.
2. Set `OPENAI_API_KEY`.
3. Run `python src/experiment.py` (requires ~70 API calls).
4. Run `python src/evaluate.py` and `python src/evaluate_stripped.py`.
5. Run `python src/analyze.py`.

## Data
- **TruthfulQA:** Local arrow file in `datasets/truthful_qa/`.
- **Creative Writing:** Custom prompts in `src/experiment.py`.

## Full Report
See [REPORT.md](REPORT.md) for a comprehensive analysis of the results and methodological details.