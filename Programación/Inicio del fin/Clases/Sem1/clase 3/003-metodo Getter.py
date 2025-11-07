class Gato ():
    def __init__ (self):
        self.color = "" #Esto es una propiedad

    def maulla(self): #Esto es un método (Una accion)
        return "miau"
    
    def setColor(self, nuevocolor): #Defino un setter - El método es el responsable de cambiar la propiedad
        self.color = nuevocolor #Se cambia la propiedad

    def getColor (self):
        #se ponen validaciones si asi se requiere
        return self.color





gato1 = Gato()
gato1.color = "naranja" #Seteamos una propiedad directamente (No es buena práctica)


gato1.setColor ( "naranja")

print (gato1.color) #Acceso directo, se uede pero no se recomienda
print (gato1.getColor()) #Acceso mediante método, se recomienda