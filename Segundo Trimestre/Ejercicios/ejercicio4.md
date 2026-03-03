En Python, los diccionarios son ideales para manejar datos organizados.
En este ejercicio veremos cómo crear uno, recorrer su contenido y añadirle datos nuevos dinámicamente. Es un concepto fundamental y muy práctico para cualquier aplicación que necesite manejar información flexible, como formularios o configuraciones.

El código comienza creando un diccionario `datos_personales` con claves estándar: nombre, apellidos y email.  
Después, usamos un bucle `for` para recorrer las claves. En cada vuelta, imprimimos la clave y su valor para verificar qué información contiene.  
A continuación, añadimos una clave nueva `"edad"` con el valor `20` directamente.  
Al final, imprimimos todo el diccionario para confirmar que se ha actualizado correctamente. Esto demuestra la eficacia de los diccionarios para modificarse en tiempo de ejecución.

```python
# Se crea el objeto
datos_personales = {
    "nombre": "Piero",
    "apellidos": "Funes Larios",
    "email": "piero@example.com"
}

# Se recore todo el objeto y se imprime cada propiedad
for dato in datos_personales:
    print(dato + ": " + datos_personales[dato])

# Se añade la propiedad edad
datos_personales["edad"] = 20
print(datos_personales)
```

En resumen, este ejercicio cubre lo esencial de los diccionarios: creación, lectura y modificación. Su capacidad para adaptarse dinámicamente los convierte en una herramienta versátil para modelar datos que cambian.
