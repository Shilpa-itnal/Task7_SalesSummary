import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

DB_PATH = "sales_data.db"

SAMPLE_DATA = [
    ("2025-09-01", "Widget A", 10, 9.99),
    ("2025-09-02", "Widget B", 5, 19.99),
    ("2025-09-03", "Widget A", 7, 9.99),
    ("2025-09-04", "Widget C", 3, 29.99),
    ("2025-09-05", "Widget B", 4, 19.99),
    ("2025-09-06", "Widget A", 2, 9.99),
    ("2025-09-07", "Widget C", 1, 29.99),
]

def create_db_and_seed(db_path):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_date TEXT,
            product TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        );
        """)
        cur.execute("SELECT COUNT(*) FROM sales;")
        count = cur.fetchone()[0]
        if count == 0:
            cur.executemany(
                "INSERT INTO sales (sale_date, product, quantity, price) VALUES (?, ?, ?, ?);",
                SAMPLE_DATA
            )
            conn.commit()
            print(f"Seeded {len(SAMPLE_DATA)} rows into {db_path}")
        else:
            print(f"DB already has {count} rows — skipping seed.")

def run_queries_and_plot(db_path):
    conn = sqlite3.connect(db_path)
    query = """
    SELECT product,
           SUM(quantity) AS total_qty,
           SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC;
    """
    df = pd.read_sql_query(query, conn)
    df['total_qty'] = df['total_qty'].astype(int)
    df['revenue'] = df['revenue'].round(2)

    print("\nSales Summary:")
    print(df.to_string(index=False))

    ax = df.plot(kind='bar', x='product', y='revenue', legend=False)
    ax.set_xlabel("Product")
    ax.set_ylabel("Revenue")
    ax.set_title("Revenue by Product")
    plt.tight_layout()
    plt.savefig("sales_chart.png")
    plt.show()
    print("\nChart saved as sales_chart.png")
    conn.close()

if __name__ == "__main__":
    create_db_and_seed(DB_PATH)
    run_queries_and_plot(DB_PATH)