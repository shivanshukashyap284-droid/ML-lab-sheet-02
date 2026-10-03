"""
Program 16: Replace outliers with the median value.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")
df_replaced = df.copy()

def get_iqr_bounds(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr

for col in ["Salary", "Score"]:
    lower, upper = get_iqr_bounds(df_replaced[col].dropna())
    median_value = df_replaced[col].median()
    outlier_mask = (df_replaced[col] < lower) | (df_replaced[col] > upper)
    print(f"'{col}': replacing {outlier_mask.sum()} outliers with median = {median_value:.2f}")
    df_replaced.loc[outlier_mask, col] = median_value

df_replaced.to_csv("../outputs/16_outliers_replaced_median.csv", index=False)
print("Saved to outputs/16_outliers_replaced_median.csv")
