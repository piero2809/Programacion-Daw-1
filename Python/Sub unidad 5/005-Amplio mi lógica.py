def divide (divisor,dividendo):
    try:                                    ##Intenta
        dividendo = int (dividendo)         ##1 Convertir dividendo a entero
        divisor = int (divisor)             ##Convertir divisor a entero
        if divisor !=0:                     ##Y ahora compureba si el divisor no es igual a 0
            return dividendo/divisor        ##Si hasta aqui no has dado fallo, devuelve la división
        else:                               ##y si el divisor es 0
            return "Infinito"                    ##Devuelve infinidad
    except:                                 ##Si algo de todo lo anterior ha dado error
        return "Error per no es fatal"      ##Devuelve el mensaje de error limpio
    
##! Es igual a la negación 

    
for divisor in range (-100,100):
    for dividendo in range (-100,100):
        print (divide(divisor,dividendo))


print (divide(4,"a"))