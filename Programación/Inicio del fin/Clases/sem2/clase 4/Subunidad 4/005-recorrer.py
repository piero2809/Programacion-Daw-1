import os

carpeta = input ("indica una carpeta: ")


for directorio,carpetas,archivo in os.walk (carpeta):
    print (directorio)
    print(carpetas)
    print (archivo)
   