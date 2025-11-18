Otro ejercicio:

¡Vamos! Aquí tienes **solo el enunciado** del ejercicio final para la unidad de DAW, sin soluciones ni esqueletos.

# 101 — Ficha técnica y presupuesto de un dispositivo (JS/HTML y Python)

## Objetivo

Crear un programa que recopile datos básicos de un dispositivo, realice **cálculos y conversiones simples**, evalúe si encaja en un **presupuesto**, y muestre una **salida formateada** como ficha técnica y presupuesto. Se debe evidenciar el dominio de **variables, literales, constantes, tipos y conversiones, operadores aritméticos/comparación/booleanos, comentarios y salidas**.

## Alcance de contenidos (deben aparecer de forma clara)

* **Identificadores** y nomenclatura correcta (evitar nombres ambiguos).
* **Variables**, **literales** y **constantes** (`const` en JS; mayúsculas en Python).
* **Tipos y conversiones** (JS: `Number()`, `parseInt/Float` o equivalentes simples; Python: `int/float`).
* **Operadores**: aritméticos, comparaciones y booleanos (sin necesidad de `if` aún).
* **Entradas/salidas**:

  * JS/HTML: `prompt()`, `console.log()` y **una** salida en el documento (`document.write()`).
  * Python: `input()` y `print()`.
* **Comentarios** de bloque y en línea.

## Requisitos funcionales

1. **Entradas**
   Solicitar al usuario:

   * `nombre` del dispositivo (cadena).
   * `precio_base` (numérico).
   * `almacenamiento_gb` (numérico).
   * `peso_g` (numérico).
   * `pantalla_pulgadas` (numérico).
   * `presupuesto_max` (numérico) para evaluar si se excede.

2. **Constantes**

   * Definir la constante `IVA = 0.21` (21%).

3. **Cálculos obligatorios**

   * `total_iva = precio_base * IVA`
   * `precio_total = precio_base + total_iva`
   * `almacenamiento_mb = almacenamiento_gb * 1024`
   * `peso_kg = peso_g / 1000`

4. **Comparaciones y booleanos (sin `if`)**

   * Calcular y **mostrar** el booleano `excede_presupuesto = precio_total > presupuesto_max`.
   * Mostrar al menos **dos** comparaciones adicionales (por ejemplo, `pantalla_pulgadas >= 6`, `peso_kg < 1`, etc.).
   * Mostrar al menos **una** expresión booleana con `&&`/`||` en JS o `and`/`or` en Python (por ejemplo, “¿Es pantalla grande **y** no excede presupuesto?”).

5. **Salida formateada**

   * **Encabezado** con tres líneas (nombre del programa, autor/a, año).
   * **Ficha** con todos los datos de entrada y los resultados calculados (precio base, IVA, total, almacenamiento en MB, peso en kg).
   * **Bloque de evaluación** con los resultados booleanos (excede/no excede, comparaciones adicionales).
   * En JS/HTML, además de `console.log()`, deben aparecer **al menos dos líneas** visibles en el documento con `document.write()` (por ejemplo, total y estado de presupuesto).

6. **Comentarios mínimos**

   * Comentario de bloque inicial con nombre, versión, autor/a y finalidad.
   * Comentarios en línea explicando **una conversión de tipo**, **un cálculo** y **una comparación/booleana**.

7. **Restricciones**

   * No usar librerías externas.
   * No usar estructuras no vistas (evitar funciones/clases if no se han tratado).
   * Mantener números significativos como **constantes** cuando sea apropiado (por ejemplo, IVA, factores de conversión).

## Entregables

* **Opción A (recomendada):** entregar **dos versiones** del ejercicio

  1. `006-Operadores y expresiones/101-Ejercicios/021-ficha-presupuesto.html` (JS/HTML)
  2. `006-Operadores y expresiones/101-Ejercicios/028-ficha-presupuesto.py` (Python)
* **Opción B:** si solo se entrega una versión, debe ser **JS/HTML**, ya que esta unidad trabaja ambos entornos.
* Mantener los nombres de carpetas coherentes con la estructura dada del proyecto.

## Casos de prueba (a ejecutar por el alumnado)

> No entregar salidas ni código; únicamente verificar que el programa se comporta como se especifica.

1. **Presupuesto justo**

   * `precio_base` tal que `precio_total == presupuesto_max` → `excede_presupuesto` debe ser `false`.
2. **Excede presupuesto**

   * `precio_base` alto → `excede_presupuesto` `true`.
3. **Conversiones correctas**

   * Valores con decimales para `pantalla_pulgadas` y `peso_g`; comprobar `peso_kg` y comparaciones.
4. **Almacenamiento**

   * `almacenamiento_gb = 0.5` → `almacenamiento_mb = 512`.
5. **Booleanos compuestos**

   * Una condición compuesta que combine **dos** comparaciones con `&&`/`||` (o `and`/`or`) y muestre el resultado.