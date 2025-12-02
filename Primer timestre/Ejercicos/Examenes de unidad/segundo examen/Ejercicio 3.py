##Se importan librerías
import math 
import datetime as fechas



## Validaciones y entrada de datos

while True:
    caballos= int(input("Ingrese el numero de caballos: "))
    capacidad_por_cuadra = int (input("ingrese la capacidad por cuadra del caballo: "))
    if caballos > 0 and capacidad_por_cuadra > 0:
        break
    else:
        print ("Lo valores tienen que ser mayor que 0, Intenta de nuevo")
   
##Validacion de fechas
while True:
    dia = int (input("Introduce el dia: "))
    if dia <= 30  or dia >= 1:
        break
    else:
        print ("No puede ser un dia invalido")
       
   

while True:
    mes = int (input("Introduce el mes en números"))
    if mes >= 1 and mes <=12:
        break
    else:
        print ("No puede ser un mes invalido")
   
año = int (input ("dime el año"))
##Calculos
cuadras_necesarias = math.ceil(caballos / capacidad_por_cuadra)

##Calcula las fechas.
dates = fechas.date(año , mes, dia)



##Salida

print ("#################################################################################")
print ("hay",caballos," caballos en total:")
print("cada cuadra tiene de capacidad",capacidad_por_cuadra,"caballos")
print ("Se necesitan",cuadras_necesarias,"cuadras.")
print (dates)
print ("Fecha Formateada:",dates.day,"/", dates.month,"/", dates.year,"\nWeekday:", dates.weekday(),"\n" "ISOweekday: ", dates.isoweekday())

print ("#################################################################################")