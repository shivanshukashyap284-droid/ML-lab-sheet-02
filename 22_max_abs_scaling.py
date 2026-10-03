"""
Program 22: Apply Max Absolute Scaling.
Formula: X_scaled = X / |X_max|  -> range [-1, 1]
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
from sklearn.preprocessing import MaxAbsScaler

df = pd.read_csv("../outputs/05_mean_filled.csv")
df_maxabs = df.copy()

numeric_cols = ["Age", "Salary", "Score"]

scaler = MaxAbsScaler()
df_maxabs[numeric_cols] = scaler.fit_transform(df_maxabs[numeric_cols])

print("Data after Max Absolute Scaling (first 5 rows):")
print(df_maxabs[numeric_cols].head())

df_maxabs.to_csv("../outputs/22_maxabs_scaled.csv", index=False)
print("Saved to outputs/22_maxabs_scaled.csv")
