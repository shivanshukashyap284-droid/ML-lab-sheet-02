"""
Program 34: Perform Feature Selection using correlation analysis.
Highly correlated features carry redundant information; here we inspect
the correlation matrix of numeric features and flag strong correlations.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../outputs/32_math_features.csv")

numeric_df = df.select_dtypes(include="number")
correlation_matrix = numeric_df.corr()

print("Correlation matrix:")
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Numeric Features")
plt.tight_layout()
plt.savefig("../plots/34_correlation_heatmap.png", dpi=150)
print("Saved heatmap to plots/34_correlation_heatmap.png")
plt.close()

# Flag feature pairs with strong correlation (|r| > 0.8), excluding self-correlation
strong_pairs = []
for i in range(len(correlation_matrix.columns)):
    for j in range(i + 1, len(correlation_matrix.columns)):
        value = correlation_matrix.iloc[i, j]
        if abs(value) > 0.8:
            strong_pairs.append((correlation_matrix.columns[i], correlation_matrix.columns[j], value))

print("\nStrongly correlated feature pairs (|r| > 0.8):")
print(strong_pairs if strong_pairs else "None found")
