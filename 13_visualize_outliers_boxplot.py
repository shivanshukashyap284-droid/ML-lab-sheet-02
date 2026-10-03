"""
Program 13: Visualize outliers using a Box Plot.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/raw_dataset.csv")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, col in zip(axes, ["Age", "Salary", "Score"]):
    sns.boxplot(y=df[col], ax=ax, color="skyblue")
    ax.set_title(f"Box Plot: {col}")

plt.tight_layout()
plt.savefig("../plots/13_boxplots.png", dpi=150)
print("Box plots saved to plots/13_boxplots.png")
plt.close()
