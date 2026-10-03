"""
Program 7: Replace missing categorical values using the mode.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")
df_mode_filled = df.copy()

categorical_cols = df_mode_filled.select_dtypes(include="object").columns
print("Categorical columns:", list(categorical_cols))

for col in categorical_cols:
    if df_mode_filled[col].isnull().sum() > 0:
        mode_value = df_mode_filled[col].mode(dropna=True)
        if not mode_value.empty:
            mode_value = mode_value[0]
            df_mode_filled[col] = df_mode_filled[col].fillna(mode_value)
            print(f"Filled '{col}' missing values with mode = '{mode_value}'")

print("\nRemaining missing values in categorical columns:")
print(df_mode_filled[categorical_cols].isnull().sum())

df_mode_filled.to_csv("../outputs/07_mode_filled.csv", index=False)
print("Saved to outputs/07_mode_filled.csv")
