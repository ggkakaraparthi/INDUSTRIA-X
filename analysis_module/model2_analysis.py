import pandas as pd

df = pd.read_csv("data/Model_2.csv")

print("\n--- MODEL 2 RELATIONSHIP ANALYSIS ---")

columns = [
    "Demand",
    "Entities In Part 1",
    "Part 1 VA Time",
    "Drilling Queue Time",
    "Part 1 Storage Time",
    "Part 1 Stored",
    "Entities In Part 2",
    "Part 2 VA Time",
    "Milling Queue Time",
    "Part 2 Storage Time",
    "Part 2 Stored",
    "Entities Out",
    "Assembly Time",
    "Assembly Queue Time",
    "Drilling Utilization",
    "Milling Utilization",
    "Assembly Utilization"
]

correlation = df[columns].corr()

print("\nCorrelation with Entities Out:")
print(
    correlation["Entities Out"]
    .sort_values(ascending=False)
)

print("\nCorrelation with Drilling Queue Time:")
print(
    correlation["Drilling Queue Time"]
    .sort_values(ascending=False)
)

print("\nStrongest relationships with Entities Out:")

out_corr = correlation["Entities Out"].drop(
    "Entities Out"
).abs().sort_values(ascending=False)

print(out_corr.head(5))
