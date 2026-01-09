import os
import pandas as pd
from sqlalchemy import create_engine


# Paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))  # project root

RAW_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "raw", "online_retail_II.csv")
DB_PATH = os.path.join(PROJECT_ROOT, "data", "retail.db")

# File check
if not os.path.exists(RAW_DATA_PATH):
    raise FileNotFoundError(f"Raw data not found: {RAW_DATA_PATH}")

# Load raw dataset
df = pd.read_csv(RAW_DATA_PATH, encoding='unicode_escape')

# Rename columns to remove spaces
df = df.rename(columns={
    'Customer ID': 'CustomerID',
    'InvoiceDate': 'InvoiceDate',
    'Price': 'UnitPrice'
})

# Create SQLite engine

engine = create_engine(f"sqlite:///{DB_PATH}")

# Load raw data into database
df.to_sql(
    'online_retail_raw',
    engine,
    if_exists='replace',
    index=False
)

print("Raw data successfully loaded into SQLite database.")