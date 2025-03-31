# 导入必要的库
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import chardet

file_path = "../data/ecommerce_sales.xlsx"

# 读取 CSV 数据
df = pd.read_excel("../data/ecommerce_sales.xlsx")
df.to_csv("../data/ecommerce_sales.csv", index=False, encoding='utf-8-sig')

# 查看加载的数据
# 打印列名
print("Columns in the DataFrame:",df.columns)


# 计算总销售额 
df['total_sales'] = df['quantity'] * df['unit_price']

# 解析日期
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.to_period('M')

# 计算月度销售额
monthly_sales = df.groupby('month')['total_sales'].sum()

# 可视化月度销售趋势
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o', linestyle='-')
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 查看最畅销产品
top_products = df.groupby('product')['total_sales'].sum().sort_values(ascending=False)

# 可视化最畅销产品
plt.figure(figsize=(10, 5))
sns.barplot(x=top_products.index, y=top_products.values, palette="Blues_r")
plt.xlabel("Product")
plt.ylabel("Total Sales ($)")
plt.title("Top Selling Products")
plt.xticks(rotation=45)
plt.show()
