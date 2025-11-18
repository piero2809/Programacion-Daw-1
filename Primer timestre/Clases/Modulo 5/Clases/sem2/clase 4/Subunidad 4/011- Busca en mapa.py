archivo =  open ("mapa.txt", "r") #READ

lineas = archivo.readlines()

for linea in lineas:
    if "css" in linea:
        print ("####################################################")
        print ("Encontrado!: ", linea)
