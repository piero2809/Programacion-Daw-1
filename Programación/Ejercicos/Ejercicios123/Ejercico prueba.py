'''
Programa simulacro
v0.1 Piero Funes
'''

print ("Bienvenido al simulador de compra de ordenadores // v0.1 Piero Funes")





#Se definen las entradas y variables
nombredeldispostivo = str (input("Ingrese el nombre del dispositivo: "))
precio_base = int (input ("Ingrese el precio base del dispositivo: "))
almacenamiento_gb = int (input ("Ingrese el almacenamiento en GB del dispositivo: "))
peso_g = int (input ("Ingrese el peso en gramos del dispositivo: "))
pantalla_pulgadas = int (input ("Ingrese el tamaño de la pantalla en pulgadas del dispositivo: "))
presupuesto_max = int (input ("Ingrese el presupuesto máximo: ")) 
precio_total = 0

#Se definen las constantes
IVA = 0.21

#Calculos obligatorios
total_iva =  precio_base * IVA
precio_total = precio_base + total_iva
almacenamiento_mb = almacenamiento_gb * 1024
peso_kg = peso_g / 1000


#Se muestran los resultados
print ("\nEl dispositivo ", nombredeldispostivo, " \nTiene un precio base de", precio_base, "€")
print ("Tiene un IVA de ", total_iva, "€")
print ("El precio total es de ", precio_total, "€")
print ("Tiene un almacenamiento de ", almacenamiento_mb, "MB")
print ("Tiene un peso de ", peso_kg, "Kg\n")


#Se hacen los booleanos
if precio_total > presupuesto_max:
    print ("El precio total supera el presupuesto máximo.")
elif precio_total <= presupuesto_max:
    print ("Podemos seguir con la compra.\n")



if peso_kg < 1:
    print ("El dispositivo es ligero\n")
elif peso_kg >= 1:
    print ("El dispositivo es pesado\n")



if pantalla_pulgadas >= 6:
    print ("El dispositivo tiene una pantalla grande\n")
elif pantalla_pulgadas < 6:
    print ("El dispositivo tiene una pantalla pequeña\n")


