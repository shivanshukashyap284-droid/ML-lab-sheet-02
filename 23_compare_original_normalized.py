"""
Program 23: Compare original and normalized datasets.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df_original = pd.read_csv("../outputs/05_mean_filled.csv")
df_normalized = pd.read_csv("../outputs/19_minmax_normalized.csv")

numeric_cols = ["Age", "Salary", "Score"]

comparison = pd.DataFrame({
    "Original_Min": df_original[numeric_cols].min(),
    "Normalized_Min": df_normalized[numeric_cols].min(),
    "Original_Max": df_original[numeric_cols].max(),
    "Normalized_Max": df_normalized[numeric_cols].max(),
    "Original_Mean": df_original[numeric_cols].mean(),
    "Normalized_Mean": df_normalized[numeric_cols].mean(),
})

print("Comparison of original vs Min-Max normalized data:")
print(comparison)

comparison.to_csv("../outputs/23_normalization_comparison.csv")
print("Saved to outputs/23_normalization_comparison.csv")
