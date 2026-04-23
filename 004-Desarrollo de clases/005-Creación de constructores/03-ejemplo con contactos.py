class Contacto():
  def __init__(self,nombre,apellidos,email,direccion):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    self.direccion = direccion
 
contactos = []
while True:  
 
  nombre = input("Introduce el nombre del contacto: ")
  apellidos = input("Introduce los apellidos del contacto: ")
  email = input("Introduce el email del contacto: ")
  direccion = input("Introduce la dirección del contacto: ")

  contactos.append(Contacto(nombre,apellidos,email,direccion))
