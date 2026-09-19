import pandas as pd

df = pd.read_csv("INDUSTRIA-X/data/Model_3.csv")

print("Shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())