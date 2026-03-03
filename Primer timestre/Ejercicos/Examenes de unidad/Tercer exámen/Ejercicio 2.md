En el mundo de la programación, la lectura y escritura de información son fundamentales para cualquier aplicación. Gracias al manejo de ficheros, un programa puede almacenar datos permanentemente, incluso después de finalizarlo; luego puede leer estos archivos para utilizar los datos guardados. Esto es ùtil para aplicaciones de inventario, gestores de usuarios, etc.


Python permite usar archivos con la función `open()`

- `"r"` → leer  
- `"w"` → escribir sobrescribiendo el contenido  
- `"a"` → añadir al final del archivo  
- `"rb"` → leer binario  
- `"wb"` → escribir binario


Para almacenar los datos se usa la librería pickle.

## A continuación se realiza el ejercicio.


```
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
    


##Se intenta abrir el archivo, si no existe crea la lista clientes vacía
try:
    archivo = open(ruta_deseada, "rb")
    clientes = pick.load(archivo)
    archivo.close()
except :    
    clientes = []


## Se hace el gestor CRUD
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
        
```

En conclusión, el manejo de archivos es un aspecto esencial en programación, ya que permite guardar y recuperar datos de forma permanente. La lectura y escritura de información hacen posible desarrollar aplicaciones reales como agendas, sistemas de clientes o inventarios, relacionando la teoría de los ficheros con los objetos en Python.