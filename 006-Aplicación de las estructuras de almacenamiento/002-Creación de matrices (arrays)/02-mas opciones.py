menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva bebida en el menú")
  print("2.-Listar bebidas en el menú")
  opcion = int(input("Selecciona una opción:"))
  if opcion == 1:
    bebida = input("Introduce el nombre de la bebida: ")
    menu.append(bebida)
  elif opcion == 2:
    print("Tu bebida hasta el momento es:")
    for elemento in menu:
      print(elemento)