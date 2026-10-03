"""
Program 6: Replace missing numerical values using the median.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")
df_median_filled = df.copy()

numeric_cols = df_median_filled.select_dtypes(include="number").columns

for col in numeric_cols:
    if df_median_filled[col].isnull().sum() > 0:
        median_value = df_median_filled[col].median()
        df_median_filled[col] = df_median_filled[col].fillna(median_value)
        print(f"Filled '{col}' missing values with median = {median_value:.2f}")

print("\nRemaining missing values in numeric columns:")
print(df_median_filled[numeric_cols].isnull().sum())

df_median_filled.to_csv("../outputs/06_median_filled.csv", index=False)
print("Saved to outputs/06_median_filled.csv")
