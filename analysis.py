import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data/sales_data.csv')

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Display first few rows
print("Sample Data:")
print(data.head())

# Total sales
total_sales = data['Sales'].sum()
print(f"\nTotal Sales: {total_sales}")

# Average sales
avg_sales = data['Sales'].mean()
print(f"Average Sales: {avg_sales}")

# Sales by category
sales_by_category = data.groupby('Category')['Sales'].sum()
print("\nSales by Category:")
print(sales_by_category)

# Plot sales over time
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Sales'], marker='o', linestyle='-', color='b')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_over_time.png')  # Save the plot as a PNG file
plt.show()

# Plot sales by category
plt.figure(figsize=(8, 5))
sales_by_category.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_category.png')  # Save the plot as a PNG file
plt.show()
