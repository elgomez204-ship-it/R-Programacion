'''
  Aplicación de gestión de libros
  (c) 2026 Juan Patino
  Esta aplicación gestiona libros
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Libro():
  def __init__(self):
    self.titulo = ""
    self.autor = ""
    self.precio = 0
    
# Creamos las variables globales

libros = []

# Primero lanzamos un mensaje de bienvenida
print("Gestor de libros v0.1 Juan Patino")
# Metemos al usuario en un bucle infinito
while True:
  # Le mostramos al usuario las opciones que tiene
  print("Selecciona una opción:")
  print("1.-Crear un nuevo libro")
  print("2.-Listar libros")
  print("3.-Actualizar libros")
  print("4.-Eliminar libros")
  opcion = int(input("Escoge tu opción: "))
  # En función de la opción que coja el usuario
  if opcion == 1:
    # O bien creamos un nuevo libro
    print("Creamos un nuevo libro")
  elif opcion == 2:
    # O bien listamos los libros
    print("Vamos a listar los libros")
  elif opcion == 3:
    # O bien actualizamos los libros
    print("Vamos a actualizar libros")
  elif opcion == 4:
    # O bien eliminamos los libros
    print("Vamos a eliminar libros")
  # Y volvemos a repetir