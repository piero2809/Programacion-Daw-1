import os

carpeta = input ("indica una carpeta: ")
grande = 1024*1024*1024  #1GB



for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        try:
            if os.path.getsize(ruta) >grande:
                print (ruta,os.path.getsize(ruta)/ (1024*1025), "MB")

        except:
            pass  # Evita errores si un archivo no se puede leer
  