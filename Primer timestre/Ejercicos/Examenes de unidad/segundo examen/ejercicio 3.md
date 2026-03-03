
En el mundo de la programación, las estructuras de control son como las bases fundamentales para proporcionar lógica y direccion al codigo, existen estructuras condicionales(``if``,``elif``,``else``), de repeticion (``for``,``while``)y de salto(``break``, ``continue``).


Primero se importan librerias necearias, se inician los bucles y la entrada de datos, se hacen los bucles ```while`` para validar las condiciones, se hacen los calculos, se formatean las fechas y se imprimen los datos


```
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
```

En resumen, las estructuras de control son super importante ya que  permiten decidir, repetir y ajustar el flujo del programa para que el código sea dinámico y eficiente, en este caso se usaron todas las estructuras tanto de salto, condicionales y repeticion.