#step 1 : Environment setup (venv, pandas, matplotlib)
import pandas as pd

# to load the raw data
df = pd.read_csv(r'C:\Users\LUKESH\OneDrive\Desktop\RetailSalesAnalysis\python\data\SuperStoreOrdersfi.csv', encoding='utf-8')

#first look
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
print(df.head(10))

#step 2 : data cleaning
#to clean the sales column - strip the comma and convert to float
df['sales'] = df['sales'].str.replace(',', '', regex=False).astype(float)
print(df['sales'].dtype)
print(df['sales'].describe())

# step 3 : Fix the mixed date formats
def parse_mixed_date(date_str):
    date_str = str(date_str).strip()
    if '/' in date_str:
        return pd.to_datetime(date_str, format='%m/%d/%Y', errors='coerce')
    else:
        return pd.to_datetime(date_str, format='%d-%m-%Y', errors='coerce')

df['order_date'] = df['order_date'].apply(parse_mixed_date)
df['ship_date'] = df['ship_date'].apply(parse_mixed_date)

print(df[['order_date', 'ship_date']].dtypes)
print(df[['order_date', 'ship_date']].head())
print(df['order_date'].isna().sum(), df['ship_date'].isna().sum())

#step 6 : Save cleaned data for reuse
df.to_csv('../data/Superstore_cleaned.csv', index=False)

#step 5 : 	Calculate KPIs

print("=== KPIs ===")

total_revenue = df['sales'].sum()
total_profit = df['profit'].sum()
total_orders = df['order_id'].nunique()
total_customers = df['customer_name'].nunique()
avg_order_value = total_revenue / total_orders
profit_margin = total_profit / total_revenue

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Avg Order Value: ${avg_order_value:,.2f}")
print(f"Profit Margin: {profit_margin:.1%}")

# step - 6 : group-by analysis

# Group by Region (sales + profit)

by_region = df.groupby('region').agg(sales=('sales', 'sum'), profit=('profit', 'sum')).sort_values('sales', ascending=False)
by_category = df.groupby('category').agg(sales=('sales', 'sum'), profit=('profit', 'sum')).sort_values('sales', ascending=False)
by_subcategory = df.groupby('sub_category').agg(sales=('sales', 'sum'), profit=('profit', 'sum')).sort_values('sales', ascending=False)
by_segment = df.groupby('segment').agg(sales=('sales', 'sum'), profit=('profit', 'sum')).sort_values('sales', ascending=False)

df['order_month'] = df['order_date'].dt.to_period('M').astype(str)
monthly = df.groupby('order_month').agg(sales=('sales', 'sum'), profit=('profit', 'sum')).sort_index()

top_products = df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(10)

print("=== BY REGION ===")
print(by_region)
print("\n=== BY CATEGORY ===")
print(by_category)
print("\n=== BY SUB-CATEGORY ===")
print(by_subcategory)
print("\n=== BY SEGMENT ===")
print(by_segment)
print("\n=== TOP 10 PRODUCTS ===")
print(top_products)

# Step 7: Charts

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ---- helper function to add $ symbol to y-axis labels ----
def format_as_dollars(ax):
    # get the current y-axis tick values (the numbers already shown)
    ticks = ax.get_yticks()
    # build a new list of labels, each with a $ in front
    new_labels = []
    for value in ticks:
        new_labels.append(f'${value:,.0f}')
    ax.set_yticklabels(new_labels)

# ---- Monthly Revenue Trend (line chart) ----
plt.figure(figsize = (10, 4.5))
plt.plot(monthly.index, monthly['sales'], marker = 'o', color = 'blue')
plt.title('Monthly Revenue Trend')
plt.ylabel('Revenue')
plt.xticks(rotation = 90, fontsize = 7)
plt.tight_layout()
plt.savefig(r'C:\Users\LUKESH\OneDrive\Desktop\RetailSalesAnalysis\python\screenshots\monthly_revenue_trend.png')
plt.close()

# ---- Revenue by Region (bar chart) ----
plt.figure(figsize=(8, 4.5))
plt.bar(by_region.index, by_region['sales'], color = 'blue')
plt.title('Revenue by Region')
plt.ylabel('Revenue')
plt.xticks(rotation = 45, ha='right')
plt.tight_layout()
plt.savefig(r'C:\Users\LUKESH\OneDrive\Desktop\RetailSalesAnalysis\python\screenshots\revenue_by_region.png')
plt.close()

# ---- Profit by Category (bar chart, red if losing money) ----
plt.figure(figsize = (6, 4.5))

# build a list of colors: one color per category, based on whether profit is negative
bar_colors = []
for value in by_category['profit']:
    if value >= 0:
        bar_colors.append('blue') #means profit
    else:
        bar_colors.append('red') #means loss

plt.bar(by_category.index, by_category['profit'], color = bar_colors)
plt.title('Profit by category')
plt.ylabel('Profit')
plt.xticks(rotation = 0)
plt.tight_layout()
plt.savefig(r'C:\Users\LUKESH\OneDrive\Desktop\RetailSalesAnalysis\python\screenshots\profit_by_category.png')
plt.close()

# ---- Top 10 Products (horizontal bar chart) ----
plt.figure(figsize=(9,5))
sorted_products = top_products.sort_values()
plt.barh(sorted_products.index, sorted_products.values, color = 'blue')
plt.title('Top 10 Products by Sales')
plt.xlabel('Revenue')
plt.tight_layout()
plt.savefig(r'C:\Users\LUKESH\OneDrive\Desktop\RetailSalesAnalysis\python\screenshots\Top10_Products')
plt.close()

# ---- Revenue by Sub-Category (red = losing money) ----
plt.figure(figsize=(9,5))

bar_colors = []
for value in by_subcategory['profit']:
    if value >= 0:
        bar_colors.append('blue')
    else:
        bar_colors.append('red')

plt.bar(by_subcategory.index, by_subcategory['sales'], color = bar_colors)
plt.title('Revenue by Sub-Category')
plt.ylabel('Revenue')
plt.xticks(rotation = 60, ha = 'right', fontsize = 8)
plt.tight_layout()
plt.savefig(r'C:\Users\LUKESH\OneDrive\Desktop\RetailSalesAnalysis\python\screenshots\Revenue_by_Sub_Category')
plt.close()

print('All charts are saved to screenshots')

