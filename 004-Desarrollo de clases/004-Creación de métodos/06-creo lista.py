class Usuario():
  # Este es el método constructor
  def __init__(self):
    self.nombrecompleto = ""
    self.email = ""
  # Estos son los setters y los getters
  def setNombreCompleto(self,nuevonombre):
    self.nombrecompleto = nuevonombre
  def setEmail(self,nuevoemail):
    self.email = nuevoemail
  def getNombreCompleto(self):
    return self.nombrecompleto
  def getEmail(self):
    return self.email
    
# CRUD - Create, Read, Update, Delete
# CRUD SQL - INSERT, SELECT, UPDATE, DELETE

usuarios = []             ############## Meto una lista de usuarios vacia

print("Gestor de usuarios v0.1 Juan Patino")
print("Selecciona una opción:")
print("1.-Insertar un nuevo usuario")
print("2.-Obtener listado de usuarios")
opcion = int(input("Indica tu opción (1,2): "))

if opcion == 1:     # Los SETTERS se usan en las operaciones de creación de nuevos elementos
  print("Voy a insertar un usuario")
  nuevousuario = Usuario()
  nombreusuario = input("Introduce el nombre del usuario: ")  # Tomo el dato
  nuevousuario.setNombreCompleto(nombreusuario) # Uso el metodo set para meter el dato en el objeto
  emailusuario = input("Introduce el email del usuario: ")  # Tomo el dato
  nuevousuario.setEmail(emailusuario) # Uso el metodo set para meter el dato en el objeto
  usuarios.append(nuevousuario) # Agrego el usuario a la lista
elif opcion == 2:   # Los GETTERS se usan en las operaciones de listado
    print("Saco el listado de usuarios")
    for usuario in usuarios:
      print("-------------------------")
      print("Nombre: ",usuario.getNombreCompleto())
      print("email: ",usuario.getEmail())
      print("-------------------------")