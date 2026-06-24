# Bluestock Mutual Fund Analytics - Data Dictionary

## Project Overview

This document describes all datasets, columns, data types, business definitions, and source references used in the Mutual Fund Analytics Capstone Project.

---

# Dataset 1: fund_master

**Source:** `01_fund_master.csv`

| Column | Data Type | Business Definition |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| fund_house | TEXT | Asset Management Company (AMC) |
| scheme_name | TEXT | Mutual fund scheme name |
| category | TEXT | Broad mutual fund category |
| sub_category | TEXT | Detailed fund category |
| plan | TEXT | Direct or Regular plan |
| launch_date | DATE | Scheme launch date |
| benchmark | TEXT | Benchmark index used for comparison |
| expense_ratio_pct | FLOAT | Annual expense ratio (%) |
| exit_load_pct | FLOAT | Exit load percentage |
| min_sip_amount | INTEGER | Minimum SIP investment amount |
| min_lumpsum_amount | INTEGER | Minimum lump sum investment |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | Risk classification |
| sebi_category_code | TEXT | SEBI category identifier |

---

# Dataset 2: nav_history

**Source:** `02_nav_history.csv`

| Column | Data Type | Business Definition |
|----------|----------|----------|
| amfi_code | INTEGER | Mutual fund scheme code |
| date | DATE | NAV date |
| nav | FLOAT | Net Asset Value |

---

# Dataset 3: aum_by_fund_house

**Source:** `03_aum_by_fund_house.csv`

| Column | Data Type | Business Definition |
|----------|----------|----------|
| date | DATE | Reporting date |
| fund_house | TEXT | AMC name |
| aum_lakh_crore | FLOAT | AUM in lakh crore |
| aum_crore | FLOAT | AUM in crore |
| num_schemes | INTEGER | Number of schemes managed |

---

# Dataset 4: monthly_sip_inflows

**Source:** `04_monthly_sip_inflows.csv`

| Column | Data Type | Business Definition |
|----------|----------|----------|
| month | DATE | Reporting month |
| sip_inflow_crore | FLOAT | Monthly SIP inflow in crore rupees |

---

# Dataset 5: category_inflows

**Source:** `05_category_inflows.csv`

| Column | Data Type | Business Definition |
|----------|----------|----------|
| category | TEXT | Fund category |
| date | DATE | Reporting period |
| inflow_crore | FLOAT | Net inflow/outflow amount |

---

# Dataset 6: industry_folio_count

**Source:** `06_industry_folio_count.csv`

| Column | Data Type | Business Definition |
|----------|----------|----------|
| date | DATE | Reporting date |
| folio_count | INTEGER | Total investor folios |

---

# Dataset 7: scheme_performance

**Source:** `07_scheme_performance.csv`

| Column | Data Type | Business Definition |
|----------|----------|----------|
| amfi_code | INTEGER | Scheme identifier |
| scheme_name | TEXT | Scheme name |
| fund_house | TEXT | AMC name |
| category | TEXT | Fund category |
| plan | TEXT | Direct/Regular |
| return_1yr_pct | FLOAT | One-year return (%) |
| return_3yr_pct | FLOAT | Three-year return (%) |
| return_5yr_pct | FLOAT | Five-year return (%) |
| benchmark_3yr_pct | FLOAT | Benchmark 3-year return |
| alpha | FLOAT | Excess return over benchmark |
| beta | FLOAT | Market sensitivity |
| sharpe_ratio | FLOAT | Risk-adjusted performance metric |
| sortino_ratio | FLOAT | Downside risk-adjusted return |
| std_dev_ann_pct | FLOAT | Annualized volatility |
| max_drawdown_pct | FLOAT | Maximum historical decline |
| aum_crore | FLOAT | Assets under management |
| expense_ratio_pct | FLOAT | Expense ratio |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk grade classification |

---

# Dataset 8: investor_transactions

**Source:** `08_investor_transactions.csv`

| Column | Data Type | Business Definition |
|----------|----------|----------|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Fund scheme code |
| transaction_type | TEXT | SIP, Lumpsum, Redemption |
| amount_inr | FLOAT | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | T30/B30 classification |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | FLOAT | Annual income in lakh rupees |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | KYC verification status |

---

# Dataset 9: portfolio_holdings

**Source:** `09_portfolio_holdings.csv`

| Column | Data Type | Business Definition |
|----------|----------|----------|
| amfi_code | INTEGER | Fund scheme code |
| company_name | TEXT | Invested company |
| sector | TEXT | Industry sector |
| weight_pct | FLOAT | Portfolio allocation percentage |

---

# Dataset 10: benchmark_indices

**Source:** `10_benchmark_indices.csv`

| Column | Data Type | Business Definition |
|----------|----------|----------|
| date | DATE | Trading date |
| benchmark_name | TEXT | Benchmark index |
| close_price | FLOAT | Closing index value |
| daily_return_pct | FLOAT | Daily benchmark return |

---

# Data Cleaning Rules

1. Remove duplicate records.
2. Remove completely empty rows.
3. Convert date columns to datetime format.
4. Validate NAV values greater than zero.
5. Validate transaction amounts greater than zero.
6. Validate expense ratio range (0.1%–2.5%).
7. Flag negative Sharpe Ratio schemes.
8. Standardize transaction types (SIP, Lumpsum, Redemption).
9. Validate KYC status values.
10. Maintain referential integrity using AMFI codes.

---

# Database Schema

## Dimension Tables

- dim_fund

## Fact Tables

- fact_nav
- fact_transactions
- fact_performance
- fact_aum

**Database File:** `data/db/bluestock_mf.db`

---

## Source References

| Dataset | Source File |
|----------|------------|
| Fund Master | 01_fund_master.csv |
| NAV History | 02_nav_history.csv |
| AUM Data | 03_aum_by_fund_house.csv |
| SIP Inflows | 04_monthly_sip_inflows.csv |
| Category Inflows | 05_category_inflows.csv |
| Folio Count | 06_industry_folio_count.csv |
| Scheme Performance | 07_scheme_performance.csv |
| Investor Transactions | 08_investor_transactions.csv |
| Portfolio Holdings | 09_portfolio_holdings.csv |
| Benchmark Indices | 10_benchmark_indices.csv |

---

**Project:** Mutual Fund Analytics Capstone  
**Database:** SQLite (`bluestock_mf.db`)  
**Prepared For:** Capstone Project I