'''
Programa de registro de productos
v0.1 Piero Funes

'''
#No se importa ninguna libreria por que no se requiere


print ("Bienvenido al programa de registro de productos // v0.1 Piero Funes\n\n")


#Se definen variables y entradas
nombre = str (input("Ingrese el nombre del producto: "))
precio_base =  float(input ("Ingrese el precio del producto: "))
cantidad = int (input ("ingrese el stock del producto: "))

#Se definen constantes
IVA = 0.21
#Se hacen el calculo del IVA y el precio final
total_iva = precio_base * IVA
precio_final = precio_base + total_iva

#Se hacen los prints de los datos
print ("\nEl producto ", nombre, "tiene un precio base de ", precio_base, "€")
print ("El IVA del producto es de ", total_iva, "€")
print ("El precio final del producto es de ", precio_final, "€\n")



#Se realizan los booleanos
if cantidad > 0:
    print ("Si hay stock del producto ", nombre, "\nLa cantidad de stock es de ", cantidad, "unidades")

if cantidad > 0 and cantidad <= 5:
    print ("!!!El stock del producto ", nombre, "es bajo!!!, solo quedan ", cantidad, "unidades")
elif cantidad == 0 or cantidad < 0:
    print ("No hay stock del producto ", nombre)


print ("\nGracias por usar el programa de registro de productos, vuelva pronto.")
