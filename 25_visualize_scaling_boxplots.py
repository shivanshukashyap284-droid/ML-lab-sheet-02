"""
Program 25: Visualize the effect of scaling using box plots.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_original = pd.read_csv("../outputs/05_mean_filled.csv")
df_standardized = pd.read_csv("../outputs/20_standardized.csv")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(data=df_original[["Age", "Salary", "Score"]], ax=axes[0])
axes[0].set_title("Before Scaling")

sns.boxplot(data=df_standardized[["Age", "Salary", "Score"]], ax=axes[1])
axes[1].set_title("After Standardization")

plt.tight_layout()
plt.savefig("../plots/25_scaling_boxplots.png", dpi=150)
print("Saved to plots/25_scaling_boxplots.png")
plt.close()
