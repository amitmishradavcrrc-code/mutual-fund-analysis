-- 1. Top 5 funds by AUM
SELECT * FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- 3. NAV by AMFI code
SELECT amfi_code, AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

-- 4. Transaction count by type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 5. Total transaction amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- 6. Funds with expense ratio < 1%
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 7. Average 1Y return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- 8. Average 3Y return
SELECT AVG(return_3yr_pct)
FROM fact_performance;

-- 9. Average 5Y return
SELECT AVG(return_5yr_pct)
FROM fact_performance;

-- 10. Total funds
SELECT COUNT(*)
FROM fact_performance;