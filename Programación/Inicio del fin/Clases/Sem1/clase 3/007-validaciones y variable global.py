Limitediferenciasaldo=1000


class CuentaBancaria ():
    def __init__ (self):
        self.__saldo = 0
        self.__cliente = ""
    
#Defino setters y getters para el saldo
    def setSaldo (self,nuevosaldo):
       #Establezco una condicion de que valida si el saldo es mayor a 1000 euros
        if nuevosaldo > self.__saldo + Limitediferenciasaldo:
            #Si salta la alarma, avisa y no cambia el saldo
            print ("Voy a avisar a la entidad de un ingreso muy grande")
        else:
            #Si pasa el filtro, solo entoces se cambia el saldo
            self.__saldo = nuevosaldo


    def getSaldo(self):
        return self.__saldo


cuentaCliente1 = CuentaBancaria()
cuentaCliente1.setSaldo (1000000)
print (cuentaCliente1.getSaldo())
