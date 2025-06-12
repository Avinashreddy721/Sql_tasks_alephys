import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",      
    password="123456789",
    database="tasks"
)
cursor = conn.cursor()

# give four queries

def run_query(title, sql):
    print(f"\n---- {title} ----")
    df = pd.read_sql(sql, conn)
    print(df)



run_query("Q3: Running Total in Sales", """
SELECT date, amount,
    SUM(amount) OVER (ORDER BY date) AS running_total
FROM sales;
""")







run_query("Q4: Duplicate (col1, col2) combinations", """
SELECT col1, col2, COUNT(*) AS dup_count
FROM transactions
GROUP BY col1, col2
HAVING COUNT(*) > 1;
""")

cursor.close()
conn.close()
