#CRUD
#Create
#Read
#Update
#Delete



class Cliente ():
    def __init__ (self):  
        self.email = None
        self.nombre = None
        self.direccion = None

print ("Programa de gestión de cleintes v0.1 Piero Funes")

print ("Selecciona una opcion: ")
print ("1.- Insertar un cliente")
print ("2.- Listar clientes")
print ("3.- Actualizar clientes")
print ("4.- Eliminar clientes")



clientes = []           #creo una lista


while True:

    #le permito escoger una opción
    opcion = input ("Escoge una opción")
    opcion = int (opcion)

    if opcion == 1:
        print ("Vamos a insertar un cliente")
        nuevocliente = Cliente() 
        nuevocliente.nombre = input ("introduce el nombre del cliente: ")
        nuevocliente.email = input ("introduce el email del cliente: ")
        nuevocliente.direccion = input ("introduce el direccion del cliente: ")
        clientes.append(nuevocliente)

    elif opcion == 2:
        print ("Vamos a ver los clientes")
        print (clientes)
    elif opcion == 3:
        print ("Vamos a actualizar un cliente")
    elif opcion == 4:
        print ("Vamos a eliminar un cliente")

    else:
        break