import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Create Sample Sales Dataset
# -----------------------------
data = {
    "Date": pd.date_range(start="2024-01-01", periods=100, freq="D"),
    "Product": ["Shampoo", "Soap", "Toothpaste", "Detergent", "Lotion"] * 20,
    "Category": ["Personal Care", "Personal Care", "Personal Care", "Household", "Personal Care"] * 20,
    "Price": [120, 40, 60, 200, 150] * 20,
    "Quantity": [5, 12, 9, 4, 7] * 20
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]

print("First 5 rows of sales data:")
print(df.head())

# -----------------------------
# 2. Basic Analysis
# -----------------------------
print("\nTotal Revenue:", df["Total_Sales"].sum())
print("Top Selling Product:\n", df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False).head(1))

# -----------------------------
# 3. Visualization (Only Matplotlib)
# -----------------------------

# a) Sales by Product
df.groupby("Product")["Total_Sales"].sum().plot(kind="bar", figsize=(8,5), color="skyblue")
plt.title("Total Sales by Product")
plt.ylabel("Revenue (INR)")
plt.show()

# b) Sales Trend Over Time
df.groupby("Date")["Total_Sales"].sum().plot(figsize=(12,6))
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue (INR)")
plt.show()

# c) Sales by Category
df.groupby("Category")["Total_Sales"].sum().plot(kind="pie", autopct="%1.1f%%", figsize=(6,6))
plt.title("Sales Contribution by Category")
plt.ylabel("")
plt.show()
