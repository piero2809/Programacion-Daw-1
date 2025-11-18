
En el mundo de la programación, las excepciones son como los obstáculos que aparecen en el programa,el control de excepciones es una tecnica fundamental que nos permite manejar los problemas de manera eficiente.

Se empieza importando las librerias, luego se usa la libreria para asignar un numero aleatorio, luego se usan los while para iniciar el bloque, el ``try-except`` para manejar el flujo, se usa el bucle ``if`` para dar una pista y al final un bucle ``if`` para verificar si el usuario ha perdido o si adivinó el numero.

```
import random

numero_aleatorio = random.randint(1, 50)

intentos = 0
intentos_totales = 6



while intentos < intentos_totales:
    try:
        user = int(input("Introduce un número entre 1-50: "))
        
        if user < 1 or user > 50:
            print("Valor fuera de rango")
            continue
        
        intentos += 1  # Incrementamos después de un intento válido
        
        if user > numero_aleatorio:
            print("Número mayor que el número secreto")
        elif user < numero_aleatorio:
            print("Número menor que el número secreto")
        else:
            print(f"Has acertado el número. El número secreto era {numero_aleatorio}.")
            break

    except ValueError:
        print("Valor inválido, inténtalo de nuevo")
        continue

    if intentos  == 3 :
        if numero_aleatorio % 2 ==0:
            print ("PISTA: Es un numero par")
        else:
            print("PISTA: Es un numero inpar")


# Si se acaban los intentos y no se acertó
if intentos == intentos_totales and user != numero_aleatorio:
    print(f"Has perdido. El número secreto era: {numero_aleatorio}")



```

En resumen, el control de excepciones  sirve para mantener un programa estable ante imprevistos. Esto combinados con bucles, genera una herramienta poderosa para detectar errores y controlar la dirección del programa