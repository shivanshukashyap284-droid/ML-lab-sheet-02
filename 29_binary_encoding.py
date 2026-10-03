"""
Program 29: Perform Binary Encoding on categorical data.
Binary encoding first label-encodes categories into integers, then
converts each integer into its binary representation, spread across
several columns. This uses fewer columns than one-hot encoding when
there are many categories.
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # ensures ../data, ../outputs, ../plots resolve correctly no matter where this script is run from

import pandas as pd
import numpy as np

df = pd.read_csv("../outputs/07_mode_filled.csv")
df_binary = df.copy()

def binary_encode(dataframe, column):
    unique_vals = dataframe[column].unique()
    mapping = {val: i for i, val in enumerate(unique_vals)}
    n_bits = int(np.ceil(np.log2(len(unique_vals)))) if len(unique_vals) > 1 else 1

    codes = dataframe[column].map(mapping)
    for bit in range(n_bits):
        dataframe[f"{column}_bin{bit}"] = codes.apply(lambda x: (x >> bit) & 1)
    return dataframe, mapping

df_binary, department_mapping = binary_encode(df_binary, "Department")
print("Department integer mapping used before binary conversion:", department_mapping)

print("\nSample of binary-encoded columns:")
print(df_binary.filter(like="Department_bin").head())

df_binary.to_csv("../outputs/29_binary_encoded.csv", index=False)
print("Saved to outputs/29_binary_encoded.csv")
