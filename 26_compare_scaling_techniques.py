"""
Program 26: Compare different scaling techniques on the same dataset.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df_original = pd.read_csv("../outputs/05_mean_filled.csv")
df_minmax = pd.read_csv("../outputs/19_minmax_normalized.csv")
df_standard = pd.read_csv("../outputs/20_standardized.csv")
df_robust = pd.read_csv("../outputs/21_robust_scaled.csv")
df_maxabs = pd.read_csv("../outputs/22_maxabs_scaled.csv")

col = "Salary"
comparison = pd.DataFrame({
    "Original": df_original[col],
    "MinMax": df_minmax[col],
    "Standard": df_standard[col],
    "Robust": df_robust[col],
    "MaxAbs": df_maxabs[col],
})

print(f"Comparison of scaling techniques on '{col}' column (first 10 rows):")
print(comparison.head(10))

print("\nSummary statistics of each scaling technique:")
print(comparison.describe())

comparison.to_csv("../outputs/26_scaling_technique_comparison.csv", index=False)
print("Saved to outputs/26_scaling_technique_comparison.csv")
