import pandas as pd

df = pd.read_csv("data/Model_1.csv")

# Remove completely empty columns
df = df.dropna(axis=1, how="all")

print("\n--- ROOT-CAUSE / RELATIONSHIP ANALYSIS ---")

# Variables to analyze
columns = [
    "Demand",
    "Total parts",
    "Parts per hour",
    "VA Time",
    "Drilling Waiting Time",
    "Milling Waiting Time",
    "Assembly Waiting Time",
    "Drilling Util",
    "Milling Util",
    "Assembly Util"
]

# Correlation matrix
correlation = df[columns].corr()

print("\nCorrelation with Assembly Waiting Time:")
print(
    correlation["Assembly Waiting Time"]
    .sort_values(ascending=False)
)

print("\nCorrelation with Parts per Hour:")
print(
    correlation["Parts per hour"]
    .sort_values(ascending=False)
)

print("\nStrongest relationships with Assembly Waiting Time:")

assembly_corr = correlation["Assembly Waiting Time"].drop(
    "Assembly Waiting Time"
).abs().sort_values(ascending=False)

print(assembly_corr.head(5))
