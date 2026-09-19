import pandas as pd


def analyze_model1():
    print("\n" + "=" * 60)
    print("MODEL 1 - ROOT CAUSE / RELATIONSHIP ANALYSIS")
    print("=" * 60)

    df = pd.read_csv("data/Model_1.csv")
    df = df.dropna(axis=1, how="all")

    columns = [
        "Demand",
        "Total parts",
        "Parts per hour",
        "VA Time",
        "Drilling Waiting Time",
        "Milling Waiting Time",
        "Assembly Waiting Time",
        "Drilling Util",
        "Milling Util",
        "Assembly Util"
    ]

    correlation = df[columns].corr()

    print("\nTop relationships with Assembly Waiting Time:")

    result = (
        correlation["Assembly Waiting Time"]
        .drop("Assembly Waiting Time")
        .abs()
        .sort_values(ascending=False)
    )

    print(result.head(5))


def analyze_model2():
    print("\n" + "=" * 60)
    print("MODEL 2 - ROOT CAUSE / RELATIONSHIP ANALYSIS")
    print("=" * 60)

    df = pd.read_csv("data/Model_2.csv")

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

    print("\nTop relationships with Entities Out:")

    result = (
        correlation["Entities Out"]
        .drop("Entities Out")
        .abs()
        .sort_values(ascending=False)
    )

    print(result.head(5))

    print("\nTop relationships with Drilling Queue Time:")

    result = (
        correlation["Drilling Queue Time"]
        .drop("Drilling Queue Time")
        .abs()
        .sort_values(ascending=False)
    )

    print(result.head(5))


if __name__ == "__main__":

    analyze_model1()
    analyze_model2()

    print("\n" + "=" * 60)
    print("Root-cause relationship analysis completed.")
    print("=" * 60)
    print(
        "Note: Correlation indicates statistical relationship, "
        "not proven causation."
    )