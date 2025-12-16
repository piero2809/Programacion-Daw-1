# pip3 install pillow --break-system-packages
from PIL import Image

imagen = Image.open("/home/piero/Escritorio/Github/Programacion-Daw-1/Segundo Trimestre/Clases/011-Utilizacion avanzada de clases/005-Interfaces/gatito123.jpg")

anchura,altura = imagen.size	

for x in range(0,anchura):	
	for y in range(0,altura):	
		pixel = imagen.getpixel((x, y))	
		rojo = pixel[0]
		verde = pixel[1]
		azul = pixel[2]
		rojo += 20
		verde += 20
		azul += 20
		pixel = (rojo,verde,azul)
    
imagen.save("modificado.jpg")N