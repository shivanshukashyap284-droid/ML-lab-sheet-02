"""
Program 1: Load a dataset and identify missing values in each column.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

# Load the raw dataset
df = pd.read_csv("../data/raw_dataset.csv")

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# Count missing values in each column
missing_counts = df.isnull().sum()

print("\nMissing values per column:")
print(missing_counts)

print("\nColumns with at least one missing value:")
print(missing_counts[missing_counts > 0])
