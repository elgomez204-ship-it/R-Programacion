import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="corporacion2026",
    password="Corporacion2026$",
    database="corporacion2026"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()