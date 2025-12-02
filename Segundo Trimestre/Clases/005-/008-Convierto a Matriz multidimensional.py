archivo = open ("C:\\Users\\PIEROGABRIELFUNESLAR\\OneDrive - INSTITUTO SUPERIOR DE FORMACION PROFESIONAL CEAC FP\\Escritorio\\Piero Daw 1\\Programacion-Daw-1\\Segundo Trimestre\\Clases\\005-\\clientes.csv", "r")

lineas = archivo.readlines()

conjunto_datos = []

for linea in lineas:
    partido = linea.split (",")
    conjunto_datos.append(partido)
    
print(conjunto_datos)