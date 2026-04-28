class Persona():
  def __init__(self,nombre,apellidos):
    self.nombre = nombre
    self.apellidos = apellidos
  def dameDatos(self):
    return self.nombre+self.apellidos

class Docente(Persona):
  def __init__(self,nombre,apellidos):
  	super().__init__(nombre, apellidos)
  
class Estudiante(Persona):
  def __init__(self,nombre,apellidos,email,direccion):
    super().__init__(nombre, apellidos)

    
estudiante1 = Estudiante("Juan","Patino")
print(estudiante1.dameDatos())

docente1 = Docente("Jorge","Gomez")
print(docente1.dameDatos())