import random

secreto= random.randint(1,50)

intentos = 6



assert intentos>= 0, "El contador no puede ser negativo "
assert 1<=secreto<=50, "El numero tiene que estar en el rango"

while intentos > 0:
    user =input("Intento",intentos - 5,"ingresa un numero: ")
    ##Verificacion si es un entero
    try:
        int(user)
    except:
        print("entrada invalida, escribe un entero")
        continue

    ##verificacion si el numero esta entre 1 y 50
    if user< 1 and user >50:
        print("numero invalido")
        continue


    intentos -= 1


    if user == secreto:
        print ("!!Correcto, el numero si es :",secreto)
        break
    elif user <secreto:
        print ("Numero demasiado bajo")
    elif user > secreto:
        print ("Numero demasiado alto")


    if intentos  == 3 :
        if secreto % 2 ==0:
            print ("PISTA: Es un numero par")
        else:
            print("PISTA: Es un numero inpar")


if user != secreto and intentos ==0:
    print("has perdido el numero era",secreto)

    




