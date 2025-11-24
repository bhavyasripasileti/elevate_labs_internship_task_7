import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales_data.db")

query = """
SELECT
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
"""

df = pd.read_sql_query(query, conn)

print("\nSALES SUMMARY:\n")
print(df.to_string(index=False))

ax = df.plot(kind="bar", x="product", y="revenue", legend=False)
ax.set_xlabel("Product")
ax.set_ylabel("Revenue")
ax.set_title("Revenue by Product")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

conn.close()