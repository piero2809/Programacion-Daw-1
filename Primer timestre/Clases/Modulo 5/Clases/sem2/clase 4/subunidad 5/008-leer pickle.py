import pickle

archivo = open("datos.bin","rb")

cadena = pickle.loads(archivo)
print (cadena)

archivo.close()