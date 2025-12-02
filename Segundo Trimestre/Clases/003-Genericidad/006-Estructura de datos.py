numeros = [1,2,"3",4,"cinco"]

print (numeros)
numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco"]
def calculaDoble():
    for numero in numeros:
       try:                                     #Se intenta convertir
           numero = int (numero)
           print (numero*2)
       except:                                  #Si no puedes
           #Intenta buscar el valor de la lista de numeros,
        for i in range (0,len (numeros_etiquetas)):
            if numero == numeros_etiquetas[i]:
                print (i*2)    
            
calculaDoble()