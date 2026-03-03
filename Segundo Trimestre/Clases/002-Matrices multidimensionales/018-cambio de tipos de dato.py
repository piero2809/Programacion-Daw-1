tupla = ('manzanas','peras','platanos')
#Necesito meter una fruta mas
print (tupla)
lista =list(tupla) #Convierto una tupla en una lista
print(lista)
lista.append("fresas")

#Ahora se vuelve a tupla

nueva_tupla = tuple(lista)
print(nueva_tupla)