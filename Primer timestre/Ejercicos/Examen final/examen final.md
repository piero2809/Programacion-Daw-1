
En el mundo de la programación, los CRUD son muy importantes para la gestión de datos en las aplicaciones. CRUD significa CREATE, READ, UPDATE y DELETE, que son cuatro operaciones basicas que se pueden realizar. Estas operaciones permiten crear, leer, actualizar y eliminar los datos almacenados.


Primero, se importa la librerìa para conectar python con MySQL. Luego, se establece la conexión a la base de datos utilizando el usuario ya creado en la base de datos, se crea el cursor para que se puedan ejecutar los comando SQL. Luego se crea un bucle `While True:` para que el programa se ejecute y el usuario pueda elegir entre las cuatro opciones del CRUD. Se crea cada opcion con un `if` y `elif` para que el usuario pueda elegir la opción que desee. dentro de cada `if-else` se ejecuta el comando SQL correspondiente y finalmente se ejecuta conexion.commit() para guardar los cambios en la base de datos.

## Se realiza el ejercicio:
``
import mysql.connector 
'''
Programa de gestión de proyectos
v0.1 Piero Funes

'''

print ("---Gestión de proyectos v0.1---")
print ("---------Piero Funes----------")

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolioexamen",
  password="1portafolioexamen",
  database="portafolioexamen"
)
cursor = conexion.cursor()


while True:
    print ("1.-Agregar un proyecto")
    print ("2.-Ver los proyectos")
    print ("3.-Actualizar un proyecto")
    print ("4-.Eliminar un proyecto")
    
    opcion = int (input ("Inserte una opción: "))

    if opcion == 1 :
        titulo = input ("Inserte Título: ")
        descripcion = input ("Inserte descripción: ")
        fecha = input ("Inserte la fecha en formato AA-MM-DD:")
        id_categoria  = input ("Introduce la categoria Dam(1)/Daw(2)")
        cursor.execute('''
      INSERT INTO piezasportafolio (titulo, descripcion, fecha, id_categoria) VALUES (
      "'''+titulo+'''",
      "'''+descripcion+'''",
      "'''+fecha+'''",
      '''+id_categoria+'''
      );
    ''')
        conexion.commit()
    
    elif opcion == 2:
        cursor.execute('''
      SELECT * FROM piezasportafolio;
    ''')
        filas = cursor.fetchall()
        for fila in filas:
            print (fila)
    
    elif opcion == 3:
        identificador = input("Introduce el id a actualizar: ")
        titulo = input("Introduce el titulo: ")
        descripcion = input("Introduce la descripcion: ")
        fecha = input("Introduce la fecha en formato AA-MM-DD: ")
        id_categoria = input("Introduce la categoria Dam(1)/Daw(2)")
        cursor.execute('''
        UPDATE piezasportafolio SET 
        titulo = "'''+titulo+'''",
        descripcion = "'''+descripcion+'''",
        fecha = "'''+fecha+'''",
        id_categoria = '''+id_categoria+'''
        WHERE identificador = '''+identificador+''';
        ''')
        conexion.commit()
        
    elif opcion == 4:
        identificador = input("Introduce el id a eliminar: ")
        cursor.execute('''
        DELETE FROM piezasportafolio
        WHERE identificador = '''+identificador+''';
        ''')
        conexion.commit()

``

Las personas suelen equivocarse en las comas, ya que puede llegar a ser confuso


En resumen, el uso de python en conjunto con MySQL permite crear aplicaciones CRUD para la gestion de datos en una BD. Esto es importante para el desarrollo de aplicaciones que requieren almacenar y manipular datos de manera eficiente.