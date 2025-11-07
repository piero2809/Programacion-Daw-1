import os

carpeta = input ("indica una carpeta: ")
grande = 1024*1024*1024  #1GB



mapa = open("mapa.txt","a")

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        mapa.write (str(ruta+"\n"))

mapa.close()
