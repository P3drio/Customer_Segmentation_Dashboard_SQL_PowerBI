import os
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

RAW_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "raw", "online_retail_II.csv")
DB_PATH = os.path.join(PROJECT_ROOT, "data", "retail.db")

SQL_FILES = [
    os.path.join(PROJECT_ROOT, "SQL", "01_schema.sql"),
    os.path.join(PROJECT_ROOT, "SQL", "02_cleaning.sql"),
    os.path.join(PROJECT_ROOT, "SQL", "03_features.sql"),
    os.path.join(PROJECT_ROOT, "SQL", "04_segmentation.sql"),
]

# Load CSV
if not os.path.exists(RAW_DATA_PATH):
    raise FileNotFoundError(f"Raw data not found: {RAW_DATA_PATH}")

df = pd.read_csv(RAW_DATA_PATH, encoding="unicode_escape")
df = df.rename(columns={
    'Customer ID': 'CustomerID',
    'Price': 'UnitPrice'
})

engine = create_engine(f"sqlite:///{DB_PATH}")
df.to_sql('online_retail_raw', engine, if_exists='replace', index=False)
print(f"Raw data loaded into SQLite at {DB_PATH}")

# Run SQL files in order
with sqlite3.connect(DB_PATH) as conn:
    for sql_file in SQL_FILES:
        if not os.path.exists(sql_file):
            raise FileNotFoundError(f"SQL file not found: {sql_file}")
        with open(sql_file, "r", encoding="utf-8") as f:
            sql_script = f.read()
        try:
            conn.executescript(sql_script)
            print(f"Executed {os.path.basename(sql_file)}")
        except sqlite3.DatabaseError as e:
            print(f"[ERROR] SQL execution failed in {os.path.basename(sql_file)}: {e}")
            raise

# Quick preview
with sqlite3.connect(DB_PATH) as conn:
    try:
        preview = pd.read_sql("SELECT * FROM customer_summary LIMIT 10;", conn)
        print("Customer summary preview:")
        print(preview)
    except Exception as e:
        print(f"[WARNING] Could not preview customer_summary: {e}")