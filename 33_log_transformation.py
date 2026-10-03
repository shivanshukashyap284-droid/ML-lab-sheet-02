"""
Program 33: Apply Log Transformation to skewed data.
Log transformation reduces right-skew and compresses large outlier
values, making distributions closer to normal.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../outputs/05_mean_filled.csv")
df_log = df.copy()

print("Skewness BEFORE log transform (Salary):", df_log["Salary"].skew())

# log1p handles zero values safely (log(1+x))
df_log["Salary_Log"] = np.log1p(df_log["Salary"])

print("Skewness AFTER log transform (Salary):", df_log["Salary_Log"].skew())

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].hist(df_log["Salary"], bins=20, color="salmon", edgecolor="black")
axes[0].set_title("Salary - Before Log Transform")
axes[1].hist(df_log["Salary_Log"], bins=20, color="skyblue", edgecolor="black")
axes[1].set_title("Salary - After Log Transform")
plt.tight_layout()
plt.savefig("../plots/33_log_transformation.png", dpi=150)
print("Saved plot to plots/33_log_transformation.png")
plt.close()

df_log.to_csv("../outputs/33_log_transformed.csv", index=False)
print("Saved to outputs/33_log_transformed.csv")
