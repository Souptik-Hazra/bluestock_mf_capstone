import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"

# --------------------------------------------------
# Load Data
# --------------------------------------------------

performance = pd.read_csv(
    DATA_PROCESSED / "clean_performance.csv"
)

# --------------------------------------------------
# User Input
# --------------------------------------------------

print("=" * 50)
print(" Mutual Fund Recommendation System ")
print("=" * 50)

print("\nRisk Appetite Options:")
print("1. Low")
print("2. Moderate")
print("3. High")
print("4. Very High")

risk = input("\nEnter Risk Appetite: ").strip().title()

# --------------------------------------------------
# Filter Funds
# --------------------------------------------------

filtered = performance[
    performance["risk_grade"].str.title() == risk
]

if filtered.empty:
    print("\nNo funds found for the selected risk grade.")
    exit()

# --------------------------------------------------
# Recommend Top 3 Funds
# --------------------------------------------------

recommended = (
    filtered
    .sort_values(
        by="sharpe_ratio",
        ascending=False
    )
    .head(3)
)

# --------------------------------------------------
# Display Recommendations
# --------------------------------------------------

print("\nTop 3 Recommended Mutual Funds\n")

for i, (_, row) in enumerate(recommended.iterrows(), start=1):

    print(f"{i}. {row['scheme_name']}")

    print(f"   Fund House : {row['fund_house']}")
    print(f"   Category   : {row['category']}")
    print(f"   Sharpe     : {row['sharpe_ratio']:.2f}")
    print(f"   Return 3Y  : {row['return_3yr_pct']:.2f}%")
    print(f"   Risk Grade : {row['risk_grade']}")
    print()