# CRUD
# Create 
# Read
# Update
# Delete

print("Programa de gestión de contactos v0.1 Juan Patino")

# Muestro opciones en el menú para el usuario
print("Selecciona una opción: ")
print("1.-Insertar un contacto")
print("2.-Listar contactos")
print("3.-Actualizar contactos")
print("4.-Eliminar contactos")

# Le permito escoger una opción
opcion = input("Escoge una opción: ")
opcion = int(opcion)   # Convierto a entero

contactos = []   # Creo una lista VACIA

while True: # Esto desata un bucle infinito pero controlado
  if opcion == 1:
    print("Vamos a insertar un contacto")
  elif opcion == 2:
    print("Vamos a ver los contactos")
  elif opcion == 3:
    print("Vamos a actualizar un contacto")
  elif opcion == 4:
    print("Vamos a eliminar un contacto")
  else:
    break