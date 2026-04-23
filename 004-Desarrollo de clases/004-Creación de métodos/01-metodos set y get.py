class Perro():
  def __init__(self):
    self.color = ""     # Esto es una propiedad
  
  def maulla(self):     # Esto es un método (es una acción)
    return "guau guau"
    
  def setColor(self,nuevocolor):   # Defino un setter - el método es el responsable de cambiar la
    # Por ejemplo aquí podría validar si el color es un color válido para un gato
    self.color = nuevocolor         # Y cambio la propiedad
  
  def getColor(self):
    # Una vez más, aquí podría poner validaciones si lo quisiera
    return self.color
    
    
perro1 = Perro()
perro1.color = "cafe"   # Aquí seteamos una propiedad directamente (no es buena práctica)

perro1.setColor("cafe") # Esto es una práctica mucho mejor

print(perro1.color)      # Acceso directo, se puede pero no se recomienda

print(perro1.getColor()) # Acceso mediante método, se recomienda