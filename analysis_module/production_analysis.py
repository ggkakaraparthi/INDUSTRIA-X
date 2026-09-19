import pandas as pd

df = pd.read_csv("data/Model_1.csv")

# Remove completely empty columns
df = df.dropna(axis=1, how="all")

print("\n--- THROUGHPUT ANALYSIS ---")

throughput = df["Parts per hour"]

print("Average Throughput:", throughput.mean())
print("Minimum Throughput:", throughput.min())
print("Maximum Throughput:", throughput.max())
print("Median Throughput:", throughput.median())
print("Throughput Standard Deviation:", throughput.std())

print("\n--- PRODUCTION VOLUME ---")

print("Average Total Parts:", df["Total parts"].mean())
print("Minimum Total Parts:", df["Total parts"].min())
print("Maximum Total Parts:", df["Total parts"].max())
