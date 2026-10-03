"""
Program 24: Visualize the effect of normalization using histograms.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
import matplotlib.pyplot as plt

df_original = pd.read_csv("../outputs/05_mean_filled.csv")
df_normalized = pd.read_csv("../outputs/19_minmax_normalized.csv")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].hist(df_original["Salary"], bins=20, color="orange", edgecolor="black")
axes[0].set_title("Salary - Before Normalization")
axes[0].set_xlabel("Salary")

axes[1].hist(df_normalized["Salary"], bins=20, color="green", edgecolor="black")
axes[1].set_title("Salary - After Min-Max Normalization")
axes[1].set_xlabel("Normalized Salary")

plt.tight_layout()
plt.savefig("../plots/24_normalization_histograms.png", dpi=150)
print("Saved to plots/24_normalization_histograms.png")
plt.close()
