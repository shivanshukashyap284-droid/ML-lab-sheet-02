"""
Program 3: Remove rows containing missing values from the dataset.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")
print("Original shape:", df.shape)

# Work on a copy so the original dataset stays untouched
df_no_missing_rows = df.copy()
df_no_missing_rows = df_no_missing_rows.dropna(axis=0)

print("Shape after dropping rows with ANY missing value:", df_no_missing_rows.shape)

df_no_missing_rows.to_csv("../outputs/03_rows_dropped.csv", index=False)
print("Saved to outputs/03_rows_dropped.csv")
