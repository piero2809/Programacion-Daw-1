

En el mundo de la programación existen diferentes conceptos que son la base de un código, asi como las variables, las entradas, el tipo de dato y las constantes. En primer lugar, las variables, estas son pequeños contenedores de datos que almacenan un valor específico que puede ser cambiado con el tiempo. En segundo lugar, las entradas, son una forma de agregar datos a una variable pidiendola a la persona que ejecuta el programa. En tercer lugar, los tipos de datos son categorias que determinan el tipo de valor que pueden utilizar, estas tienen sus propios usos y restricciones. Por último, las constantes son variables, sin embargo estas son inmutables con el tiempo, es decir que no pueden cambiar su valor.  

Primero, hacemos el docstring, luego importamos las librerías, en este caso no es necesario. Luego se definen las variables y las entradas, se define la constante IVA (21%), luego se calcula con operadores matemáticos el IVA del producto y el precio total con IVA. Se imprimen los datos y por último se realizan los booleanos que a la vez imprimen datos.


## Se realiza la siguiente actividad:

El programa solicita al usuario el nombre, precio y cantidad en stock de un producto, calcula el precio con IVA aplicando un 21%, determina si el producto está disponible (cuando el stock es mayor que cero), muestra una alerta si el stock es bajo (menos de 5 unidades), y finalmente presenta todos los datos del producto en un solo párrafo informativo.



---
```

'''
Programa de registro de productos
v0.1 Piero Funes

'''

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

```
---


En resumen, este ejercicio remarca la importancia de los loelementos de un programa informático. Cada componente mencionado anteriormente cumple un papel crucial en el desarrollo de un programa siendo estos la base para aprender a programar.

