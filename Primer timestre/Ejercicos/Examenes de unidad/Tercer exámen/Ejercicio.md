
En el extenso mundo de la programación enfocada a objetos, las clases son los bloques fundamentales para la construcción de un codigo. Son estructuras que agrupan variables y métodos relacionados.


Una clase en Python está compuesta por:

- **Atributos** → características del objeto
- **Métodos** → funciones que pueden usar o modificar atributos
- **Constructor** → método especial `__init__` que se ejecuta al crear un objeto

primero se define el nombre d ela clase
- `self` que permite acceder a los atributos del objeto

- Los métodos *setter* y *getter* que permiten cambiar y consultar los valores respectivamente. A esto se le llama encapsulación

A continuacion se realiza el ejercicio propuesto.

```

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
```


Señalar errores comunes y cómo evitarlos.

En conclusión, Las clases son herramientas esenciales en la programacion permitiendo organizar el codigo de manera eficiente. Con ellas podemos crear múltiples objetos cada uno con sus propios datos. 