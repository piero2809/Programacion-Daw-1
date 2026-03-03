En Python, los errores o excepciones pueden ocurrir durante la ejecución de un programa, interrumpiendo su funcionamiento normal.
El manejo de excepciones mediante las sentencias try y except permite capturar estos errores y definir una respuesta controlada.


En Python, try se utiliza para ejecutar un bloque de código que podría generar un error, y except para indicar la acción que debe realizarse si ese error ocurre.

En este caso, se intenta dividir la variable puntos entre tiros_libres, cuyo valor es 0. Al producirse una división entre cero, se activa el bloque except, mostrando un mensaje de advertencia y permitiendo que el programa continúe su ejecución sin detenerse.


```
puntos = 4
tiros_libres = 0

try:
    puntos/tiros_libres
except:
    print("No se puede dividir lo putnos entre 0")

print("El programa sigue ejecutandose")


```

En conclusión, técnicas como el try-except permite interceptar errores en tiempo de ejecución y definir respuestas específicas, garantizando la continuidad y estabilidad del programa.