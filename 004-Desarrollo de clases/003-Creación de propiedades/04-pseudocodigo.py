'''
  Aplicación de gestión de Libros
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
# Le mostramos al usuario las opciones que tiene
# En función de la opción que coja el usuario
  # O bien creamos un nuevo libro
  # O bien listamos los libros
  # O bien actualizamos los libros
  # O bien eliminamos los libros