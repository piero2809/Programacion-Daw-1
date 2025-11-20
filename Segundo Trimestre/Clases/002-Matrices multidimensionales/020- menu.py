import pickle as pk
juego = []

while True:
    print ("Opciones:")
    print ("1.-Introducir nuevo juego")
    print ("2.-Listar juegos en el portafolio")
    print ("3.-Guardar en archivo")
    print ("4.-Cargar datos de archivo")
    print ("5.-Eliminar datos")
    opcion = int(input ("Selecciona una opcion: "))
    
    if opcion ==1:
        nombre = input ("Introduce el nombre del juego: ")
        categoria = input ("Introduce la categorìa")
        juego.append((nombre, categoria))
    elif opcion ==2:
        print ("Tus juegos registrados hasta el momento son:")
        for elemento in juego:
            print (elemento)
    elif opcion == 3:
        archivo = open("juegos.bin", "wb")           #Write Binary
        pk.dump(juego, archivo)
        archivo.close()
        print ("¡Se ha guardado con éxito✅✅!.")
    elif opcion == 4:
        archivo = open ("juegos.bin", "rb")
        juego =pk.load (archivo)                     #Volcamos el archivo en la lista
        archivo.close()
        print ("Se ha cargado el archivo con exito✅✅")    
    elif opcion == 5:
            identificador = int(input("Introduce el id para eliminar: "))
            confirmacion = input("¿Estás seguro? (S/N): ").lower()
            if confirmacion == "s":
                juego.pop(identificador)
            elif confirmacion == "n":
                print("Cancelado")
            else:
                print("Opción no válida")