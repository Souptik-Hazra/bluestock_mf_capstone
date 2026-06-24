import pandas as pd
from pathlib import Path

file_path = Path("data/raw/01_fund_master.csv")

df = pd.read_csv(file_path)

print("=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

print("\nTotal Schemes:", len(df))

print("\nUnique Fund Houses:")
print(df["fund_house"].nunique())
print(sorted(df["fund_house"].unique()))

print("\nUnique Categories:")
print(df["category"].nunique())
print(sorted(df["category"].unique()))

print("\nUnique Sub-Categories:")
print(df["sub_category"].nunique())
print(sorted(df["sub_category"].unique()))

print("\nUnique Risk Grades:")
print(df["risk_category"].nunique())
print(sorted(df["risk_category"].unique()))

print("\nFund House Distribution:")
print(df["fund_house"].value_counts())

print("\nCategory Distribution:")
print(df["category"].value_counts())

print("\nRisk Grade Distribution:")
print(df["risk_category"].value_counts())

print("\nAnalysis Complete")