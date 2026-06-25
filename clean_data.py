import pandas as pd

perf = pd.read_csv("data/raw/07_scheme_performance.csv")

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Find invalid expense ratios
anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]

print("Expense Ratio Anomalies:")
print(len(anomalies))

# Save cleaned file
perf.to_csv(
    "processed/scheme_performance_clean.csv",
    index=False
)

print("\nSaved Successfully!")
print("Rows:", len(perf))