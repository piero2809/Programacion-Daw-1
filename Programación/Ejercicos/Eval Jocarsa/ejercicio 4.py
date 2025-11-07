
ruta = "C:\\Users\\PIEROGABRIELFUNESLAR\\OneDrive - INSTITUTO SUPERIOR DE FORMACION PROFESIONAL CEAC FP\\Escritorio\\Piero Daw 1\\Programación\\Ejercicos\\Eval Jocarsa\\jugadores.txt"

archivo = open(ruta,'r')

contenido  = archivo.readlines()


print(contenido)

archivo.close()