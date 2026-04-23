# CRUD
# Create 
# Read
# Update
# Delete

class Contacto():
  def __init__(self):
    self.email = None
    self.nombre = None
    self.direccion = None

print("Programa de gestión de contactos v0.1 Juan Patino")

# Muestro opciones en el menú para el usuario
print("Selecciona una opción: ")
print("1.-Insertar un contacto")
print("2.-Listar contactos")
print("3.-Actualizar contactos")
print("4.-Eliminar contactos")

contactos = []   # Creo una lista VACIA

while True: # Esto desata un bucle infinito pero controlado

  # Le permito escoger una opción
  opcion = input("Escoge una opción: ")
  opcion = int(opcion)   # Convierto a entero
  
  if opcion == 1:
    print("Vamos a insertar un contacto")
    # Primero creamos un nuevo contacto
    nuevcontacto = Contacto()
    # Ahora le ponemos propiedades
    nuevcontacto.nombre = input("Introduce el nombre del contacto: ")
    nuevcontacto.email = input("Introduce el email del contacto: ")
    nuevcontacto.direccion = input("Introduce la direccion del contacto: ")
    # A la lista de contactos añadimos nuestro contacto
    contactos.append(nuevcontacto)
  elif opcion == 2:
    print("Vamos a ver los contactos")
    print(contactos)
  elif opcion == 3:
    print("Vamos a actualizar un contacto")
  elif opcion == 4:
    print("Vamos a eliminar un contacto")
  else:
    break
    