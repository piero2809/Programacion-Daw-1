import os

carpeta = input ("indica una carpeta: ")

elementos = os.listdir(carpeta)

suma = 0

for elemento in elementos: 
    ruta = os.path.join(carpeta, elemento)
    suma += os.path.getsize(ruta)

print ("la carpeta ocupa: ")
print (suma/(1024*1024), "MB")
    
