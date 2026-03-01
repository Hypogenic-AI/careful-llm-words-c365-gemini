# Literature Review: An LLM That's Careful With Its Words

## Research Area Overview
The research focuses on enhancing the reasoning capabilities and output quality of Large Language Models (LLMs) by increasing inference-time computation. Specifically, it explores the use of "thinking tokens" or "pause tokens"—intermediate tokens that do not necessarily represent human-readable reasoning but provide the model with additional computational steps before generating the final output.

## Key Papers

### 1. Let's Think Dot by Dot: Hidden Computation in Transformer Language Models (2024)
- **Authors**: Jacob Pfau, William Merrill, Samuel R. Bowman
- **arXiv**: 2404.15758
- **Key Contribution**: Shows that transformers can use "meaningless filler tokens" (e.g., '......') to perform complex computations that they cannot perform in a single step.
- **Methodology**: Evaluates models on hard algorithmic tasks (e.g., parity, 3SUM) with and without filler tokens.
- **Results**: Filler tokens can substitute for Chain-of-Thought (CoT) in certain tasks, but training models to use them effectively is difficult and requires specific supervision.
- **Relevance**: Directly supports the hypothesis that extra tokens (even if meaningless) can improve model "carefulness" or computational depth.

### 2. Think Before You Speak: Training Language Models With Pause Tokens (2023)
- **Authors**: Sachin Goyal et al.
- **arXiv**: 2310.02226
- **Key Contribution**: Introduces the "[PAUSE]" token as a way to delay output and allow for extra computation.
- **Methodology**: Pretrains and finetunes models with sequences of [PAUSE] tokens.
- **Results**: Significant gains on SQuAD (+18% EM), CommonSenseQA (+8%), and GSM8K when models are trained with these delays.
- **Relevance**: Provides a practical implementation of "thinking tokens" and shows empirical benefits for reasoning.

### 3. Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking (2024)
- **Authors**: Eric Zelikman et al.
- **arXiv**: 2403.09629
- **Key Contribution**: Generalizes the Self-Taught Reasoner (STaR) to allow LMs to generate unstated rationales (internal thoughts) for *any* text, not just QA.
- **Methodology**: Tokenwise parallel sampling of rationales at each token, optimized via reinforcement learning (REINFORCE).
- **Results**: Improvements on GSM8K and CommonsenseQA without task-specific finetuning.
- **Relevance**: Shows that "thinking" can be integrated into the general generation process, making the model more "careful" with every token.

### 4. Pause Tokens Strictly Increase the Expressivity of Constant-Depth Transformers (2025)
- **Authors**: Charles London, Varun Kanade
- **arXiv**: 2505.21024
- **Key Contribution**: Provides a formal theoretical separation proving that pause tokens strictly increase the computational expressivity of constant-depth Transformers.
- **Relevance**: Offers a theoretical foundation for why the proposed hypothesis (extra tokens -> more careful/better generation) should hold.

### 5. Rethinking Thinking Tokens: Understanding Why They Underperform in Practice (2024)
- **Authors**: Sreeram Vennam et al.
- **arXiv**: 2411.11371
- **Key Contribution**: Critiques the "Thinking Tokens" approach, showing it often underperforms compared to explicit CoT.
- **Findings**: Reliance on a single embedding for thinking tokens may lead to noisy gradients and inconsistent learning signals.
- **Relevance**: Provides a necessary counter-perspective and highlights potential pitfalls (e.g., the need for diverse or learned embeddings for thoughts).

## Common Methodologies
1. **Filler/Pause Tokens**: Inserting a fixed or learned token multiple times before the answer.
2. **Latent/Quiet Reasoning**: Generating rationales that are either hidden or used to influence the next "real" token.
3. **Reinforcement Learning**: Using RL (like REINFORCE or GRPO) to reward the model when "thinking" leads to better predictions.

## Standard Baselines
- **Standard Greedy/Sampling**: No extra tokens.
- **Chain-of-Thought (CoT)**: Explicit human-readable reasoning steps.
- **Self-Consistency**: Multiple CoT paths and majority voting.

## Evaluation Metrics
- **Accuracy/Exact Match**: For benchmarks like GSM8K, SQuAD.
- **Perplexity**: For general text generation quality.
- **Human Evaluation / LLM-as-a-Judge**: For qualitative differences in text (as mentioned in the hypothesis).

## Recommendations for Our Experiment
1. **Implementation**: Use a special `<thought>` token or simple filler tokens like `.` or `...` between sentences.
2. **Datasets**: Use **GSM8K** for reasoning and **TruthfulQA** for "carefulness" in factual claims.
3. **Evaluation**: Compare standard output vs. "Thinking Token" output using an LLM-as-a-judge (e.g., GPT-4) to assess "carefulness", "depth", and "qualitative differences".
4. **Contrast**: Specifically test the "between every sentence" constraint as proposed in the hypothesis.
