class Docente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

class Estudiante():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    
estudiante1 = Estudiante("Juan","Patino","juan@empresa.com")
print(estudiante1)

docente1 = Docente("Jorge","Gomez","jorgre@empresa.com")
print(docente1)