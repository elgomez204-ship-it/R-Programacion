# Las propiedades son como las variables PERO dentro de una clase

class Contacto():
  def __init__(self):
    self.nombre = ""
    self.edad = 0
    self.telefonos = []
    
# Ahora instancio un nuevo objeto
contacto1 = Contacto()

# Ahora le escribo una propiedad

contacto1.nombre = "Jorge"

print("El nombre del contacto es:",contacto1.nombre)

contacto1.telefonos.append("63354333")
contacto1.telefonos.append("65436456")

print(contacto1.telefonos)
    