class CuentaBancaria ():
    def __init__ (self):
        self.__saldo = 0
        self.__cliente = ""
    
#Defino setters y getters para el saldo
    def setSaldo (self,nuevosaldo):
        self.__saldo = nuevosaldo
        if nuevosaldo > self.__saldo +1000:
            print ("Voy a avisar a la entidad de un ingreso muy grande")

        else:
            self.__saldo = nuevosaldo


    def getSaldo(self):
        return self.__saldo


cuentaCliente1 = CuentaBancaria()
cuentaCliente1.setSaldo (1000000)
print (cuentaCliente1.getSaldo())
