import pandas as pd

df = pd.read_csv("data/Model_1.csv")

# Remove empty columns
df = df.dropna(axis=1, how="all")

print("Dataset shape after cleaning:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nAverage Waiting Time:")
print(df[[
    "Drilling Waiting Time",
    "Milling Waiting Time",
    "Assembly Waiting Time"
]].mean())

print("\nAverage Utilization:")
print(df[[
    "Drilling Util",
    "Milling Util",
    "Assembly Util"
]].mean())