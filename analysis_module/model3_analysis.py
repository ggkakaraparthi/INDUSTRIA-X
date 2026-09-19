import pandas as pd

FILE = "data/Model_3.csv"

print("=" * 60)
print("        MEMBER 2 - MODEL 3 PRODUCTION ANALYSIS")
print("=" * 60)

# ---------------------------------------------------------
# Columns used for analysis
# ---------------------------------------------------------

utilization_cols = [
    "Blanking_Util",
    "Press1_Util", "Press2_Util", "Press3_Util", "Press4_Util",
    "Cell1_Util", "Cell2_Util", "Cell3_Util", "Cell4_Util",
    "Paint1_Util", "Paint2_Util",
    "Quality_Util",
    "Forklift_Util"
]

queue_cols = [
    "Blanking_SKU1_Queue",
    "Blanking_SKU2_Queue",
    "Blanking_SKU3_Queue",
    "Blanking_SKU4_Queue",
    "Press1_Queue", "Press2_Queue", "Press3_Queue", "Press4_Queue",
    "Cell1_Queue", "Cell2_Queue", "Cell3_Queue", "Cell4_Queue",
    "Warehouse1_Queue", "Warehouse_2_Queue",
    "Warehouse_3_Queue", "Warehouse_4_Queue",
    "Paint1_Queue", "Paint2_Queue",
    "Quality_Queue",
    "Forklift_Blanking_Queue",
    "Forklift_Press_Queue",
    "Forklift_Assembly_Queue",
    "Blanking_Queue"
]

production_cols = [
    "c_TotalProducts"
]

sku_wait_cols = [
    "SKU1_Wait_Time",
    "SKU2_Wait_Time",
    "SKU3_Wait_Time",
    "SKU4_Wait_Time"
]

# ---------------------------------------------------------
# Read required columns only, in chunks
# ---------------------------------------------------------

required_cols = (
    utilization_cols
    + queue_cols
    + production_cols
    + sku_wait_cols
)

sum_values = {col: 0.0 for col in required_cols}
count_values = {col: 0 for col in required_cols}

print("\nReading Model 3 in chunks...")

for chunk in pd.read_csv(
    FILE,
    usecols=required_cols,
    chunksize=100000
):
    for col in required_cols:
        values = pd.to_numeric(chunk[col], errors="coerce")

        sum_values[col] += values.sum()
        count_values[col] += values.count()

print("Model 3 reading completed.")

# ---------------------------------------------------------
# Calculate averages
# ---------------------------------------------------------

averages = {}

for col in required_cols:
    if count_values[col] > 0:
        averages[col] = sum_values[col] / count_values[col]
    else:
        averages[col] = 0

# ---------------------------------------------------------
# 1. UTILIZATION ANALYSIS
# ---------------------------------------------------------

print("\n1. AVERAGE RESOURCE UTILIZATION")
print("-" * 40)

utilization_results = []

for col in utilization_cols:
    utilization_results.append(
        (col, averages[col])
    )

utilization_results.sort(
    key=lambda x: x[1],
    reverse=True
)

for name, value in utilization_results:
    print(f"{name:25s}: {value:.4f}")

# ---------------------------------------------------------
# 2. QUEUE ANALYSIS
# ---------------------------------------------------------

print("\n2. AVERAGE QUEUE LEVEL")
print("-" * 40)

queue_results = []

for col in queue_cols:
    queue_results.append(
        (col, averages[col])
    )

queue_results.sort(
    key=lambda x: x[1],
    reverse=True
)

for name, value in queue_results[:10]:
    print(f"{name:30s}: {value:.4f}")

# ---------------------------------------------------------
# 3. SKU WAITING TIME
# ---------------------------------------------------------

print("\n3. SKU WAITING TIME")
print("-" * 40)

sku_results = []

for col in sku_wait_cols:
    sku_results.append(
        (col, averages[col])
    )

sku_results.sort(
    key=lambda x: x[1],
    reverse=True
)

for name, value in sku_results:
    print(f"{name:25s}: {value:.4f}")

