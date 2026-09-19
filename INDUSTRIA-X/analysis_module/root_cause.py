import pandas as pd
import os


# ============================================================
# MODEL 3 ROOT CAUSE ANALYSIS
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

UTIL_CORR_FILE = os.path.join(
    OUTPUT_DIR,
    "utilization_production_correlation.csv"
)

QUEUE_CORR_FILE = os.path.join(
    OUTPUT_DIR,
    "queue_production_correlation.csv"
)


print()
print("=======================================================")
print("             INDUSTRIA-X ROOT CAUSE ANALYSIS")
print("=======================================================")


# ============================================================
# 1. RESOURCE UTILIZATION
# ============================================================

print("\n1. RESOURCE UTILIZATION")

try:
    resource = pd.read_csv(RESOURCE_FILE)

    print("Resource utilization file loaded successfully.")
    print("Columns:", resource.columns.tolist())

    # Find resource name column
    resource_name_col = None

    for col in resource.columns:
        if col.lower() in [
            "resource",
            "variable",
            "resource_name"
        ]:
            resource_name_col = col
            break

    # Find utilization column
    utilization_col = None

    for col in resource.columns:
        col_lower = col.lower()

        if (
            "utilization" in col_lower
            or "util" in col_lower
            or "average" in col_lower
        ):
            if col != resource_name_col:
                utilization_col = col
                break

    if resource_name_col is not None and utilization_col is not None:

        resource[utilization_col] = pd.to_numeric(
            resource[utilization_col],
            errors="coerce"
        )

        resource = resource.dropna(
            subset=[utilization_col]
        )

        highest_resource = resource.loc[
            resource[utilization_col].idxmax()
        ]

        print(
            f"Highest utilization resource: "
            f"{highest_resource[resource_name_col]}"
        )

        print(
            f"Utilization: "
            f"{highest_resource[utilization_col]:.4f}"
        )

    else:
        print("Could not automatically identify utilization columns.")
        print("Available columns:", resource.columns.tolist())

except Exception as e:
    print("Resource utilization analysis failed.")
    print("Error:", e)


# ============================================================
# 2. QUEUE ANALYSIS
# ============================================================

print("\n2. QUEUE ANALYSIS")

try:
    queue = pd.read_csv(QUEUE_FILE)

    print("Queue analysis file loaded successfully.")
    print("Columns:", queue.columns.tolist())

    queue_name_col = None
    queue_value_col = None

    for col in queue.columns:
        col_lower = col.lower()

        if col_lower in [
            "queue",
            "variable",
            "resource",
            "queue_name"
        ]:
            queue_name_col = col
            break

    for col in queue.columns:
        if col != queue_name_col:
            if (
                "average" in col.lower()
                or "queue" in col.lower()
                or "value" in col.lower()
            ):
                queue_value_col = col
                break

    if queue_name_col is not None and queue_value_col is not None:

        queue[queue_value_col] = pd.to_numeric(
            queue[queue_value_col],
            errors="coerce"
        )

        queue = queue.dropna(
            subset=[queue_value_col]
        )

        largest_queue = queue.loc[
            queue[queue_value_col].idxmax()
        ]

        print(
            f"Largest queue: "
            f"{largest_queue[queue_name_col]}"
        )

        print(
            f"Average queue: "
            f"{largest_queue[queue_value_col]:.4f}"
        )

    else:
        print("Could not automatically identify queue columns.")
        print("Available columns:", queue.columns.tolist())

except Exception as e:
    print("Queue analysis failed.")
    print("Error:", e)


# ============================================================
# 3. UTILIZATION VS PRODUCTION
# ============================================================

print("\n3. UTILIZATION vs PRODUCTION")

try:
    util_corr = pd.read_csv(UTIL_CORR_FILE)

    print("Utilization correlation file loaded successfully.")

    print(
        "Columns:",
        util_corr.columns.tolist()
    )

    correlation_col = "Correlation_With_Production"

    if correlation_col in util_corr.columns:

        valid_util = util_corr.dropna(
            subset=[correlation_col]
        )

        if not valid_util.empty:

            strongest_util = valid_util.loc[
                valid_util[correlation_col].abs().idxmax()
            ]

            print(
                f"Strongest relationship: "
                f"{strongest_util['Variable']}"
            )

            print(
                f"Correlation: "
                f"{strongest_util[correlation_col]:.4f}"
            )

    else:
        print(
            f"Column '{correlation_col}' "
            "was not found."
        )

except Exception as e:
    print("Utilization-production analysis failed.")
    print("Error:", e)


# ============================================================
# 4. QUEUE VS PRODUCTION
# ============================================================

print("\n4. QUEUE vs PRODUCTION")

try:
    queue_corr = pd.read_csv(QUEUE_CORR_FILE)

    print("Queue correlation file loaded successfully.")

    print(
        "Columns:",
        queue_corr.columns.tolist()
    )

    correlation_col = "Correlation_With_Production"

    if correlation_col in queue_corr.columns:

        valid_queue = queue_corr.dropna(
            subset=[correlation_col]
        )

        if not valid_queue.empty:

            strongest_queue = valid_queue.loc[
                valid_queue[correlation_col].abs().idxmax()
            ]

            print(
                f"Strongest relationship: "
                f"{strongest_queue['Variable']}"
            )

            print(
                f"Correlation: "
                f"{strongest_queue[correlation_col]:.4f}"
            )

    else:
        print(
            f"Column '{correlation_col}' "
            "was not found."
        )

except Exception as e:
    print("Queue-production analysis failed.")
    print("Error:", e)


# ============================================================
# 5. ROOT CAUSE SUMMARY
# ============================================================

print("\n5. ROOT CAUSE SUMMARY")

print(
    "The analysis combines resource utilization, "
    "queue size, and production correlation."
)

print(
    "High utilization indicates resources that may "
    "require closer monitoring."
)

print(
    "Large queues indicate possible waiting or "
    "material accumulation points."
)

print(
    "Strong correlations identify variables that "
    "move closely with production in Model 3."
)


print()
print("=======================================================")
print("              END ROOT CAUSE ANALYSIS")
print("=======================================================")