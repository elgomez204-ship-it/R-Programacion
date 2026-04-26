import pickle

class Usuario():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de usuarios v0.1 ######")
print("####### Juan Patino  ######")

usuarios = []

try:  #### Ojo que igual no existe el archivo ######
  archivo = open("usuarios.bin",'rb')
  usuarios = pickle.load(archivo)
  archivo.close()
except:
  print("No existe archivo de datos")

while True:
  archivo = open("usuarios.bin",'wb')
  pickle.dump(usuarios,archivo)
  archivo.close()
  
  print("Escoge una opción:")
  print("1.-Insertar un usuario")
  print("2.-Listar usuarios")
  print("3.-Actualizar un usuario")
  print("4.-Eliminar un usuario")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    usuarios.append(Usuario(nombre,apellidos,email))
  elif opcion == 2:
    identificador = 0
    for usuario in usuarios:
      print("Este es el usuario con ID:",identificador)
      print(usuario.nombre,usuario.apellidos,usuario.email)
      identificador += 1
  elif opcion == 3:
    identificador = int(input("Introduce el id para modificar: "))
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    usuarios[identificador].nombre = nombre
    usuarios[identificador].apellidos = apellidos
    usuarios[identificador].email = email
  elif opcion == 4:
    identificador = int(input("Introduce el id para eliminar: "))
    confirmacion = input("¿Estás seguro? (S/N): ").lower()
    if confirmacion == "s":
      usuarios.pop(identificador)
    elif confirmacion == "n":
      print("Cancelado")
    else:
      print("Opción no válida")
  