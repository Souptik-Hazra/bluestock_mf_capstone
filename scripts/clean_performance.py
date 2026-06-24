import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

print("\nNegative Sharpe Ratio Funds")
print(
    df[df["sharpe_ratio"] < 0][
        ["scheme_name", "sharpe_ratio"]
    ]
)

print("\nExpense Ratio Anomalies")
print(
    df[
        (df["expense_ratio_pct"] < 0.1)
        |
        (df["expense_ratio_pct"] > 2.5)
    ]
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)

print("\nclean_performance.csv created")
print("Rows:", len(df))