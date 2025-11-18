#Las propiedades son como las variables PERO dentro de una clase

class Cliente ():
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = []
            
#Instancio un nuevo objeto

cliente1 = Cliente()

cliente1.nombre = "Piero Funes"

print ("El nombre del cliente es:", cliente1.nombre)

cliente1.telefonos.append ("1254624524")
cliente1.telefonos.append ("6267427742")

print (cliente1.telefonos)