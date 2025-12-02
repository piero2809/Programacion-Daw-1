#CRUD
#Create
#Read
#Update
#Delete

print ("Programa de gestión de cleintes v0.1 Piero Funes")

print ("Selecciona una opcion: ")
print ("1.- Insertar un cliente")
print ("2.- Listar clientes")
print ("3.- Actualizar clientes")
print ("4.- Eliminar clientes")

#le permito escoger una opción
opcion = input ("Escoge una opción")
opcion = int (opcion)


clientes = []           #creo una lista


while True:
    if opcion == 1:
        print ("Vamos a insertar un cliente")
    elif opcion == 2:
        print ("Vamos a ver los clientes")
    elif opcion == 3:
        print ("Vamos a actualizar un cliente")
    elif opcion == 4:
        print ("Vamos a eliminar un cliente")

    else:
        break