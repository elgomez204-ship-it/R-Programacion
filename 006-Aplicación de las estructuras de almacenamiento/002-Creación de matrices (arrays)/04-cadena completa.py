import pickle

menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva bebida en el menú")
  print("2.-Listar bebidas en el menú")
  print("3.-Guardar en archivo")
  print("4.-Cargar datos de archivo")
  opcion = int(input("Selecciona una opción:"))
  if opcion == 1:
    bebida = input("Introduce el nombre de la bebida: ")
    menu.append(bebida)
  elif opcion == 2:
    print("Tu bebida hasta el momento es:")
    for elemento in menu:
      print(elemento)
  elif opcion == 3:
    archivo = open("datos.bin","wb") # Write Binary
    pickle.dump(menu,archivo)
    archivo.close()
    print("Se ha guardado con éxito ✅")
  elif opcion == 4:
    archivo = open("datos.bin","rb")
    menu = pickle.load(archivo) # Volcamos el archivo a la lista
    archivo.close()
    print("Se ha cargado con éxito ✅")