import os

carpeta = input ("indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos: 
    ruta = os.path.join(carpeta, elemento)
    print (elemento)
    print (os.path.getsize(ruta))
    print (os.path.getatime(ruta))