"""
Program 18: Compare the dataset before and after outlier treatment.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df_original = pd.read_csv("../data/raw_dataset.csv")
df_treated = pd.read_csv("../outputs/17_outliers_capped.csv")

comparison = pd.DataFrame({
    "Original_Mean": df_original[["Age", "Salary", "Score"]].mean(),
    "Treated_Mean": df_treated[["Age", "Salary", "Score"]].mean(),
    "Original_Std": df_original[["Age", "Salary", "Score"]].std(),
    "Treated_Std": df_treated[["Age", "Salary", "Score"]].std(),
    "Original_Max": df_original[["Age", "Salary", "Score"]].max(),
    "Treated_Max": df_treated[["Age", "Salary", "Score"]].max(),
})

print("Comparison before vs after outlier treatment:")
print(comparison)

comparison.to_csv("../outputs/18_outlier_treatment_comparison.csv")
print("Saved to outputs/18_outlier_treatment_comparison.csv")
