En Python, las estructuras de datos nos vienen genial para organizar info real de forma clara. En este ejercicio vamos a usar una **lista de diccionarios** para montar una agenda de contactos sencilla, donde cada entrada tiene nombre, apellido y correo.

Empezamos con una lista vacía `agenda`.
Usando `append()`, vamos añadiendo diccionarios, donde cada uno es un contacto con sus claves correspondientes: `"nombre"`, `"apellido"` y `"correo"`.
Al final, un `print(agenda)` nos deja ver toda la estructura completa para comprobar que todo está en su sitio.

```python
agenda = []

agenda.append({"nombre": 'Juan',
"apellido": 'Lopez',
"correo": 'juan@example.com'})

agenda.append({"nombre": 'Laura',
"apellido": 'Garcia',
"correo": 'laura@example.com'})

agenda.append({"nombre": 'Pedro',
"apellido": 'Martinez',
"correo": 'pedro@example.com'})

agenda.append({"nombre": 'Ana',
"apellido": 'Rodriguez',
"correo": 'ana@example.com'})

agenda.append({"nombre": 'Luis',
"apellido": 'Gomez',
"correo": 'luis@example.com'})

print(agenda)
```

En resumen, así es como manejamos datos estructurados sin complicarnos la vida.
Es una base sólida que se usa en cosas más grandes como gestores de usuarios o cachés. Lo importante es saber elegir: diccionarios para los objetos y listas para agruparlos.
