"""
Program 31: Extract year, month, and day from a date column.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../data/raw_dataset.csv")
df_dates = df.copy()

df_dates["JoiningDate"] = pd.to_datetime(df_dates["JoiningDate"])

df_dates["Joining_Year"] = df_dates["JoiningDate"].dt.year
df_dates["Joining_Month"] = df_dates["JoiningDate"].dt.month
df_dates["Joining_Day"] = df_dates["JoiningDate"].dt.day
df_dates["Joining_Weekday"] = df_dates["JoiningDate"].dt.day_name()

print("Sample of extracted date features:")
print(df_dates[["JoiningDate", "Joining_Year", "Joining_Month", "Joining_Day", "Joining_Weekday"]].head())

df_dates.to_csv("../outputs/31_date_features_extracted.csv", index=False)
print("Saved to outputs/31_date_features_extracted.csv")
