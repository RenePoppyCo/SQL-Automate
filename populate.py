import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# first "clears" table, then creates sales_data table
cursor.execute("DROP TABLE IF EXISTS sales_data")
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales_data (
    id INTEGER PRIMARY KEY,
    date DATE,
    product TEXT,
    quantity INTEGER,
    price REAL
);
''')

# generate mock sales data
def generate_mock_sales(num_rows):
    product_count = {}
    products = ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Printer', 'Headphones']
    mock_data = []
    for _ in range(num_rows):
        date = (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')  # Random date within the last year
        product = random.choice(products)  
        
        if (any(product in tuple_item for tuple_item in mock_data)):
            product_count[product] += 1
            product = f"{product}_{product_count[product]}"
            print("what we made: ",product)
        else:                
            product_count[product] = 1
            print(product_count[product])

        quantity = random.randint(1, 10)  
        price = round(random.uniform(10.0, 1000.0), 2)  
        mock_data.append((None, date, product, quantity, price))
    return mock_data

mock_sales = generate_mock_sales(random.randint(20, 30))

# Insert mock data into the sales_data table
cursor.executemany('''
INSERT INTO sales_data (id, date, product, quantity, price)
VALUES (?, ?, ?, ?, ?);
''', mock_sales)

conn.commit()

cursor.execute('SELECT COUNT(*) FROM sales_data;')
row_count = cursor.fetchone()[0]
print(f"Inserted {row_count} rows into sales_data table.")

conn.close()