class perro:
  def __init__(self):
    self.color = ""
    self.edad = 0
  def ladra(self):
    print("El perro está ladrando")
  
rocky = perro()
rocky.color = "cafe"
rocky.edad = 9
rocky.ladra()

luna = perro()
luna.color = "blanco"
luna.edad = 11
luna.ladra()