import sqlite3

conn = sqlite3.connect("sales_data.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

sample = [
    ("2025-01-01", "Widget", 10, 5.00),
    ("2025-01-02", "Gadget", 3, 12.50),
    ("2025-01-03", "Widget", 7, 5.00),
    ("2025-01-03", "Thingamajig", 5, 8.00),
    ("2025-01-04", "Gadget", 2, 12.50),
    ("2025-01-05", "Thingamajig", 4, 8.00),
]

cur.executemany("INSERT INTO sales (date, product, quantity, price) VALUES (?, ?, ?, ?)", sample)
conn.commit()
conn.close()
print("sales_data.db created with sample data.")