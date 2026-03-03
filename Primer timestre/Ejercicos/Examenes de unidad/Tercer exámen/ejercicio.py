'''
Hola a todos, actividades de final de unidad:

Unidad 4:

Actividad de final de unidad - Desarrollo de clases

1.-Crea una clase Cliente
2.-Añadele propiedades (nombre, apellidos, email, etc)
3.-Crea al menos un metodo set y un metodo get para una de las propiedades
4.-Crea un constructor con parametros (nombre, apellidos etc en la instanciación del objeto)
5.-Una vez creada la clase, crea tres instancias de la clase, cada una de ellas con sus propias propiedades
6.-Demuestra que los métodos set y get funcionan para cada una de las instancias

Rellena la actividad siguiendo la rubrica de evaluacion

'''


## Se define la clase cliente
class Cliente ():
    def __init__(self, nombre, apellidos, email ):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


    ##Setters
    def setNombre (self, nombrenuevo):
        self.nombre = nombrenuevo

    def setApellidos (self, apellidosnuevos):
        self.apellidos = apellidosnuevos

    def setEmail (self, emailnuevo):
        self.email = emailnuevo
    ##Getters

    def getNombre (self):
        return self.nombre

    def getApellidos (self):
        return self.apellidos

    def getEmail (self):
        return self.email
    


##Se crean las instancias

cliente1 = Cliente("Piero","Funes Larios", "pierofl2005@gmail.com")
cliente2 = Cliente("Sara","Monzó", "Sara@example.com")
cliente3 = Cliente("Zakaria","Kebour", "zaka@example.com")

##Se prueban los metodos set y get
print ("Antes del cambio:")
print (cliente1.getEmail())
cliente1.setEmail("Nuevo_pierofl2005@gmail.com")
print("Despues del cambio")
print (cliente1.getEmail())
