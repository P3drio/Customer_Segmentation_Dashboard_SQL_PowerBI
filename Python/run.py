import os
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

# Paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

RAW_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "raw", "online_retail_II.csv")
DB_PATH = os.path.join(PROJECT_ROOT, "data", "retail.db")
SQL_SCRIPT_PATH = os.path.join(PROJECT_ROOT, "SQL", "process_data.sql")

# 1. Load CSV into SQLite

if not os.path.exists(RAW_DATA_PATH):
    raise FileNotFoundError(f"Raw data not found: {RAW_DATA_PATH}")

df = pd.read_csv(RAW_DATA_PATH, encoding="unicode_escape")

# Rename columns for SQL consistency
df = df.rename(columns={
    'Customer ID': 'CustomerID',
    'Price': 'UnitPrice'
})

# Create SQLite engine
engine = create_engine(f"sqlite:///{DB_PATH}")

# Load raw data
df.to_sql(
    'online_retail_raw',
    engine,
    if_exists='replace',
    index=False
)

print(f"[1/3] Raw data loaded into SQLite database at {DB_PATH}")

# 2. Run SQL processing

with sqlite3.connect(DB_PATH) as conn:
    with open(SQL_SCRIPT_PATH, "r", encoding="utf-8") as f:
        sql_script = f.read()
    conn.executescript(sql_script)

print("[2/3] SQL processing completed: cleaned data and customer summary created.")

# 3. Quick preview

with sqlite3.connect(DB_PATH) as conn:
    preview = pd.read_sql("SELECT * FROM customer_summary LIMIT 10;", conn)

print("[3/3] Customer summary preview:")
print(preview)