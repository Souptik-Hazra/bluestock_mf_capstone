from pathlib import Path
import pandas as pd

raw_path = Path("data/raw")

for file in raw_path.glob("*.csv"):
    print("=" * 60)
    print(f"Dataset: {file.name}")

    try:
        df = pd.read_csv(file)

        print("Shape:", df.shape)

        print("\nDtypes:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:", df.isnull().sum().sum())
        print("Duplicate Rows:", df.duplicated().sum())

    except Exception as e:
        print("Error:", e)