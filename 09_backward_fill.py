"""
Program 9: Fill missing values using backward fill (Backward Propagation).
Backward fill copies the NEXT valid value up into the missing cell.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")
df_bfill = df.copy()

print("Missing values BEFORE backward fill:")
print(df_bfill.isnull().sum())

df_bfill = df_bfill.bfill()

print("\nMissing values AFTER backward fill:")
print(df_bfill.isnull().sum())
# Note: if the very last row has a missing value, bfill cannot fill it
# since there is no following value to copy from.

df_bfill.to_csv("../outputs/09_backward_filled.csv", index=False)
print("Saved to outputs/09_backward_filled.csv")
