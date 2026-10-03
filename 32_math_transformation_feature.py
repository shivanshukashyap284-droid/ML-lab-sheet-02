"""
Program 32: Create a new feature using mathematical transformations.
Example: a 'Salary_per_Age' ratio and a squared Score feature.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../outputs/05_mean_filled.csv")
df_math = df.copy()

df_math["Salary_per_Age"] = df_math["Salary"] / df_math["Age"]
df_math["Score_Squared"] = df_math["Score"] ** 2

print("Sample of new mathematically-derived features:")
print(df_math[["Salary", "Age", "Salary_per_Age", "Score", "Score_Squared"]].head())

df_math.to_csv("../outputs/32_math_features.csv", index=False)
print("Saved to outputs/32_math_features.csv")
