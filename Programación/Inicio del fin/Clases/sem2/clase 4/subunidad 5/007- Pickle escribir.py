import pickle

archivo = open("datos.bin","wb")
cadena = "Piero Funes"

pickle.dump(cadena, archivo)

archivo.close()