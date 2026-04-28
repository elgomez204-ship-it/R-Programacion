class Persona():
  def __init__(self,nombre,apellidos):
    self.nombre = nombre
    self.apellidos = apellidos
  def dameDatos(self):
    return self.nombre+self.apellidos

class Docente(Persona):
  def __init__(self,nombre,apellidos):
  	super().__init__(nombre, apellidos)
  def dameDatos(self):
    return "Docente: "+self.nombre+" "+self.apellidos
  
class Estudiante(Persona):
  def __init__(self,nombre,apellidos):
    super().__init__(nombre, apellidos)
  def dameDatos(self):
    return "Estudiante: "+self.nombre+" "+self.apellidos

    
estudiante1 = Estudiante("Juan","Patino")
print(estudiante1.dameDatos())

docente1 = Docente("Jorge","Gomez")
print(docente1.dameDatos())