import os

carpeta = input ("indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos: 
    print (elemento)