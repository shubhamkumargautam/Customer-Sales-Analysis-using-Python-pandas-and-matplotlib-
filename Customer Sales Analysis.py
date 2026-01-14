import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Datasets
# -----------------------------
sales_df = pd.read_csv(r"C:\Users\shubh\Desktop\Arena projects file document\5th week project\Sales_Data.csv")
customer_df = pd.read_csv(r"C:\Users\shubh\Desktop\Arena projects file document\5th week project\customer_churn.csv")

print("✅ Datasets Loaded Successfully\n")

# -----------------------------
# 2. Explore Structure
# -----------------------------

print("📊 Sales Data - First 5 Rows")
print(sales_df.head(), "\n")

print("📊 Customer Data - First 5 Rows")
print(customer_df.head(), "\n")

print("ℹ️ Sales Data Info")
print(sales_df.info(), "\n")

print("ℹ️ Customer Data Info")
print(customer_df.info(), "\n")

print("📐 Sales Data Shape:", sales_df.shape)
print("📐 Customer Data Shape:", customer_df.shape, "\n")

# -----------------------------
# 3. Check Missing Values
# -----------------------------
print("❓ Missing Values in Sales Data")
print(sales_df.isnull().sum(), "\n")

print("❓ Missing Values in Customer Data")
print(customer_df.isnull().sum())




