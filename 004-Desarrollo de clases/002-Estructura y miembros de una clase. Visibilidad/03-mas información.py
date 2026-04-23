# Declaramos una clase
class Contacto():
  def __init__(self):
    self.email = None
    self.nombre = None
    self.direccion = None
    
# Usamos la clase instanciando en un objeto
contacto1 = Contacto()
contacto1.email = input("Introduce el email del contacto: ")
contacto1.nombre = input("Introduce el nombre del contacto: ")
contacto1.direccion = input("Introduce la direccion del contacto: ")

print(contacto1)
print(contacto1.email)
print(contacto1.nombre)
print(contacto1.direccion)
