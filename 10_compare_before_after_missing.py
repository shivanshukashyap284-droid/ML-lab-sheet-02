"""
Program 10: Compare the dataset before and after handling missing values.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df_original = pd.read_csv("../data/raw_dataset.csv")
df_cleaned = pd.read_csv("../outputs/05_mean_filled.csv")  # mean-filled version as the "after" dataset

comparison = pd.DataFrame({
    "Missing_Before": df_original.isnull().sum(),
    "Missing_After": df_cleaned.isnull().sum()
})
comparison["Values_Filled"] = comparison["Missing_Before"] - comparison["Missing_After"]

print("Comparison of missing values before vs after cleaning:")
print(comparison)

print("\nShape before:", df_original.shape)
print("Shape after :", df_cleaned.shape)

comparison.to_csv("../outputs/10_missing_value_comparison.csv")
print("Saved comparison table to outputs/10_missing_value_comparison.csv")
