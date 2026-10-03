"""
Program 8: Fill missing values using forward fill (Forward Propagation).
Forward fill copies the previous valid value down into the missing cell.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")
df_ffill = df.copy()

print("Missing values BEFORE forward fill:")
print(df_ffill.isnull().sum())

df_ffill = df_ffill.ffill()

print("\nMissing values AFTER forward fill:")
print(df_ffill.isnull().sum())
# Note: if the very first row has a missing value, ffill cannot fill it
# since there is no previous value to copy from.

df_ffill.to_csv("../outputs/08_forward_filled.csv", index=False)
print("Saved to outputs/08_forward_filled.csv")
