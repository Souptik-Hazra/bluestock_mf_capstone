import pandas as pd
from pathlib import Path

fund_master = pd.read_csv(
    Path("data/raw/01_fund_master.csv")
)

nav_history = pd.read_csv(
    Path("data/raw/02_nav_history.csv")
)

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes
extra_codes = nav_codes - fund_codes

print("=" * 60)
print("AMFI CODE VALIDATION REPORT")
print("=" * 60)

print(f"\nFund Master Codes : {len(fund_codes)}")
print(f"NAV History Codes : {len(nav_codes)}")

if len(missing_codes) == 0:
    print("\nAll fund_master AMFI codes exist in nav_history")
else:
    print("\nMissing Codes:")
    for code in sorted(missing_codes):
        print(code)

if len(extra_codes) == 0:
    print("\nNo extra codes found in nav_history")
else:
    print("\nExtra Codes Found:")
    for code in sorted(extra_codes):
        print(code)

print("\nDATA QUALITY SUMMARY")
print("-" * 30)
print(f"Missing Codes : {len(missing_codes)}")
print(f"Extra Codes   : {len(extra_codes)}")

if len(missing_codes) == 0 and len(extra_codes) == 0:
    print("\nPASS: Data integrity validated")
else:
    print("\nWARNING: Validation issues detected")