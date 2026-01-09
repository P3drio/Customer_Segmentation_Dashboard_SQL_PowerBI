import os
import sqlite3

# Paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
DB_PATH = os.path.join(PROJECT_ROOT, "data", "retail.db")
SQL_SCRIPT_PATH = os.path.join(PROJECT_ROOT, "SQL", "process_data.sql")

# Run SQL script

with sqlite3.connect(DB_PATH) as conn:
    with open(SQL_SCRIPT_PATH, "r", encoding="utf-8") as f:
        sql_script = f.read()
    conn.executescript(sql_script)

print("SQL processing completed: cleaned data and customer summary created.")