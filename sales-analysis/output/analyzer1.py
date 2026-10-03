# import os
# from pathlib import Path
# # Check if we're in the right place
# print("Current directory:", os.getcwd())

# # Base directory: one level up from this script (sales-analysis/)
# BASE_DIR = Path(__file__).resolve().parents[2]
# print(BASE_DIR)

# # Construct path to sales-analysis/data/paris_weather.csv
# data_path = BASE_DIR / "data" / "paris_weather.csv"

# # Check if our data file exists

# if data_path.exists():
#     print(f"✅ Found {data_path}")
# else:
#     print(f"❌ Cannot find {data_path}")
#     print("Make sure you're running from the sales-analysis folder!")

import pandas as pd
import json
import os
from pathlib import Path

# Read the CSV file
BASE_DIR = Path(__file__).resolve().parents[1]
print(BASE_DIR)
df = pd.read_csv(BASE_DIR / "data" / "sales.csv")
print("CSV Data:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

# Create output directory
os.makedirs(BASE_DIR / "output", exist_ok=True)

# Save as different formats
# 1. JSON format (good for web APIs)
df.to_json(BASE_DIR / "output" / "sales_data.json", orient='records', indent=2)

# 2. Excel format (good for sharing)
#df.to_excel(BASE_DIR / "output" / "sales_data.xlsx", index=False)

# 3. Updated CSV (with our new total column)
df.to_csv(BASE_DIR / "output" / "sales_with_totals.csv", index=False)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx") 
print("- output/sales_with_totals.csv")