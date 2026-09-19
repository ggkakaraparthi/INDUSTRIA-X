import pandas as pd
from pathlib import Path

# ==========================================
# PATHS
# ==========================================

DATA_PATH = "INDUSTRIA-X/data/Model_3.csv"
OUTPUT_DIR = Path("INDUSTRIA-X/business_module/outputs")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(DATA_PATH)

print("========== DATASET ==========")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# ==========================================
# RESOURCE UTILIZATION
# ==========================================

util_cols = [
    "Blanking_Util",
    "Press1_Util",
    "Press2_Util",
    "Press3_Util",
    "Press4_Util",
    "Cell1_Util",
    "Cell2_Util",
    "Cell3_Util",
    "Cell4_Util",
    "Paint1_Util",
    "Paint2_Util",
    "Quality_Util",
    "Forklift_Util"
]

utilization = df[util_cols].mean().sort_values(ascending=False)

utilization_report = pd.DataFrame({
    "Resource": utilization.index,
    "Average_Utilization": utilization.values,
    "Utilization_Percent": utilization.values * 100
})

print("\n========== RESOURCE UTILIZATION ==========")
print(utilization_report.to_string(index=False))


# ==========================================
# QUEUES
# ==========================================

queue_cols = [
    "Blanking_Queue",
    "Press1_Queue",
    "Press2_Queue",
    "Press3_Queue",
    "Press4_Queue",
    "Cell1_Queue",
    "Cell2_Queue",
    "Cell3_Queue",
    "Cell4_Queue",
    "Warehouse1_Queue",
    "Warehouse_2_Queue",
    "Warehouse_3_Queue",
    "Warehouse_4_Queue",
    "Paint1_Queue",
    "Paint2_Queue",
    "Quality_Queue",
    "Forklift_Blanking_Queue",
    "Forklift_Press_Queue",
    "Forklift_Assembly_Queue"
]

queue_means = df[queue_cols].mean().sort_values(ascending=False)

queue_report = pd.DataFrame({
    "Queue": queue_means.index,
    "Average_Queue": queue_means.values
})

print("\n========== QUEUE ANALYSIS ==========")
print(queue_report.to_string(index=False))


# ==========================================
# PRODUCTION
# ==========================================

production = df["c_TotalProducts"]

production_report = pd.DataFrame({
    "Metric": [
        "Average",
        "Minimum",
        "Maximum"
    ],
    "Value": [
        production.mean(),
        production.min(),
        production.max()
    ]
})

print("\n========== PRODUCTION ==========")
print(production_report.to_string(index=False))


# ==========================================
# CORRELATION WITH PRODUCTION
# ==========================================

util_corr = []

for col in util_cols:
    corr = df[col].corr(production)

    util_corr.append({
        "Variable": col,
        "Correlation_With_Production": corr
    })

util_corr_df = pd.DataFrame(util_corr)
util_corr_df["Abs_Correlation"] = (
    util_corr_df["Correlation_With_Production"].abs()
)

util_corr_df = util_corr_df.sort_values(
    "Abs_Correlation",
    ascending=False
)

print("\n========== UTILIZATION / PRODUCTION CORRELATION ==========")
print(util_corr_df.to_string(index=False))


queue_corr = []

for col in queue_cols:

    # Avoid correlation calculation when there is no variation
    if df[col].nunique(dropna=True) <= 1:
        corr = float("nan")
    else:
        corr = df[col].corr(production)

    queue_corr.append({
        "Variable": col,
        "Correlation_With_Production": corr
    })

queue_corr_df = pd.DataFrame(queue_corr)

queue_corr_df["Abs_Correlation"] = (
    queue_corr_df["Correlation_With_Production"].abs()
)

queue_corr_df = queue_corr_df.sort_values(
    "Abs_Correlation",
    ascending=False
)

print("\n========== QUEUE / PRODUCTION CORRELATION ==========")
print(queue_corr_df.to_string(index=False))


# ==========================================
# SKU ANALYSIS
# ==========================================

sku_rows = []

for sku in range(1, 5):

    va = df[f"SKU{sku}_VA_Time"].mean()
    nva = df[f"SKU{sku}_NVA_Time"].mean()
    transport = df[f"SKU{sku}_Transport_Time"].mean()
    wait = df[f"SKU{sku}_Wait_Time"].mean()
    other = df[f"SKU{sku}_Other_Time"].mean()

    total = va + nva + transport + wait + other

    sku_rows.append({
        "SKU": f"SKU{sku}",
        "VA_Time": va,
        "NVA_Time": nva,
        "Transport_Time": transport,
        "Wait_Time": wait,
        "Other_Time": other,
        "Total_Time": total
    })

sku_report = pd.DataFrame(sku_rows)

print("\n========== SKU TIME ANALYSIS ==========")
print(sku_report.to_string(index=False))


# ==========================================
# SAVE REPORTS
# ==========================================

utilization_report.to_csv(
    OUTPUT_DIR / "resource_utilization.csv",
    index=False
)

queue_report.to_csv(
    OUTPUT_DIR / "queue_analysis.csv",
    index=False
)

production_report.to_csv(
    OUTPUT_DIR / "production_summary.csv",
    index=False
)

util_corr_df.to_csv(
    OUTPUT_DIR / "utilization_production_correlation.csv",
    index=False
)

queue_corr_df.to_csv(
    OUTPUT_DIR / "queue_production_correlation.csv",
    index=False
)

sku_report.to_csv(
    OUTPUT_DIR / "sku_time_analysis.csv",
    index=False
)


print("\n========== REPORTS CREATED ==========")

print("resource_utilization.csv")
print("queue_analysis.csv")
print("production_summary.csv")
print("utilization_production_correlation.csv")
print("queue_production_correlation.csv")
print("sku_time_analysis.csv")

print("\nOutput folder:")
print(OUTPUT_DIR)