class Cliente():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


print ("---Gestión de clientes v0.1---")
print ("---------Piero Funes----------")

clientes = []

while True:
    print ("Selecciona una opcion: ")
    print ("1.- Insertar un cliente")
    print ("2.- Listar clientes")
    print ("3.- Actualizar clientes")
    print ("4.- Eliminar clientes")
    opcion = int(input("Escoge una opción"))

    if opcion == 1:
        nombre =  input ("Introduce el nombre: ")
        apellidos = input ("Introduce los apellidos:")
        email = input ("Introduce el email: ")
        clientes.append (Cliente(nombre, apellidos,email))

    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print ("Este es el cliente con ID: ", identificador)
            print (cliente.nombre,cliente.apellidos,cliente.email)
            identificador +=1
    elif opcion ==3:
        identificador =int (input("Introduce el ID para modificar"))
        
        nombre =  input ("Introduce el nombre: ")
        apellidos = input ("Introduce los apellidos:")
        email = input ("Introduce el email: ")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellidos = apellidos
        clientes[identificador].email = email

    elif opcion == 4:
        identificador =  int(input("Introduce el ID para eliminar"))
        confirmacion =  (input ("Estas seguro? (S/N)")).lower
        if confirmacion == "s" :
            clientes.pop (identificador)
        elif confirmacion == "n":
            print ("Cancelado")
        else:
            print ("Opcion no valida")