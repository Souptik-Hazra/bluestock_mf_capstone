import requests
import pandas as pd
from pathlib import Path

codes = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

out = Path("data/raw/nav_api")
out.mkdir(parents=True, exist_ok=True)

for name, code in codes.items():
    try:
        url = f"https://api.mfapi.in/mf/{code}"

        r = requests.get(url, timeout=30)
        r.raise_for_status()

        data = r.json()

        if "data" in data:
            df = pd.DataFrame(data["data"])
            df.to_csv(out / f"{name}.csv", index=False)

            print(f"Saved {name}: {len(df)} rows")

    except Exception as e:
        print(f"Failed {name}: {e}")