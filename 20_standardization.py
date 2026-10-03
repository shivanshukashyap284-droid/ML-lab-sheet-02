"""
Program 20: Apply Standardization (Z-score Scaling).
Formula: X_scaled = (X - mean) / std_dev  -> mean 0, std 1
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("../outputs/05_mean_filled.csv")
df_standardized = df.copy()

numeric_cols = ["Age", "Salary", "Score"]

scaler = StandardScaler()
df_standardized[numeric_cols] = scaler.fit_transform(df_standardized[numeric_cols])

print("Data after Standardization (first 5 rows):")
print(df_standardized[numeric_cols].head())
print("\nMean after scaling (should be ~0):")
print(df_standardized[numeric_cols].mean())
print("\nStd after scaling (should be ~1):")
print(df_standardized[numeric_cols].std())

df_standardized.to_csv("../outputs/20_standardized.csv", index=False)
print("Saved to outputs/20_standardized.csv")
