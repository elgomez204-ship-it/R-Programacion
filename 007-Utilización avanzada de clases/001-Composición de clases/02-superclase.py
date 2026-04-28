class Persona():
  def __init__(self,nombre,apellidos,email,direccion):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    self.direccion = direccion
  def dameDatos(self):
    return self.nombre+self.apellidos

class Docente(Persona):
  def __init__(self,nombre,apellidos,email,direccion):
  	super().__init__(nombre, apellidos, email,direccion)
  
class Estudiante(Persona):
  def __init__(self,nombre,apellidos,email,direccion):
    super().__init__(nombre, apellidos, email,direccion)
  
    
estudiante1 = Estudiante("Juan","Patino","juan@empresa.com","Direccion")
print(estudiante1.dameDatos())

docente1 = Docente("Jorge","Gomez","jorge@empresa.com","Direccion")
print(docente1.dameDatos())