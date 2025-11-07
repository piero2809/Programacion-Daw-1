'''
Aplicacioón de gestión de productos
(c) 2025 Piero Funes 
Esta aplicación gestiona productos
'''


#En esta aplicacion no se importan librerías

#Definimos clases y funciones

class Producto ():
    def __init__ (self):
        self.nombre = ""
        self.precio = 0

#Creamos variables globales

productos = []

#Primero lanzamos un mensaje de bienvenida

print ("Gestor de productos v0.1 Piero Funes ")

#Le mostramos al usuario las opciones que ti
print ("Selecciona una opción: ")
print ("1.-Crear un nuevo producto" )
print ("2.-Listar productos")
print ("3.-Actualizar productos")
print ("4.- Eliminar productos")

opcion = int (input ("Escoge tu opción: "))
while True:
    #En función de la opcion que coja el usario
    if opcion == 1:
        #o bien creamos un nuevo producto 
        print ("Creamos un nuevo producto")
        producto = Producto()
        producto.nombre = input ("Introduce el nombre del producto")
        producto.precio = input ("Introduce el precio del producto")
        productos.append (producto)
        #o bien listamos los productos
    elif opcion == 2:
        print ("Vamos a listar los productos")
        print (productos)
        #o bien actualizamos los productos
    elif opcion ==3:
        print ("Vamos a actualizar los productos")
    
        #o bien eliminamos los productos
    elif opcion == 4: 
        print ("Vamos a elminar productos")
    
    else:
        break
    #Volvemos a repetir

