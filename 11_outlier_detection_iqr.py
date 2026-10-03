"""
Program 11: Detect outliers using the Interquartile Range (IQR) method.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")

def detect_outliers_iqr(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return series[(series < lower_bound) | (series > upper_bound)], lower_bound, upper_bound

for col in ["Salary", "Score", "Age"]:
    outliers, lower, upper = detect_outliers_iqr(df[col].dropna())
    print(f"\nColumn: {col}")
    print(f"  Lower bound: {lower:.2f}, Upper bound: {upper:.2f}")
    print(f"  Number of outliers: {len(outliers)}")
    print(f"  Outlier values: {outliers.values}")
