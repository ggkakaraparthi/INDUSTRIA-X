import pandas as pd
import os

# ============================================================
# MODEL 3 RECOMMENDATIONS
# ============================================================

OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__),
    "outputs"
)

# ------------------------------------------------------------
# LOAD OUTPUT FILES
# ------------------------------------------------------------

resource = pd.read_csv(
    os.path.join(
        OUTPUT_DIR,
        "resource_utilization.csv"
    )
)

queue = pd.read_csv(
    os.path.join(
        OUTPUT_DIR,
        "queue_analysis.csv"
    )
)

production = pd.read_csv(
    os.path.join(
        OUTPUT_DIR,
        "production_summary.csv"
    )
)

sku = pd.read_csv(
    os.path.join(
        OUTPUT_DIR,
        "sku_time_analysis.csv"
    )
)

util_corr = pd.read_csv(
    os.path.join(
        OUTPUT_DIR,
        "utilization_production_correlation.csv"
    )
)

queue_corr = pd.read_csv(
    os.path.join(
        OUTPUT_DIR,
        "queue_production_correlation.csv"
    )
)


print("\n========== MODEL 3 RECOMMENDATIONS ==========\n")


# ============================================================
# 1. RESOURCE UTILIZATION
# ============================================================

highest_resource = resource.loc[
    resource["Average_Utilization"].idxmax()
]

print("1. RESOURCE UTILIZATION")

print(
    f"Highest utilization resource: "
    f"{highest_resource['Resource']}"
)

print(
    f"Utilization: "
    f"{highest_resource['Average_Utilization']:.2%}"
)

if highest_resource["Average_Utilization"] > 0.80:

    print(
        "Recommendation: Monitor this resource closely "
        "because utilization is above 80%."
    )

else:

    print(
        "Recommendation: Utilization is below 80%; "
        "continue monitoring resource performance."
    )


# ============================================================
# 2. QUEUE ANALYSIS
# ============================================================

largest_queue = queue.loc[
    queue["Average_Queue"].idxmax()
]

print("\n2. QUEUE ANALYSIS")

print(
    f"Largest queue: "
    f"{largest_queue['Queue']}"
)

print(
    f"Average queue: "
    f"{largest_queue['Average_Queue']:.2f}"
)

print(
    "Recommendation: Investigate the process feeding "
    "this queue and identify opportunities to reduce "
    "waiting and material accumulation."
)


# ============================================================
# 3. SKU ANALYSIS
# ============================================================

highest_wait = sku.loc[
    sku["Wait_Time"].idxmax()
]

highest_total = sku.loc[
    sku["Total_Time"].idxmax()
]

print("\n3. SKU ANALYSIS")

print(
    f"Highest waiting-time SKU: "
    f"{highest_wait['SKU']}"
)

print(
    f"Waiting time: "
    f"{highest_wait['Wait_Time']:.4f}"
)

print(
    f"Highest total-time SKU: "
    f"{highest_total['SKU']}"
)

print(
    f"Total time: "
    f"{highest_total['Total_Time']:.4f}"
)

print(
    "Recommendation: Investigate the flow and waiting "
    "conditions affecting the highest-time SKU."
)


# ============================================================
# 4. PRODUCTION
# ============================================================

print("\n4. PRODUCTION")

for _, row in production.iterrows():

    print(
        f"{row['Metric']}: "
        f"{row['Value']:.2f}"
    )


# ============================================================
# 5. UTILIZATION vs PRODUCTION
# ============================================================

print("\n5. UTILIZATION vs PRODUCTION")

valid_util = util_corr.dropna(
    subset=["Correlation_With_Production"]
)

if not valid_util.empty:

    strongest_util = valid_util.loc[
        valid_util["Abs_Correlation"].idxmax()
    ]

    print(
        f"Strongest relationship: "
        f"{strongest_util['Variable']}"
    )

    print(
        f"Correlation: "
        f"{strongest_util['Correlation_With_Production']:.4f}"
    )

else:

    print(
        "No valid utilization-production "
        "correlation values available."
    )


# ============================================================
# 6. QUEUE vs PRODUCTION
# ============================================================

print("\n6. QUEUE vs PRODUCTION")

valid_queue = queue_corr.dropna(
    subset=["Correlation_With_Production"]
)

if not valid_queue.empty:

    strongest_queue = valid_queue.loc[
        valid_queue["Abs_Correlation"].idxmax()
    ]

    print(
        f"Strongest relationship: "
        f"{strongest_queue['Variable']}"
    )

    print(
        f"Correlation: "
        f"{strongest_queue['Correlation_With_Production']:.4f}"
    )

else:

    print(
        "No valid queue-production "
        "correlation values available."
    )


# ============================================================
# END
# ============================================================

print(
    "\n========== END ==========\n"
)