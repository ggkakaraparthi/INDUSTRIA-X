import os
import pandas as pd


# ============================================================
# INDUSTRIA-X
# MODEL 3 ANOMALY LOCALIZATION
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
print("          INDUSTRIA-X ANOMALY LOCALIZATION")
print("=======================================================")


# ============================================================
# RESOURCE LOCALIZATION
# ============================================================

print("\n1. RESOURCE ANOMALY LOCALIZATION")

try:

    resource = pd.read_csv(RESOURCE_FILE)

    resource["Average_Utilization"] = pd.to_numeric(
        resource["Average_Utilization"],
        errors="coerce"
    )

    high_resources = resource[
        resource["Average_Utilization"] >= 0.80
    ].copy()

    if not high_resources.empty:

        print("\nHigh-utilization process areas:")

        for _, row in high_resources.iterrows():

            resource_name = row["Resource"]

            if "Blanking" in resource_name:
                area = "Blanking"

            elif "Cell" in resource_name:
                area = "Assembly / Cell"

            elif "Press" in resource_name:
                area = "Press"

            elif "Paint" in resource_name:
                area = "Painting"

            elif "Quality" in resource_name:
                area = "Quality"

            elif "Forklift" in resource_name:
                area = "Material Handling"

            else:
                area = "Other"

            print(
                f"- {resource_name}"
                f" -> Process Area: {area}"
                f" -> Utilization: "
                f"{row['Average_Utilization']:.2%}"
            )

    else:

        print(
            "No high-utilization resource anomalies found."
        )

except Exception as e:

    print("Resource localization failed.")
    print("Error:", e)


# ============================================================
# QUEUE LOCALIZATION
# ============================================================

print("\n2. QUEUE ANOMALY LOCALIZATION")

try:

    queue = pd.read_csv(QUEUE_FILE)

    queue["Average_Queue"] = pd.to_numeric(
        queue["Average_Queue"],
        errors="coerce"
    )

    mean_queue = queue["Average_Queue"].mean()
    std_queue = queue["Average_Queue"].std()

    threshold = mean_queue + std_queue

    abnormal_queues = queue[
        queue["Average_Queue"] > threshold
    ].copy()

    if not abnormal_queues.empty:

        print("\nAbnormal queue locations:")

        for _, row in abnormal_queues.iterrows():

            queue_name = row["Queue"]

            if "Warehouse" in queue_name:
                area = "Warehouse"

            elif "Forklift_Blanking" in queue_name:
                area = "Material Handling - Blanking"

            elif "Forklift_Press" in queue_name:
                area = "Material Handling - Press"

            elif "Forklift_Assembly" in queue_name:
                area = "Material Handling - Assembly"

            elif "Press" in queue_name:
                area = "Press"

            elif "Blanking" in queue_name:
                area = "Blanking"

            elif "Quality" in queue_name:
                area = "Quality"

            elif "Paint" in queue_name:
                area = "Painting"

            elif "Cell" in queue_name:
                area = "Assembly / Cell"

            else:
                area = "Other"

            print(
                f"- {queue_name}"
                f" -> Process Area: {area}"
                f" -> Queue: "
                f"{row['Average_Queue']:.2f}"
            )

    else:

        print(
            "No abnormal queue locations found."
        )

except Exception as e:

    print("Queue localization failed.")
    print("Error:", e)


# ============================================================
# SKU LOCALIZATION
# ============================================================

print("\n3. SKU ANOMALY LOCALIZATION")

try:

    sku = pd.read_csv(SKU_FILE)

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

    abnormal_skus = sku[
        (sku["Wait_Time"] > average_wait)
        |
        (sku["Total_Time"] > average_total)
    ].copy()

    if not abnormal_skus.empty:

        print("\nSKUs requiring investigation:")

        for _, row in abnormal_skus.iterrows():

            print(
                f"- {row['SKU']}"
                f" -> Waiting Time: "
                f"{row['Wait_Time']:.4f}"
                f" -> Total Time: "
                f"{row['Total_Time']:.4f}"
            )

    else:

        print(
            "No SKU time anomalies found."
        )

except Exception as e:

    print("SKU localization failed.")
    print("Error:", e)


# ============================================================
# LOCALIZATION SUMMARY
# ============================================================

print("\n=======================================================")
print("              LOCALIZATION SUMMARY")
print("=======================================================")

print(
    "\nThe localization module maps detected anomalies "
    "to their corresponding production process areas."
)

print(
    "\nAreas considered:"
)

print("- Blanking")
print("- Press")
print("- Assembly / Cell")
print("- Warehouse")
print("- Painting")
print("- Quality")
print("- Material Handling")


print("\n=======================================================")
print("         END ANOMALY LOCALIZATION")
print("=======================================================")