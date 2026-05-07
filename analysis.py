import pandas as pd

df = pd.read_csv("sales_data.csv")

print(df)

total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

top_product = df.groupby("Product")["Sales"].sum()

print("\nSales By Product:")
print(top_product)