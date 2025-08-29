import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Basic summary
print("Dataset Shape:", df.shape)
print(df.head())

# Sales by region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Region:\n", region_sales)

# Plot top 5 products
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(8,5))
top_products.plot(kind="bar", color="skyblue")
plt.title("Top 5 Products by Sales")
plt.ylabel("Total Sales")
plt.show()
