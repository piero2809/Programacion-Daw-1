class Cliente():
    #Este es el método constructor
    def __init__ (self):
        self.nombrecompleto = ""
        self.email = ""
#Estos son los setters 
    def setNombreCompleto (self, nuevonombre):
        self.nombrecompleto = nuevonombre
    
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
#------------------------------
# Estos son los getters
    def getNombreCompleto (self):
        return self.nombrecompleto
   
    def getEmail (self):
        return self.email
    

#CRUD - Create, Read, Update, Delete
#CRUD SQL - Insert, Select, Update, Delete

clientes = []   ### Creo una lista de clientes vacía

print ("Gestor de clientes v0.1 Piero Funes")
while True:
    print ("Selecciona una opción")
    print ("1.- Insertar un nuevo cliente:")
    print ("2.- Obtener el listado de clientes")
    opcion = int (input ("Indica tu opción (1,2): "))



    if opcion == 1 :
        print ("voy a insertar un cliente")
        nuevocliente = Cliente()
        nombrecliente = input ("introduce el nombre del cliente: ") #Tomo el dato
        nuevocliente.setNombreCompleto (nombrecliente) #Uso el setter para meter el dato en el objeto
        emailcliente = input ("Introduce el email del cliente: ")
        nuevocliente.setEmail(emailcliente)
        clientes.append(nuevocliente)

    elif opcion == 2 : ##Los getters se  usan en las operaciones de lsitado
        print ("Saco el listado de clientes")
        for cliente  in clientes:
            print ("------------------------")
            print ("Nombre: ", cliente.getNombreCompleto())
            print ("Email: ",cliente.getEmail())
            print ("------------------------")