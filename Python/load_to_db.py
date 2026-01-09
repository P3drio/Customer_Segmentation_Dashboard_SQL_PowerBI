import pandas as pd
from sqlalchemy import create_engine
import os

# Paths
RAW_DATA_PATH = os.path.join('..', 'data', 'raw', 'online_retail_II.csv')
DB_PATH = os.path.join('..', 'data', 'retail.db')

# Load raw dataset
df = pd.read_csv(RAW_DATA_PATH, encoding='unicode_escape')

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