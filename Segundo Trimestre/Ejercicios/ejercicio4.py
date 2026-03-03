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
