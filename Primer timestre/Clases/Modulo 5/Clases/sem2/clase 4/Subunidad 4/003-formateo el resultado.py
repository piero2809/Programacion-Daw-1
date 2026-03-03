import os

carpeta = input ("indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos: 
    ruta = os.path.join(carpeta, elemento)
    print (elemento)
    print (os.path.getsize(ruta)/(1024*1024),"mb")
    print (os.path.getatime(ruta))