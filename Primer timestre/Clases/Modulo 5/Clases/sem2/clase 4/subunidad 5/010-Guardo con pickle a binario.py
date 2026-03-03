import pickle


class Cliente ():
    def __init__ (self, nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail


clientes = []

clientes.append(Cliente("Piero Funes", "piero@gmial.com"))
clientes.append(Cliente("Sara Monzo", "Sara@gmial.com"))


archivo = open("clientes.bin","wb")
pickle.dump(clientes, archivo)
archivo.close()