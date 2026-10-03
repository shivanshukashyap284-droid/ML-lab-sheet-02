"""
Program 21: Apply Robust Scaling to handle outliers.
Formula: X_scaled = (X - median) / IQR
Robust scaling uses median and IQR instead of mean/std, so it is less
affected by extreme outliers.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
from sklearn.preprocessing import RobustScaler

df = pd.read_csv("../outputs/05_mean_filled.csv")
df_robust = df.copy()

numeric_cols = ["Age", "Salary", "Score"]

scaler = RobustScaler()
df_robust[numeric_cols] = scaler.fit_transform(df_robust[numeric_cols])

print("Data after Robust Scaling (first 5 rows):")
print(df_robust[numeric_cols].head())

df_robust.to_csv("../outputs/21_robust_scaled.csv", index=False)
print("Saved to outputs/21_robust_scaled.csv")
