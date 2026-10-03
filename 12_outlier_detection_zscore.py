"""
Program 12: Detect outliers using the Z-score method.
A Z-score tells us how many standard deviations a value is from the mean.
Common threshold: |Z| > 3 is considered an outlier.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
from scipy import stats
import numpy as np

df = pd.read_csv("../data/raw_dataset.csv")

def detect_outliers_zscore(series, threshold=3):
    clean_series = series.dropna()
    z_scores = np.abs(stats.zscore(clean_series))
    outliers = clean_series[z_scores > threshold]
    return outliers

for col in ["Salary", "Score", "Age"]:
    outliers = detect_outliers_zscore(df[col])
    print(f"\nColumn: {col}")
    print(f"  Number of outliers (|Z| > 3): {len(outliers)}")
    print(f"  Outlier values: {outliers.values}")
