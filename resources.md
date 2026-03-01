# Resources Catalog

## Summary
This document catalogs all resources gathered for the research project "An LLM That's Careful With Its Words", which explores the effects of thinking tokens on LLM text quality and reasoning.

## Papers
Total papers downloaded: 5

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| Let's Think Dot by Dot | Pfau et al. | 2024 | papers/2404.15758_Pfau_DotByDot.pdf | Filler tokens for hidden computation. |
| Think Before You Speak (Pause Tokens) | Goyal et al. | 2023 | papers/2310.02226_Goyal_PauseTokens.pdf | [PAUSE] tokens for better reasoning. |
| Quiet-STaR | Zelikman et al. | 2024 | papers/2403.09629_Zelikman_QuietSTaR.pdf | Tokenwise parallel rationales. |
| Pause Tokens Theory | London & Kanade | 2025 | papers/2505.21024_London_PauseTokensTheory.pdf | Proof of increased expressivity. |
| Rethinking Thinking Tokens | Vennam et al. | 2024 | papers/2411.11371_Vennam_RethinkingThinkingTokens.pdf | Underperformance of single-embedding TT. |

## Datasets
Total datasets downloaded: 2

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| GSM8K | HuggingFace | 1319 (test) | Math Reasoning | datasets/gsm8k/ | Standard for reasoning. |
| TruthfulQA | HuggingFace | 817 (val) | QA (Hallucination) | datasets/truthful_qa/ | Good for "carefulness". |

## Code Repositories
Total repositories cloned: 3

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| Quiet-STaR | ezelikman/quiet-star | Rationales impl | code/quiet-star/ | Patching Mistral for thoughts. |
| Filler Tokens | rokosbasilisk/filler-tokens | Dot-by-dot experiments | code/filler-tokens/ | Algorithmic tasks. |
| Pause Token | epfl-dlab/PauseToken | [PAUSE] token impl | code/pause-token/ | Better reasoning. |

## Recommendations for Experiment Design

1.  **Primary Dataset(s)**:
    -   **GSM8K**: To measure reasoning accuracy (standard benchmark).
    -   **TruthfulQA**: To measure "carefulness" in avoiding common misconceptions.
2.  **Baseline Methods**:
    -   **Standard Zero-shot/Few-shot**: No thinking tokens.
    -   **Explicit Chain-of-Thought (CoT)**: Human-readable reasoning steps.
3.  **Evaluation Metrics**:
    -   **Accuracy (Exact Match)** for GSM8K.
    -   **Truthfulness/Informativeness** (using an LLM judge) for TruthfulQA.
    -   **Qualitative Score** (LLM-as-a-judge) for assessing "carefulness" and "depth" in open-ended generation.
4.  **Code to Adapt/Reuse**:
    -   `code/quiet-star` provides a template for integrating thoughts at the token level.
    -   `code/pause-token` provides scripts for inserting special tokens during the generation process.
