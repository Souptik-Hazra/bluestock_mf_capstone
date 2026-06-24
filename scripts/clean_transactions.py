import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

df["transaction_type"] = (
    df["transaction_type"]
      .astype(str)
      .str.strip()
)

valid_types = [
    "SIP",
    "Lumpsum",
    "Redemption"
]

df = df[
    df["transaction_type"].isin(valid_types)
]

df = df[df["amount_inr"] > 0]

valid_kyc = [
    "Verified",
    "Pending"
]

df = df[
    df["kyc_status"].isin(valid_kyc)
]

df = df.drop_duplicates()

df.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)

print("clean_transactions.csv created")
print("Rows:", len(df))