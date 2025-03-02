import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")
query = """
        SELECT date, product, price,
            SUM(quantity) AS total_sold,
            SUM(quantity * price) AS total_revenue
        FROM sales_data
        GROUP BY date, product;
        """

df = pd.read_sql_query(query, conn)

conn.close()

print("Sales Summary:")
print(df.head())

total_revenue = df['total_revenue'].sum()
print(f"\nTotal Overall Revenue: ${total_revenue:.2f}")

# Export DataFrame to a CSV file
df.to_csv('sales_summary.csv', index=False, float_format='%.3f')
print("\nData exported to 'sales_summary.csv'.")