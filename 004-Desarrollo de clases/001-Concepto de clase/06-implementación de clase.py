# Poco escalable - uso de muchas variables

contacto1_email = "info@empresa.com"
contacto1_direccion = "La calle de Jorge"
contacto1_nombre = "Jorge"
contacto1_apellidos = "Gomez"

contacto2_email = "info@empresa2.com"
contacto2_direccion = "La calle de Enrique"
contacto2_nombre = "Enrique"
contacto2_apellidos = "Gonzalez"

# Mucho mejor: uso de clases

class Contacto:
  def __init__(self):
    self.email = ""
    self.direccion = "" 
    self.nombre = ""
    self.apellidos = ""
    
contacto1 = Contacto()
contacto1.email = "info@empresa.com"
contacto1.direccion = "La calle de Jorge"
contacto1.nombre = "Jorge"
contacto1.apellidos = "Gomez"

contacto2 = Contacto()
contacto2.email = "info@empresa2.com"
contacto2.direccion = "La calle de Enrique"
contacto2.nombre = "Enrique"
contacto2.apellidos = "Gonzalez"