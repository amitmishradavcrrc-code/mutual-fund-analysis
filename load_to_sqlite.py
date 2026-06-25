import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned CSVs
nav = pd.read_csv("processed/nav_history_clean.csv")
txn = pd.read_csv("processed/investor_transactions_clean.csv")
perf = pd.read_csv("processed/scheme_performance_clean.csv")

# Save to SQLite
nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully!")

print("NAV Rows:", len(nav))
print("Transaction Rows:", len(txn))
print("Performance Rows:", len(perf))