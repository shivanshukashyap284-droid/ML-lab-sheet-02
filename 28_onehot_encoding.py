"""
Program 28: Encode categorical variables using One-Hot Encoding.
Each category becomes its own binary (0/1) column. Best for nominal
(non-ordered) categories used with models like linear regression.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../outputs/07_mode_filled.csv")
df_onehot = df.copy()

df_onehot = pd.get_dummies(df_onehot, columns=["City", "Department"], prefix=["City", "Dept"])

print("Columns after One-Hot Encoding:")
print(list(df_onehot.columns))

print("\nSample rows:")
print(df_onehot.filter(like="City_").head())

df_onehot.to_csv("../outputs/28_onehot_encoded.csv", index=False)
print("Saved to outputs/28_onehot_encoded.csv")
