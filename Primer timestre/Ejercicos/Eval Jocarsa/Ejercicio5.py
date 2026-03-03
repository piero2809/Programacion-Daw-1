class Jugador():
    def __init__(self, nombre, edad, posicion, equipo):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo

print ("---Gestión de Jugadores v0.1---")
print ("---------Piero Funes----------")

Jugadores = []

while True:
    print ("Selecciona una opcion: ")
    print ("1.- Insertar un Jugador")
    print ("2.- Listar Jugadores")
    print ("3.- Actualizar Jugadores")
    print ("4.- Eliminar Jugadores")
    opcion = int(input("Escoge una opción: "))

    if opcion == 1:
        nombre =  input ("Introduce el nombre: ")
        edad = input ("Introduce la edad:")
        posicion = input ("Introduce la posicion: ")
        equipo = input ("Introduce el equipo: ")
        Jugadores.append(Jugador(nombre,edad,posicion,equipo))

    elif opcion == 2:
        identificador = 0
        for Jugador in Jugadores:
            print ("Este es el Jugador con ID: ", identificador)
            print (Jugador.nombre,Jugador.edad,Jugador.posicion, Jugador.equipo)
            identificador +=1
    elif opcion ==3:
        identificador =int (input("Introduce el ID para modificar"))
        
        nombre =  input ("Introduce el nombre: ")
        edad = input ("Introduce los edad:")
        posicion = input ("Introduce el posicion: ")
        equipo = input ("Introduce el equipo: ")
        Jugadores[identificador].nombre = nombre
        Jugadores[identificador].edad = edad
        Jugadores[identificador].posicion = posicion
        Jugadores[identificador].equipo = equipo

    elif opcion == 4:
        identificador =  int(input("Introduce el ID para eliminar"))
        confirmacion =  (input ("Estas seguro? (S/N)")).lower()
        if confirmacion == "s" :
            Jugadores.pop (identificador)
        elif confirmacion == "n":
            print ("Cancelado")
        else:
            print ("Opcion no valida")