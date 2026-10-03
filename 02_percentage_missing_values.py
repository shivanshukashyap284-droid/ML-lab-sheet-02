"""
Program 2: Display the percentage of missing values in every feature.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")

total_rows = len(df)
missing_percentage = (df.isnull().sum() / total_rows) * 100
missing_percentage = missing_percentage.round(2)

print("Percentage of missing values per column:")
print(missing_percentage)

# Sort descending for easy interpretation
print("\nSorted by highest missing percentage:")
print(missing_percentage.sort_values(ascending=False))
