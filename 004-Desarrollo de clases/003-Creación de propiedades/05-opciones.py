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
# Le mostramos al usuario las opciones que tiene
print("Selecciona una opción:")
print("1.-Crear un nuevo libro")
print("2.-Listar libros")
print("3.-Actualizar libros")
print("4.-Eliminar libros")
# En función de la opción que coja el usuario
  # O bien creamos un nuevo libro
  # O bien listamos los libros
  # O bien actualizamos los libros
  # O bien eliminamos los libros
# Y volvemos a repetir