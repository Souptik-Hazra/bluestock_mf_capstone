-- Top 5 Fund Houses by AUM
SELECT fund_house,
SUM(aum_crore) total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- Average NAV
SELECT amfi_code,
AVG(nav) avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- Top 10 Funds by 3Y Return
SELECT amfi_code,
return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;

-- Top 10 Funds by Sharpe Ratio
SELECT amfi_code,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- Expense Ratio < 1%
SELECT scheme_name,
expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

-- Transactions by State
SELECT state,
COUNT(*) transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;

-- Transaction Type Distribution
SELECT transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- KYC Status Distribution
SELECT kyc_status,
COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;

-- Average Investment by Age Group
SELECT age_group,
AVG(amount_inr)
FROM fact_transactions
GROUP BY age_group;

-- Gender Wise Investment
SELECT gender,
SUM(amount_inr)
FROM fact_transactions
GROUP BY gender;