"""
Program 19: Apply Min-Max Normalization to numerical features.
Formula: X_scaled = (X - X_min) / (X_max - X_min)  -> range [0, 1]
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("../outputs/05_mean_filled.csv")  # use already-cleaned (no missing) data
df_minmax = df.copy()

numeric_cols = ["Age", "Salary", "Score"]

scaler = MinMaxScaler()
df_minmax[numeric_cols] = scaler.fit_transform(df_minmax[numeric_cols])

print("Data after Min-Max Normalization (first 5 rows):")
print(df_minmax[numeric_cols].head())

df_minmax.to_csv("../outputs/19_minmax_normalized.csv", index=False)
print("Saved to outputs/19_minmax_normalized.csv")
