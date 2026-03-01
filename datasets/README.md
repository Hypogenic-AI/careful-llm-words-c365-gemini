# Downloaded Datasets

This directory contains datasets for the research project "An LLM That's Careful With Its Words".

## Dataset 1: GSM8K (test split)
- **Source**: [openai/gsm8k](https://huggingface.co/datasets/gsm8k)
- **Format**: HuggingFace Dataset
- **Task**: Mathematical word problems (Grade School Math 8K)
- **Use**: Evaluate reasoning and problem-solving quality.

## Dataset 2: TruthfulQA (generation, validation split)
- **Source**: [truthful_qa](https://huggingface.co/datasets/truthful_qa)
- **Format**: HuggingFace Dataset
- **Task**: Question answering on topics prone to hallucinations/misconceptions.
- **Use**: Evaluate factual correctness and "carefulness" in avoiding false claims.

## Download Instructions
These datasets were downloaded using the `datasets` library:
```python
from datasets import load_dataset
gsm8k = load_dataset('gsm8k', 'main', split='test')
gsm8k.save_to_disk('datasets/gsm8k')
tqa = load_dataset('truthful_qa', 'generation', split='validation')
tqa.save_to_disk('datasets/truthful_qa')
```
