"""
Program 17: Cap outliers using percentile-based capping (Winsorization).
Values below the 1st percentile are set to the 1st percentile value,
values above the 99th percentile are set to the 99th percentile value.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")
df_capped = df.copy()

for col in ["Salary", "Score"]:
    lower_cap = df_capped[col].quantile(0.01)
    upper_cap = df_capped[col].quantile(0.99)
    print(f"'{col}': capping below {lower_cap:.2f} and above {upper_cap:.2f}")
    df_capped[col] = df_capped[col].clip(lower=lower_cap, upper=upper_cap)

df_capped.to_csv("../outputs/17_outliers_capped.csv", index=False)
print("Saved to outputs/17_outliers_capped.csv")
