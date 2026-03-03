En Python, las estructuras de datos como listas, tuplas y diccionarios nos ayudan a organizar la información de manera clara y eficiente.
Este ejercicio ilustra el uso combinado de estas estructuras para representar datos relacionados con el baloncesto: equipos, jugadores y partidos.
Usaremos cada tipo de dato aprovechando sus puntos fuertes: listas para lo que puede cambiar, tuplas para lo que se mantiene fijo, y diccionarios para información más detallada.

El código utiliza tres estructuras fundamentales de Python:

1. **Lista (`equipos_basketball`)**: Guarda los nombres de los equipos. Como es una lista, podemos añadir nuevos equipos fácilmente usando `append()`.

2. **Tupla (`jugadores_favoritos`)**: Contiene los nombres de los jugadores. Al ser inmutable, nos asegura que esta lista no cambiará accidentalmente.

3. **Diccionario (`contacto_jugador`)**: Define las características de un jugador. Usamos `.get("edad")` para obtener el dato.

4. Finalmente, usamos una **lista de diccionarios (`agenda`)** para guardar varios partidos.

```python
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
```

En resumen, este ejercicio demuestra cómo elegir la estructura de datos adecuada simplifica nuestro código. Usar listas para datos dinámicos, tuplas para constantes y diccionarios para objetos estructurados es una práctica esencial en Python que hace que nuestros programas sean más robustos y fáciles de entender.
