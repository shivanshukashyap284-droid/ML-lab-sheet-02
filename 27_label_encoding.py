"""
Program 27: Encode categorical variables using Label Encoding.
Label encoding assigns each category an integer (0, 1, 2, ...).
Best used for ordinal data or tree-based models.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("../outputs/07_mode_filled.csv")  # categorical missing values already handled
df_label = df.copy()

le = LabelEncoder()
df_label["Gender_LabelEncoded"] = le.fit_transform(df_label["Gender"])
print("Gender mapping:", dict(zip(le.classes_, le.transform(le.classes_))))

le2 = LabelEncoder()
df_label["Department_LabelEncoded"] = le2.fit_transform(df_label["Department"])
print("Department mapping:", dict(zip(le2.classes_, le2.transform(le2.classes_))))

print("\nSample of encoded columns:")
print(df_label[["Gender", "Gender_LabelEncoded", "Department", "Department_LabelEncoded"]].head())

df_label.to_csv("../outputs/27_label_encoded.csv", index=False)
print("Saved to outputs/27_label_encoded.csv")
