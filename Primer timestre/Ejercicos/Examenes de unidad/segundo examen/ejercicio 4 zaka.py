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
