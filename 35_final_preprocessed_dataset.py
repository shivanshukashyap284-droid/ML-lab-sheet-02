"""
Program 35: Create a final preprocessed dataset ready for Machine Learning.

Pipeline applied (on a fresh copy of the raw data):
1. Drop the 'Remarks' column (>50% missing).
2. Fill missing numeric values with the median.
3. Fill missing categorical values with the mode.
4. Cap outliers in Salary and Score using percentile-based capping.
5. Extract Year/Month/Day from JoiningDate, then drop the raw date column.
6. Encode categorical columns with One-Hot Encoding.
7. Apply Standardization to numeric columns.
8. Save the final, ML-ready dataset.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("../data/raw_dataset.csv")
final_df = df.copy()

# Step 1: drop high-missing column
final_df = final_df.drop(columns=["Remarks"])

# Step 2: fill numeric missing values with median
numeric_cols = ["Age", "Salary", "Score"]
for col in numeric_cols:
    final_df[col] = final_df[col].fillna(final_df[col].median())

# Step 3: fill categorical missing values with mode
categorical_cols = ["Gender", "City"]
for col in categorical_cols:
    final_df[col] = final_df[col].fillna(final_df[col].mode()[0])

# Step 4: cap outliers (1st-99th percentile) in Salary and Score
for col in ["Salary", "Score"]:
    lower_cap = final_df[col].quantile(0.01)
    upper_cap = final_df[col].quantile(0.99)
    final_df[col] = final_df[col].clip(lower=lower_cap, upper=upper_cap)

# Step 5: extract date parts, then drop original date + Name (identifier, not predictive)
final_df["JoiningDate"] = pd.to_datetime(final_df["JoiningDate"])
final_df["Joining_Year"] = final_df["JoiningDate"].dt.year
final_df["Joining_Month"] = final_df["JoiningDate"].dt.month
final_df["Joining_Day"] = final_df["JoiningDate"].dt.day
final_df = final_df.drop(columns=["JoiningDate", "Name"])

# Step 6: one-hot encode categorical columns
final_df = pd.get_dummies(final_df, columns=["Gender", "City", "Department"])

# Step 7: standardize numeric columns
scaler = StandardScaler()
final_df[numeric_cols] = scaler.fit_transform(final_df[numeric_cols])

print("Final preprocessed dataset shape:", final_df.shape)
print("\nColumns:", list(final_df.columns))
print("\nMissing values remaining:", final_df.isnull().sum().sum())
print("\nSample rows:")
print(final_df.head())

final_df.to_csv("../outputs/35_final_ml_ready_dataset.csv", index=False)
print("\nSaved final dataset to outputs/35_final_ml_ready_dataset.csv")
