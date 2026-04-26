class Usuario():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de usuarios v0.1 ######")
print("####### Juan Patino  ######")

usuarios = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un usuario")
  print("2.-Listar usuarios")
  print("3.-Actualizar un usuario")
  print("4.-Eliminar un usuario")
  opcion = int(input("Escoge una opcion: "))