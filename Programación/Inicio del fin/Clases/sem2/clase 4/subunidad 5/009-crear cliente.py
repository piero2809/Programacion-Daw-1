class Cliente ():
    def __init__ (self, nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail


clientes = []

clientes.append(Cliente("Piero Funes", "piero@gmial.com"))
clientes.append(Cliente("Sara Monzo", "Sara@gmial.com"))

print (clientes)