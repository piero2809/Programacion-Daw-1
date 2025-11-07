class Gato ():
    def __init__ (self):
        self.color = "" #Esto es una propiedad

    def maulla(self): #Esto es un método (Una accion)
        return "miau"


gato1 = Gato()
gato1.color = "naranja" #Seteamos una propiedad
print (gato1.maulla) #Llamamos un método
