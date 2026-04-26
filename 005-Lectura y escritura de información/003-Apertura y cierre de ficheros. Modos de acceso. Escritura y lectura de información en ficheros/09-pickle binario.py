import pickle

class Cliente():
  def __init__(self,nuevonombre,nuevoemail):
    self.nombre = nuevonombre
    self.email = nuevoemail

clientes = []

clientes.append(Cliente("Enrique","enrique@empresa.com"))
clientes.append(Cliente("Juan","juan@empresa.com"))

archivo = open("clientes.bin","wb")
pickle.dump(clientes,archivo)
archivo.close()