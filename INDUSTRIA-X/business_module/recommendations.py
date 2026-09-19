import pandas as pd

OUTPUT_DIR = "INDUSTRIA-X/business_module/outputs"

util = pd.read_csv(
    f"{OUTPUT_DIR}/resource_utilization.csv"
)

queues = pd.read_csv(
    f"{OUTPUT_DIR}/queue_analysis.csv"
)

production = pd.read_csv(
    f"{OUTPUT_DIR}/production_summary.csv"
)

sku = pd.read_csv(
    f"{OUTPUT_DIR}/sku_time_analysis.csv"
)

print("========== MODEL 3 KEY FINDINGS ==========")

# Highest utilization
highest_util = util.iloc[0]

print("\n1. Highest resource utilization:")
print(
    f"{highest_util['Resource']}: "
    f"{highest_util['Utilization_Percent']:.2f}%"
)

# Largest queue
largest_queue = queues.iloc[0]

print("\n2. Largest queue:")
print(
    f"{largest_queue['Queue']}: "
    f"{largest_queue['Average_Queue']:.2f}"
)

# Highest SKU total time
highest_sku = sku.loc[sku["Total_Time"].idxmax()]

print("\n3. Highest SKU total time:")
print(
    f"{highest_sku['SKU']}: "
    f"{highest_sku['Total_Time']:.4f}"
)

# Highest SKU waiting time
highest_wait = sku.loc[sku["Wait_Time"].idxmax()]

print("\n4. Highest SKU waiting time:")
print(
    f"{highest_wait['SKU']}: "
    f"{highest_wait['Wait_Time']:.4f}"
)

# Production
avg_production = production.loc[
    production["Metric"] == "Average", "Value"
].iloc[0]

min_production = production.loc[
    production["Metric"] == "Minimum", "Value"
].iloc[0]

max_production = production.loc[
    production["Metric"] == "Maximum", "Value"
].iloc[0]

print("\n5. Production:")
print(f"Average: {avg_production:.2f}")
print(f"Minimum: {min_production:.2f}")
print(f"Maximum: {max_production:.2f}")

print("\n========== END ==========")