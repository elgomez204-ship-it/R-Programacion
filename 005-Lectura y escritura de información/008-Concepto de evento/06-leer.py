import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="usuarios",
    password="Usuario123$",
    database="usuarios"
)
cursor = conexion.cursor()
cursor.execute('''
  SELECT * FROM clientes;
''')

filas = cursor.fetchall()

for fila in filas:
  print(fila)
  
cursor.close()
conexion.close()