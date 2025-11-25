datos = "uno,dos,tres,cuatro,cinco,seis"

# Primero imprimo la cadena
print("Datos",datos)
# Ahora la parto
partido = datos.split(",")
# Ahora imprimo el partido
print("Datos partidos:",partido)
# Ahora quiero unirlo todo de nuevo
nueva_cadena = "|".join(partido)
print("nueva cadena:", nueva_cadena)