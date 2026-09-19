import pandas as pd

print("\n======================================")
print("      MEMBER 1 PRODUCTION ANALYSIS")
print("======================================")

# ==================================================
# MODEL 1
# ==================================================

df1 = pd.read_csv("data/Model_1.csv")
df1 = df1.dropna(axis=1, how="all")

# Model 1 bottleneck
waiting1 = df1[[
    "Drilling Waiting Time",
    "Milling Waiting Time",
    "Assembly Waiting Time"
]].mean()

util1 = df1[[
    "Drilling Util",
    "Milling Util",
    "Assembly Util"
]].mean()

result1 = pd.DataFrame({
    "Waiting_Time": [
        waiting1["Drilling Waiting Time"],
        waiting1["Milling Waiting Time"],
        waiting1["Assembly Waiting Time"]
    ],
    "Utilization": [
        util1["Drilling Util"],
        util1["Milling Util"],
        util1["Assembly Util"]
    ]
}, index=["Drilling", "Milling", "Assembly"])

result1["Waiting_Score"] = (
    result1["Waiting_Time"] / result1["Waiting_Time"].max()
)

result1["Utilization_Score"] = (
    result1["Utilization"] / result1["Utilization"].max()
)

result1["Bottleneck_Score"] = (
    result1["Waiting_Score"] +
    result1["Utilization_Score"]
) / 2

bottleneck1 = result1["Bottleneck_Score"].idxmax()

print("\n--- MODEL 1 ---")
print("Detected Bottleneck:", bottleneck1)
print("Average Throughput:",
      df1["Parts per hour"].mean())
print("Minimum Throughput:",
      df1["Parts per hour"].min())
print("Maximum Throughput:",
      df1["Parts per hour"].max())


# ==================================================
# MODEL 2
# ==================================================

df2 = pd.read_csv("data/Model_2.csv")

queue2 = df2[[
    "Drilling Queue Time",
    "Milling Queue Time",
    "Assembly Queue Time"
]].mean()

util2 = df2[[
    "Drilling Utilization",
    "Milling Utilization",
    "Assembly Utilization"
]].mean()

result2 = pd.DataFrame({
    "Queue_Time": [
        queue2["Drilling Queue Time"],
        queue2["Milling Queue Time"],
        queue2["Assembly Queue Time"]
    ],
    "Utilization": [
        util2["Drilling Utilization"],
        util2["Milling Utilization"],
        util2["Assembly Utilization"]
    ]
}, index=["Drilling", "Milling", "Assembly"])

result2["Queue_Score"] = (
    result2["Queue_Time"] / result2["Queue_Time"].max()
)

result2["Utilization_Score"] = (
    result2["Utilization"] / result2["Utilization"].max()
)

result2["Bottleneck_Score"] = (
    result2["Queue_Score"] +
    result2["Utilization_Score"]
) / 2

bottleneck2 = result2["Bottleneck_Score"].idxmax()

print("\n--- MODEL 2 ---")
print("Detected Bottleneck:", bottleneck2)
print("Average Entities Out:",
      df2["Entities Out"].mean())
print("Minimum Entities Out:",
      df2["Entities Out"].min())
print("Maximum Entities Out:",
      df2["Entities Out"].max())


# ==================================================
# FINAL SUMMARY
# ==================================================

print("\n======================================")
print("             FINAL SUMMARY")
print("======================================")

print("Model 1 Bottleneck:", bottleneck1)
print("Model 2 Bottleneck:", bottleneck2)

print("\nMember 1 analysis completed successfully.")
