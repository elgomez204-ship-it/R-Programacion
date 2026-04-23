class Perro():
  def __init__(self,edad,nombre,raza):    # El constructor se ejecuta sí o sí
    self.edad = edad
    self.nombre = nombre
    self.raza = raza
    
  def ladra(self):     # El resto de métodos sólo se ejecutan si los llamas
    return "El perro está ladrando"
    
    
perro1 = Perro(5,"max","labrador")
