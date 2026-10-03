"""
Program 4: Remove columns having more than 50% missing values.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")
print("Original columns:", list(df.columns))

df_copy = df.copy()
missing_pct = df_copy.isnull().mean() * 100

cols_to_drop = missing_pct[missing_pct > 50].index.tolist()
print("Columns with more than 50% missing values:", cols_to_drop)

df_cols_dropped = df_copy.drop(columns=cols_to_drop)
print("Columns after dropping:", list(df_cols_dropped.columns))

df_cols_dropped.to_csv("../outputs/04_columns_dropped.csv", index=False)
print("Saved to outputs/04_columns_dropped.csv")
