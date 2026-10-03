"""
Program 5: Replace missing numerical values using the mean.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")
df_mean_filled = df.copy()

numeric_cols = df_mean_filled.select_dtypes(include="number").columns
print("Numeric columns:", list(numeric_cols))

for col in numeric_cols:
    if df_mean_filled[col].isnull().sum() > 0:
        mean_value = df_mean_filled[col].mean()
        df_mean_filled[col] = df_mean_filled[col].fillna(mean_value)
        print(f"Filled '{col}' missing values with mean = {mean_value:.2f}")

print("\nRemaining missing values in numeric columns:")
print(df_mean_filled[numeric_cols].isnull().sum())

df_mean_filled.to_csv("../outputs/05_mean_filled.csv", index=False)
print("Saved to outputs/05_mean_filled.csv")
