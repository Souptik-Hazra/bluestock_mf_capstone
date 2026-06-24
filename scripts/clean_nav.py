import pandas as pd
from pathlib import Path

df = pd.read_csv("data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(["amfi_code", "date"])

df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .transform(lambda x: x.ffill())
)

df = df.drop_duplicates()

df = df[df["nav"] > 0]

Path("data/processed").mkdir(parents=True, exist_ok=True)

df.to_csv(
    "data/processed/clean_nav.csv",
    index=False
)

print("clean_nav.csv created")
print("Rows:", len(df))