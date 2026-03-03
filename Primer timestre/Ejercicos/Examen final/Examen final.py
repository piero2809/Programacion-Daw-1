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