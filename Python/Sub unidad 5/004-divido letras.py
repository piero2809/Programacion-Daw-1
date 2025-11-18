def divide (dividendo,divisor):
    if divisor !=0:
        return dividendo/divisor
    else:
        return False
        
for divisor in range (-100,100):
    for dividendo in range (-100,100):
        print (divide(4,2))


print (divide(4,"a"))