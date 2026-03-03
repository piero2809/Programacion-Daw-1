from PIL import Image

imagen = Image.open("/home/piero/Escritorio/Github/Programacion-Daw-1/Segundo Trimestre/Clases/011-Utilizacion avanzada de clases/005-Interfaces/gatito123.jpg")

pixel1 = imagen.getpixel((0,0))

print(pixel1)


