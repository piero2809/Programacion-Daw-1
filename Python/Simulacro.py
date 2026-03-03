import mysql.connector

print("Bienvenidos a la aplicacion")

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolioceac",
  password="1portafolioceac",
  database="portafolio"
)
cursor = conexion.cursor()

while True:
  print("Selecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualizar registro")
  print("4.-Eliminar registro")

  opcion = int(input("Elige tu opcion: "))
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripcion: ")
    imagen = input("Introduce la imagen: ")
    url = input("Introduce la url: ")
    id_categoria = input("Introduce la categoria: ")
    cursor.execute('''
      INSERT INTO Piezas (titulo, descripcion, imagen, url, id_categoria) VALUES (
      "'''+titulo+'''",
      "'''+descripcion+'''",
      "'''+imagen+'''",
      "'''+url+'''",
      '''+id_categoria+'''
      );
    ''')
    conexion.commit()
  elif opcion == 2:

    cursor.execute('''
      SELECT * FROM Piezas;
    ''')

    filas = cursor.fetchall()

    for fila in filas:
      print(fila)
  elif opcion == 3:
    identificador = input("Introduce el id a actualizar: ")
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripcion: ")
    imagen = input("Introduce la imagen: ")
    url = input("Introduce la url: ")
    id_categoria = input("Introduce la categoria: ")
    cursor.execute('''
      UPDATE Piezas SET 
      titulo = "'''+titulo+'''",
      descripcion = "'''+descripcion+'''",
      imagen = "'''+imagen+'''",
      url = "'''+url+'''",
      id_categoria = '''+id_categoria+'''
      WHERE identificador = '''+identificador+''';
    ''')
    conexion.commit()
  elif opcion == 4:
    identificador = input("Introduce el id a eliminar: ")
    cursor.execute('''
      DELETE FROM Piezas
      WHERE identificador = '''+identificador+''';
    ''')
    conexion.commit()



###Version mejorada por IA

import mysql.connector

print("Bienvenidos a la aplicacion")

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolioceac",           # usuario creado en SQL
  password="1portafolioceac",      # contraseña tal como está en SQL
  database="portafolio"            # nombre real de la base de datos
)
cursor = conexion.cursor()

while True:
  print("Selecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualizar registro")
  print("4.-Eliminar registro")

  opcion = int(input("Elige tu opcion: "))
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripcion: ")
    imagen = input("Introduce la imagen: ")
    url = input("Introduce la url: ")
    id_categoria = input("Introduce la categoria: ")
    cursor.execute('''
      INSERT INTO Piezas (titulo, descripcion, imagen, url, id_categoria) VALUES (
      %s, %s, %s, %s, %s
      );
    ''', (titulo, descripcion, imagen, url, id_categoria))
    conexion.commit()
  elif opcion == 2:
    cursor.execute('''
      SELECT * FROM Piezas;
    ''')
    filas = cursor.fetchall()
    for fila in filas:
      print(fila)
  elif opcion == 3:
    identificador = input("Introduce el id a actualizar: ")
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripcion: ")
    imagen = input("Introduce la imagen: ")
    url = input("Introduce la url: ")
    id_categoria = input("Introduce la categoria: ")
    cursor.execute('''
      UPDATE Piezas SET 
      titulo = %s,
      descripcion = %s,
      imagen = %s,
      url = %s,
      id_categoria = %s
      WHERE identificador = %s;
    ''', (titulo, descripcion, imagen, url, id_categoria, identificador))
    conexion.commit()
  elif opcion == 4:
    identificador = input("Introduce el id a eliminar: ")
    cursor.execute('''
      DELETE FROM Piezas
      WHERE identificador = %s;
    ''', (identificador,))
    conexion.commit()
