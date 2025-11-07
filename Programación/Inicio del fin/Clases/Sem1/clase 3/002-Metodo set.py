class Gato ():
    def __init__ (self):
        self.color = "" #Esto es una propiedad

    def maulla(self): #Esto es un método (Una accion)
        return "miau"
    
    def setColor(self, nuevocolor): #Defino un setter - El método es el responsable de cambiar la propiedad
        self.color = nuevocolor #Se cambia la propiedad


gato1 = Gato()
gato1.color = "naranja" #Seteamos una propiedad directamente (No es buena práctica)



gato1.setColor ( "naranja")