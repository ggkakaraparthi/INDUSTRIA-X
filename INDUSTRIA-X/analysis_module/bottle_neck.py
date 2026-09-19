print("Bottleneck analysis started!")

import pandas as pd

df = pd.read_csv("data/Model_1.csv")

print("Dataset shape:")
print(df.shape)

print("Column names:")
print(df.columns.tolist())