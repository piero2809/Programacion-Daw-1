# Lista
equipos_basketball = ['Los Angeles Lakers', 'Golden State Warriors', 'Boston Celtics']

# Metodo append()
equipos_basketball.append('Miami Heat')

# Tupla
jugadores_favoritos = ('LeBron James', 'Kevin Durant')

#Diccionario
contacto_jugador = {
    "nombre": "LeBron",
    "apellidos": "James",
    "email": "lebron.james@example.com",
    "edad": 38
}

# Metodo get()
edad_jugador = contacto_jugador.get("edad")


#Lista de diccionarios
agenda = [
    {
        "fecha": "2023-10-05",
        "equipo_local": "Los Angeles Lakers",
        "equipo_visitante": "Golden State Warriors",
        "resultado": "110-98"
    },
    {
        "fecha": "2023-10-12",
        "equipo_local": "Boston Celtics",
        "equipo_visitante": "Los Angeles Lakers",
        "resultado": "105-97"
    }
]

# Se imprime en pantalla los siguientes datos:
print("Nombre completo:", contacto_jugador['nombre'], contacto_jugador['apellidos'])
print("Edad:", edad_jugador)
print("Resultado del primer juego:", agenda[0]['resultado'])
