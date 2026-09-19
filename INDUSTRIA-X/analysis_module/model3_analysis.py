import pandas as pd
import numpy as np

DATA_PATH = "../data/Model_3.csv"

df = pd.read_csv(DATA_PATH)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print(df.head())