# ---------------------------------------------------------
# 4. TOTAL PRODUCTION
# ---------------------------------------------------------

print("\n4. PRODUCTION")
print("-" * 40)

print(f"Average Total Products: {averages['c_TotalProducts']:.2f}")

# ---------------------------------------------------------
# 5. SIMPLE RESOURCE BOTTLENECK ANALYSIS
# ---------------------------------------------------------

print("\n5. RESOURCE BOTTLENECK ANALYSIS")
print("-" * 40)

resource_data = {
    "Blanking": {
        "util": averages["Blanking_Util"],
        "queue": (
            averages["Blanking_SKU1_Queue"]
            + averages["Blanking_SKU2_Queue"]
            + averages["Blanking_SKU3_Queue"]
            + averages["Blanking_SKU4_Queue"]
        ) / 4
    },

    "Press1": {
        "util": averages["Press1_Util"],
        "queue": averages["Press1_Queue"]
    },

    "Press2": {
        "util": averages["Press2_Util"],
        "queue": averages["Press2_Queue"]
    },

    "Press3": {
        "util": averages["Press3_Util"],
        "queue": averages["Press3_Queue"]
    },

    "Press4": {
        "util": averages["Press4_Util"],
        "queue": averages["Press4_Queue"]
    },

    "Cell1": {
        "util": averages["Cell1_Util"],
        "queue": averages["Cell1_Queue"]
    },

    "Cell2": {
        "util": averages["Cell2_Util"],
        "queue": averages["Cell2_Queue"]
    },

    "Cell3": {
        "util": averages["Cell3_Util"],
        "queue": averages["Cell3_Queue"]
    },

    "Cell4": {
        "util": averages["Cell4_Util"],
        "queue": averages["Cell4_Queue"]
    },

    "Paint1": {
        "util": averages["Paint1_Util"],
        "queue": averages["Paint1_Queue"]
    },

    "Paint2": {
        "util": averages["Paint2_Util"],
        "queue": averages["Paint2_Queue"]
    },

    "Quality": {
        "util": averages["Quality_Util"],
        "queue": averages["Quality_Queue"]
    },

    "Forklift": {
        "util": averages["Forklift_Util"],
        "queue": (
            averages["Forklift_Blanking_Queue"]
            + averages["Forklift_Press_Queue"]
            + averages["Forklift_Assembly_Queue"]
        ) / 3
    }
}

# Normalize utilization
max_util = max(
    item["util"] for item in resource_data.values()
)

# Normalize queue
max_queue = max(
    item["queue"] for item in resource_data.values()
)

for resource, values in resource_data.items():

    util_score = (
        values["util"] / max_util
        if max_util > 0 else 0
    )

    queue_score = (
        values["queue"] / max_queue
        if max_queue > 0 else 0
    )

    values["util_score"] = util_score
    values["queue_score"] = queue_score

    values["bottleneck_score"] = (
        util_score + queue_score
    ) / 2

# Sort resources
bottleneck_results = sorted(
    resource_data.items(),
    key=lambda x: x[1]["bottleneck_score"],
    reverse=True
)

for resource, values in bottleneck_results:
    print(
        f"{resource:12s} | "
        f"Util={values['util']:.4f} | "
        f"Queue={values['queue']:.4f} | "
        f"Score={values['bottleneck_score']:.4f}"
    )

bottleneck = bottleneck_results[0][0]

print("\nDetected Bottleneck:", bottleneck)

# ---------------------------------------------------------
# FINAL SUMMARY
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("                 FINAL SUMMARY")
print("=" * 60)

print(f"Model 3 Bottleneck      : {bottleneck}")
print(
    f"Average Total Products  : "
    f"{averages['c_TotalProducts']:.2f}"
)

highest_sku = sku_results[0]

print(
    f"Highest SKU Waiting Time: "
    f"{highest_sku[0]} = {highest_sku[1]:.4f}"
)

highest_util = utilization_results[0]

print(
    f"Highest Utilization     : "
    f"{highest_util[0]} = {highest_util[1]:.4f}"
)

print("\nModel 3 analysis completed successfully.")