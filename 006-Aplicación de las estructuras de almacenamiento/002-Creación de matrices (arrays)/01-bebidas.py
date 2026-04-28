menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva bebida en el menú")
  print("2.-Listar bebidas en el menú")
  opcion = input("Selecciona una opción:")
  bebida = input("Introduce el nombre de la bebida: ")
  menu.append(bebida)
  print("Tu bebida hasta el momento es:")
  for elemento in menu:
    print(elemento)