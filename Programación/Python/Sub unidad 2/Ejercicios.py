

'''
Programa calculadora de IVA
v0.1 Piero Funes 2025

'''

#Define IVA

iva = 0.21

#Toma entradas
nombre = input("Introduce el nombre: ")
precio_base = input ("Introduce el precio de venta al publico: ")
almacenamiento_gb = input ("introduce la capacidad del dispositivo: ")
peso_g = input ("Introduce el peso en gramos: ")
pantalla_pulgadas = input ("Introduce el tamaño de la pantalla en pulgadas: ")

#Convierte tipos
precio_base = int(precio_base) #conversion explícita
almacenamiento_gb = int(almacenamiento_gb) #conversión implícita
peso_g = int(peso_g)
pantalla_pulgadas = pantalla_pulgadas*1

#Calcula
total_iva = precio_base*iva
precio_total = precio_base+ total_iva
almacenamiento_mb = almacenamiento_gb *1024
peso_kg = peso_g / 1000


#Compara sin IF
presupuesto_max = 800.0
excede_presupuesto = precio_total > presupuesto_max
print (excede_presupuesto)

#Salida

print ("El nombre del producto es: ", nombre)
print ("el precio base del producto es: ", precio_base)
print ("La capacidad de almacenamiento es: ",almacenamiento_gb)
print ("El peso del producto es: ",peso_g)


print ("El total del iva es: ",total_iva)
print ("El precio total es: ",precio_total)
print ("La cantidad de almacenamiento en MB es: ", almacenamiento_mb)
print ("El total del peso en KG: ", peso_kg)
print ("El máximo de presupuesto es: ",presupuesto_max)
print ("Excede presupuesto: ", excede_presupuesto)
