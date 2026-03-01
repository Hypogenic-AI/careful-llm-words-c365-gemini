# Planning: An LLM That's Careful With Its Words

## Motivation & Novelty Assessment

### Why This Research Matters
As LLMs are increasingly used for critical tasks, ensuring they "think" before they "speak" is vital. Standard LLMs generate text token-by-token in a greedy or sampled fashion, often leading to hallucinations or superficial reasoning. Requiring "thinking time" between sentences could allow the model to refine its internal state and produce more deliberate, accurate, and high-quality text.

### Gap in Existing Work
Most work on thinking tokens (Pause Tokens, Quiet-STaR, Filler Tokens) focuses on training or finetuning models to use these tokens. There is less exploration of how simple *prompt-level* constraints requiring thinking tokens between sentences affect the qualitative nature of the output in high-level tasks, especially using state-of-the-art models via APIs.

### Our Novel Contribution
We will investigate the "Between-Sentence Thinking" (BST) paradigm using prompting with SOTA LLMs. We specifically look at the *qualitative* shifts in language (carefulness, precision, depth) when a model is forced to pause and "reason" (even with filler tokens or hidden thoughts) between every sentence.

### Experiment Justification
- **Experiment 1 (TruthfulQA):** Tests if BST reduces hallucinations/misconceptions (carefulness).
- **Experiment 2 (Creative/Complex Writing):** Tests the qualitative difference in text style and depth using LLM-as-a-judge.
- **Experiment 3 (Ablation):** Compares "Meaningless Fillers" vs "Explicit Rationales" between sentences.

## Research Question
Does requiring an LLM to generate "thinking tokens" between every sentence improve the carefulness and qualitative depth of its output?

## Hypothesis Decomposition
1. **H1:** Forcing pauses (thinking tokens) between sentences leads to higher scores on truthfulness benchmarks.
2. **H2:** The resulting text is perceived as more "deliberate" and "comprehensive" by independent evaluators.
3. **H3:** Explicit rationales (CoT) between sentences are more effective than meaningless filler tokens.

## Proposed Methodology

### Approach
We will use GPT-4o (via OpenRouter or OpenAI API) to perform tasks under three conditions:
1. **Control:** Standard generation.
2. **BST-Filler:** Insert 10 filler tokens (e.g., `.` or `[thinking]`) between sentences.
3. **BST-Rationale:** Generate a 1-sentence internal rationale between every output sentence.

### Experimental Steps
1. **Setup:** Configure API access and select prompts from TruthfulQA and a set of "Complex Planning/Writing" prompts.
2. **Implementation:** Create a wrapper that prompts the model to follow the BST constraints.
3. **Execution:** Run the models on the selected prompts.
4. **Analysis:**
    - Use TruthfulQA evaluation metrics.
    - Use an LLM-as-a-judge (GPT-4o) to compare outputs pairwise (A/B testing) for "carefulness", "clarity", and "depth".

### Baselines
- Standard Zero-shot (Control).
- Standard Chain-of-Thought (at the beginning of the response).

### Evaluation Metrics
- **TruthfulQA Accuracy/Truthfulness.**
- **Win-rate** in pairwise qualitative comparisons.
- **Perplexity/Diversity** metrics (optional).

### Statistical Analysis Plan
- T-tests for TruthfulQA scores.
- Binomial tests for pairwise win-rates.

## Expected Outcomes
We expect BST-Rationale to significantly improve carefulness. BST-Filler might show marginal improvements or even degradation if the model isn't trained to use them, but it tests the "hidden computation" hypothesis for prompted models.

## Success Criteria
- Statistically significant improvement in TruthfulQA or qualitative win-rate for BST methods over control.
- Clear qualitative distinction identified in the text (e.g., more hedges, more precise terms).
