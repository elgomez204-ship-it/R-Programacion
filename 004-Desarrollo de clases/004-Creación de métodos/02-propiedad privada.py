class Perro():
  def __init__(self):
    self.__color = "cafe"     # Esto es una propiedad privada (contrapuesta a pública)
    
perro1 = Perro()

print(perro1.__color)