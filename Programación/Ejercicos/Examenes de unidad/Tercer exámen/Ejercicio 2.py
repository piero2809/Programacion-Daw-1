'''


Unidad 5:

Ejercicio de final de unidad

-Crea una mini-aplicacion CRUD
-Crea una mini-clase de Cliente, solo con propiedades, sin métodos
-Crea una lista vacia de clientes
-Ofrece un menu, en el que el usuario podrá, crear clientes, o listar los clientes existentes (dentro de un bucle infinito while, atrapa los dos casos con if-elif)
-Utiliza la librería pickle para guardar la lista de clientes cada vez que se crea uno
-Utiliza la libreria pickle para abrir los clientes, si existen, al abrir la aplicación (es recomendable introducir ese intento de lectura en un try-except)


'''
import pickle as pick
ruta_deseada = "C:\\Users\\PIEROGABRIELFUNESLAR\\OneDrive - INSTITUTO SUPERIOR DE FORMACION PROFESIONAL CEAC FP\\Escritorio\\Piero Daw 1\\Programación\\Examenes de unidad\\Tercer exámen\\clientes.bin"


## Se define la clase cliente
class Cliente ():
    def __init__(self):
        self.nombre = ""
        self.email =""


    ##Setters
    def setNombreCompleto(self, nombrenuevo):
        self.nombre = nombrenuevo

    def setEmail(self, emailnuevo):
        self.email = emailnuevo
    ##Getters

    def getNombreCompleto(self):
        return self.nombre

    def getEmail(self):
        return self.email
    



try:
    archivo = open(ruta_deseada, "rb")
    clientes = pick.load(archivo)
    archivo.close()
except :    
    clientes = []



print ("Gestor de clientes Piero Funes v0.2")
while True:
    print ("Selecciona una opción")
    print ("1.- Insertar un nuevo cliente")
    print ("2.-Listar a los clientes")
    opcion = int (input("Indica tu opción (1,2): "))

    if opcion == 1:
        print ("Vamos a ingresar un cliente: ")
        nuevocliente = Cliente()
        nombrecliente = input ("Introduce el nombre del cliente: ")
        nuevocliente.setNombreCompleto (nombrecliente)
        emailcliente = input ("Introduce el email del cliente: ")
        nuevocliente.setEmail(emailcliente)
        clientes.append (nuevocliente)

        try:
            archivo = open (ruta_deseada, "wb")
            pick.dump(clientes, archivo)
            archivo.close()
        except:
            pass


    elif opcion == 2:
        print ("Vamos a listar a los clientes: ")
        for cliente in clientes:
            print ("-------------------------")
            print ("Nombre: ", cliente.getNombreCompleto())
            print ("Email: ", cliente.getEmail())
            print ("--------------------------")
        


