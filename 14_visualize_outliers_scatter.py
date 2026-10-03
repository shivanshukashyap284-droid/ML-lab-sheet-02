"""
Program 14: Visualize outliers using a Scatter Plot.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/raw_dataset.csv")

plt.figure(figsize=(8, 6))
plt.scatter(df.index, df["Salary"], alpha=0.6, color="teal", label="Salary")
plt.axhline(y=df["Salary"].mean(), color="red", linestyle="--", label="Mean Salary")
plt.title("Scatter Plot: Salary values (outliers appear far from the cluster)")
plt.xlabel("Row Index")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("../plots/14_scatter_salary.png", dpi=150)
print("Scatter plot saved to plots/14_scatter_salary.png")
plt.close()
