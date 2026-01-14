import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter

# -----------------------------
# 1. Load Datasets
# -----------------------------
sales_df = pd.read_csv(r"C:\Users\shubh\Desktop\Arena projects file document\5th week project\Sales_Data.csv")
customer_df = pd.read_csv(r"C:\Users\shubh\Desktop\Arena projects file document\5th week project\customer_churn.csv")

print("✅ Datasets Loaded Successfully\n")

# --------------------------------
# 2. Fix Column Names
# --------------------------------
sales_df.columns = sales_df.columns.str.strip()
customer_df.columns = customer_df.columns.str.strip()

# Rename for consistency
sales_df.rename(columns={"Customer_ID": "CustomerID"}, inplace=True)

# --------------------------------
# 3. Date Processing (Seasonality)
# --------------------------------
sales_df['Date'] = pd.to_datetime(sales_df['Date'], errors='coerce')
sales_df['Month'] = sales_df['Date'].dt.month
sales_df['Year'] = sales_df['Date'].dt.year

# --------------------------------
# 4. Merge Sales + Customer Data
# --------------------------------
data = pd.merge(
    sales_df,
    customer_df,
    on="CustomerID",
    how="left"
)

# =========================================
# QUESTION 1: Most Valuable Customers
# =========================================
valuable_customers = (
    data.groupby('CustomerID')['Total_Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nMost Valuable Customers:")
print(valuable_customers)

# =========================================
# QUESTION 2: Products Sold Together
# =========================================
basket = data.groupby('CustomerID')['Product'].apply(list)

pairs = []
for products in basket:
    pairs.extend(combinations(sorted(set(products)), 2))

product_pairs = Counter(pairs).most_common(10)

print("\nTop Product Combinations:")
for pair, count in product_pairs:
    print(pair, "->", count)

# =========================================
# QUESTION 3: Highest Sales Regions
# =========================================
region_sales = data.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)

print("\nSales by Region:")
print(region_sales)

region_sales.plot(kind='bar', title='Sales by Region')
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# =========================================
# QUESTION 4: Seasonal Trends
# =========================================
monthly_sales = data.groupby('Month')['Total_Sales'].sum()

print("\nMonthly Sales Trend:")
print(monthly_sales)

monthly_sales.plot(kind='line', title='Monthly Sales Trend')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# =========================================
# QUESTION 5: Customer Retention Improvement
# =========================================
churn_analysis = customer_df['Churn'].value_counts()

print("\nCustomer Churn Count:")
print(churn_analysis)

churn_analysis.plot(kind='bar', title='Customer Churn Distribution')
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

print("\nRetention Suggestions:")
print("""
1. Offer discounts to month-to-month contract customers
2. Improve support for customers with high monthly charges
3. Promote long-term contracts
4. Loyalty rewards for high-value customers
""")




