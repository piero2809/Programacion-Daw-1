import pickle as pk
agenda = []

while True:
    nombre = input ("Dime tu nombre: ")
    apellidos = input ("Dime tus apellidos: ")
    email = input ("Dime tu email: ")
    telefono = int (input ("Dime tu teléfono: "))
    #Añado a la agenda
    agenda.append([nombre,apellidos,email,telefono])
    print (agenda)    
    archivo = open ("agenda.bin", "wb")
    pk.dump(agenda, archivo)
    archivo.close()