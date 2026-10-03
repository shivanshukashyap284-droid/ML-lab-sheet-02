"""
Program 30: Create a new feature by combining two existing columns.
Here we combine 'Department' and 'City' into a single descriptive feature.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd

df = pd.read_csv("../outputs/07_mode_filled.csv")
df_new_feature = df.copy()

df_new_feature["Department_City"] = df_new_feature["Department"] + "_" + df_new_feature["City"]

print("Sample of the new combined feature:")
print(df_new_feature[["Department", "City", "Department_City"]].head())

df_new_feature.to_csv("../outputs/30_combined_feature.csv", index=False)
print("Saved to outputs/30_combined_feature.csv")
