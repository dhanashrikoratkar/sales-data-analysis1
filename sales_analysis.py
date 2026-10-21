
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the sales dataset
df = pd.read_csv("sales_data_analysis.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Display basic information
print("First five rows:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

# Calculate total revenue
total_revenue = df["Revenue_INR"].sum()
print("\nTotal Revenue: ₹", total_revenue)

# Revenue by product
product_revenue = df.groupby("Product")["Revenue_INR"].sum()
print("\nRevenue by Product:")
print(product_revenue.sort_values(ascending=False))

# Revenue by month
df["Month"] = df["Date"].dt.to_period("M")
monthly_revenue = df.groupby("Month")["Revenue_INR"].sum()
print("\nMonthly Revenue:")
print(monthly_revenue)

# Revenue by region
region_revenue = df.groupby("Region")["Revenue_INR"].sum()
print("\nRevenue by Region:")
print(region_revenue.sort_values(ascending=False))

# Revenue by sales channel
channel_revenue = df.groupby("Sales_Channel")["Revenue_INR"].sum()
print("\nRevenue by Sales Channel:")
print(channel_revenue)

# Plot revenue by product
product_revenue.sort_values().plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.show()

# Plot monthly revenue
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.show()
