import pandas as pd
import os

# Paths
raw_path = os.path.join('..', 'data', 'raw', 'online_retail_II.csv')
clean_path = os.path.join('..', 'data', 'cleaned', 'online_retail_II_cleaned.csv')

# Load dataset
df = pd.read_csv(raw_path, encoding='unicode_escape')

# Remove canceled transactions
df = df[~df['Invoice'].astype(str).str.startswith('C')]

# Calculate TotalPrice
df['TotalPrice'] = df['Quantity'] * df['Price']

# Remove rows with missing CustomerID or TotalPrice <=0
df.dropna(subset=['Customer ID', 'TotalPrice'], inplace=True)
df = df[df['TotalPrice'] > 0]

# Remove duplicates
df.drop_duplicates(inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

# Export cleaned data
df.to_csv(clean_path, index=False)
print(f"Cleaned data exported to {clean_path}")