"""
Program 15: Remove outliers using the IQR method.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")
df_no_outliers = df.copy()

def get_iqr_bounds(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr

print("Shape before removing outliers:", df_no_outliers.shape)

for col in ["Salary", "Score"]:
    lower, upper = get_iqr_bounds(df_no_outliers[col].dropna())
    df_no_outliers = df_no_outliers[
        (df_no_outliers[col].isnull()) | ((df_no_outliers[col] >= lower) & (df_no_outliers[col] <= upper))
    ]

print("Shape after removing outliers:", df_no_outliers.shape)

df_no_outliers.to_csv("../outputs/15_outliers_removed.csv", index=False)
print("Saved to outputs/15_outliers_removed.csv")
