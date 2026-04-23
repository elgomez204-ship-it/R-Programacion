# Las propiedades son como las variables PERO dentro de una clase

class Contacto():
  def __init__(self):
    self.nombre = ""
    self.edad = 0
    self.telefonos = ['6543534','75345345']
    
# Ahora instancio un nuevo objeto
contacto1 = Contacto()

# Ahora le escribo una propiedad

contacto1.nombre = "Jorge"

print(contacto1.nombre)