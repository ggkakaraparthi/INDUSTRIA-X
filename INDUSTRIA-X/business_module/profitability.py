import pandas as pd

print("=" * 60)
print("          INDUSTRIA-X BUSINESS IMPACT")
print("=" * 60)

# Results from the three production models
model_results = {
    "Model 1": {
        "bottleneck": "Assembly",
        "production": 209.45
    },
    "Model 2": {
        "bottleneck": "Drilling",
        "production": 6554.37
    },
    "Model 3": {
        "bottleneck": "Forklift",
        "production": 54746.71
    }
}

print("\nPRODUCTION SUMMARY")
print("-" * 40)

for model, data in model_results.items():
    print(f"{model}")
    print(f"  Bottleneck : {data['bottleneck']}")
    print(f"  Production : {data['production']:.2f}")

# ---------------------------------------------------------
# Production exposure estimate
# ---------------------------------------------------------

print("\nBUSINESS IMPACT INDICATORS")
print("-" * 40)

for model, data in model_results.items():

    production = data["production"]

    # Scenario-based exposure indicator.
    # This is NOT monetary profit/loss.
    exposure_5_percent = production * 0.05
    exposure_10_percent = production * 0.10

    print(f"\n{model}")
    print(f"  5% production exposure  : {exposure_5_percent:.2f}")
    print(f"  10% production exposure : {exposure_10_percent:.2f}")

# ---------------------------------------------------------
# Important limitation
# ---------------------------------------------------------

print("\nIMPORTANT")
print("-" * 40)

print(
    "These values are production-impact estimates, "
    "not actual monetary profit or loss."
)

print(
    "Actual profitability requires cost, price, revenue, "
    "or margin information."
)

print("\nBusiness impact analysis completed successfully.")