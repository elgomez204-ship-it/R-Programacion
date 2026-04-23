class Perro():
  def __init__(self):    # El constructor se ejecuta sí o sí
    self.edad = 0
    
  def ladra(self):     # El resto de métodos sólo se ejecutan si los llamas
    return "El perro está ladrando"

perro1 = Perro()
print(perro1.edad)
perro1.edad = 5
print(perro1.edad)

print(perro1.ladra())
    
    