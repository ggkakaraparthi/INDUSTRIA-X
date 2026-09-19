import os
import pandas as pd


# ============================================================
# INDUSTRIA-X
# MODEL 3 DEFECT / ANOMALY DETECTION
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "business_module",
    "outputs"
)

RESOURCE_FILE = os.path.join(
    OUTPUT_DIR,
    "resource_utilization.csv"
)

QUEUE_FILE = os.path.join(
    OUTPUT_DIR,
    "queue_analysis.csv"
)

SKU_FILE = os.path.join(
    OUTPUT_DIR,
    "sku_time_analysis.csv"
)


print()
print("=======================================================")
print("        INDUSTRIA-X DEFECT / ANOMALY DETECTION")
print("=======================================================")


# ============================================================
# LOAD RESOURCE DATA
# ============================================================

print("\nLoading resource utilization data...")

try:
    resource = pd.read_csv(RESOURCE_FILE)
    print("Resource data loaded successfully.")
except Exception as e:
    print("Could not load resource data.")
    print("Error:", e)
    raise SystemExit


# ============================================================
# RESOURCE ANOMALY DETECTION
# ============================================================

print("\n1. RESOURCE ANOMALIES")

resource_name_col = "Resource"
utilization_col = "Average_Utilization"

if (
    resource_name_col in resource.columns
    and utilization_col in resource.columns
):

    resource[utilization_col] = pd.to_numeric(
        resource[utilization_col],
        errors="coerce"
    )

    high_utilization = resource[
        resource[utilization_col] >= 0.80
    ].copy()

    if not high_utilization.empty:

        print(
            f"Resources with utilization >= 80%: "
            f"{len(high_utilization)}"
        )

        for _, row in high_utilization.iterrows():

            print(
                f"- {row[resource_name_col]}: "
                f"{row[utilization_col]:.2%}"
            )

    else:
        print("No resources exceeded the 80% threshold.")

else:
    print("Expected resource columns were not found.")


# ============================================================
# LOAD QUEUE DATA
# ============================================================

print("\nLoading queue data...")

try:
    queue = pd.read_csv(QUEUE_FILE)
    print("Queue data loaded successfully.")
except Exception as e:
    print("Could not load queue data.")
    print("Error:", e)
    raise SystemExit


# ============================================================
# QUEUE ANOMALY DETECTION
# ============================================================

print("\n2. QUEUE ANOMALIES")

if (
    "Queue" in queue.columns
    and "Average_Queue" in queue.columns
):

    queue["Average_Queue"] = pd.to_numeric(
        queue["Average_Queue"],
        errors="coerce"
    )

    # Statistical threshold:
    # mean + standard deviation
    queue_mean = queue["Average_Queue"].mean()
    queue_std = queue["Average_Queue"].std()

    queue_threshold = queue_mean + queue_std

    abnormal_queues = queue[
        queue["Average_Queue"] > queue_threshold
    ].copy()

    print(
        f"Average queue level: "
        f"{queue_mean:.2f}"
    )

    print(
        f"Anomaly threshold: "
        f"{queue_threshold:.2f}"
    )

    if not abnormal_queues.empty:

        print(
            f"Queues above anomaly threshold: "
            f"{len(abnormal_queues)}"
        )

        for _, row in abnormal_queues.iterrows():

            print(
                f"- {row['Queue']}: "
                f"{row['Average_Queue']:.2f}"
            )

    else:
        print(
            "No queues exceeded the statistical "
            "anomaly threshold."
        )

else:
    print("Expected queue columns were not found.")


# ============================================================
# LOAD SKU DATA
# ============================================================

print("\nLoading SKU time data...")

try:
    sku = pd.read_csv(SKU_FILE)
    print("SKU data loaded successfully.")
except Exception as e:
    print("Could not load SKU data.")
    print("Error:", e)
    raise SystemExit


# ============================================================
# SKU ANOMALY DETECTION
# ============================================================

print("\n3. SKU TIME ANOMALIES")

if (
    "SKU" in sku.columns
    and "Wait_Time" in sku.columns
    and "Total_Time" in sku.columns
):

    sku["Wait_Time"] = pd.to_numeric(
        sku["Wait_Time"],
        errors="coerce"
    )

    sku["Total_Time"] = pd.to_numeric(
        sku["Total_Time"],
        errors="coerce"
    )

    average_wait = sku["Wait_Time"].mean()
    average_total = sku["Total_Time"].mean()

    high_wait = sku[
        sku["Wait_Time"] > average_wait
    ]

    high_total = sku[
        sku["Total_Time"] > average_total
    ]

    print(
        f"Average SKU waiting time: "
        f"{average_wait:.4f}"
    )

    print(
        f"Average SKU total time: "
        f"{average_total:.4f}"
    )

    print("\nSKUs above average waiting time:")

    if not high_wait.empty:

        for _, row in high_wait.iterrows():

            print(
                f"- {row['SKU']}: "
                f"{row['Wait_Time']:.4f}"
            )

    else:
        print("None")

    print("\nSKUs above average total time:")

    if not high_total.empty:

        for _, row in high_total.iterrows():

            print(
                f"- {row['SKU']}: "
                f"{row['Total_Time']:.4f}"
            )

    else:
        print("None")

else:
    print("Expected SKU columns were not found.")


# ============================================================
# OVERALL SUMMARY
# ============================================================

print("\n=======================================================")
print("                 ANOMALY SUMMARY")
print("=======================================================")

print(
    "\nThis module identifies potential operational "
    "anomalies using the Model 3 analysis outputs."
)

print(
    "\nDetection criteria:"
)

print(
    "1. Resource utilization >= 80%"
)

print(
    "2. Queue greater than mean + standard deviation"
)

print(
    "3. SKU waiting time above average"
)

print(
    "4. SKU total time above average"
)

print(
    "\nThese indicators identify areas for investigation. "
    "They do not by themselves establish a confirmed defect "
    "or causal relationship."
)


print("\n=======================================================")
print("       END DEFECT / ANOMALY DETECTION")
print("=======================================================")