import pymysql

conn = pymysql.connect(
    host="localhost",
    user="corporacion2026",
    password="Corporacion2026$",
    database="corporacion2026",
    charset="utf8mb4"
)

with conn.cursor() as cursor:
    cursor.execute("SELECT * FROM usuarios")
    for row in cursor.fetchall():
        print(row)

conn.close()