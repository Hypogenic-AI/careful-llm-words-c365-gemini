import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_evaluations(eval_file, output_prefix):
    """Analyze the LLM-as-a-judge evaluations."""
    if not os.path.exists(eval_file):
        print(f"File {eval_file} not found.")
        return None
        
    with open(eval_file, "r") as f:
        evals = json.load(f)
        
    df = pd.DataFrame(evals)
    
    # Count winners
    winner_counts = df['overall_winner'].value_counts()
    print(f"Winner counts for {output_prefix}:")
    print(winner_counts)
    
    # Analyze rankings
    rank_counts = {
        "truthfulness": {"A": 0, "B": 0, "C": 0},
        "carefulness": {"A": 0, "B": 0, "C": 0},
        "depth": {"A": 0, "B": 0, "C": 0}
    }
    
    for _, row in df.iterrows():
        rankings = row['rankings']
        for criterion in rank_counts:
            # Rankings are in order (1st, 2nd, 3rd)
            winner = rankings[criterion][0]
            if winner in rank_counts[criterion]:
                rank_counts[criterion][winner] += 1
            
    # Visualize
    plt.figure(figsize=(10, 6))
    plt.title(f"Overall Winner Counts: {output_prefix}")
    sns.barplot(x=winner_counts.index, y=winner_counts.values)
    plt.ylabel("Count")
    plt.xlabel("Condition (A: Control, B: BST-Filler, C: BST-Rationale)")
    plt.savefig(f"figures/{output_prefix}_winners.png")
    
    # Plot rankings per criterion
    rank_df = pd.DataFrame(rank_counts)
    rank_df.plot(kind='bar', figsize=(12, 8))
    plt.title(f"First-Place Rankings by Criterion: {output_prefix}")
    plt.ylabel("Count")
    plt.xlabel("Condition (A: Control, B: BST-Filler, C: BST-Rationale)")
    plt.savefig(f"figures/{output_prefix}_rankings.png")
    
    return winner_counts

if __name__ == "__main__":
    print("Analyzing raw evaluations...")
    analyze_evaluations("results/tqa_eval.json", "tqa_raw")
    analyze_evaluations("results/creative_eval.json", "creative_raw")
    
    print("\nAnalyzing stripped evaluations...")
    analyze_evaluations("results/tqa_eval_stripped.json", "tqa_stripped")
    analyze_evaluations("results/creative_eval_stripped.json", "creative_stripped")
    
    print("Analysis complete. Plots saved to figures/")