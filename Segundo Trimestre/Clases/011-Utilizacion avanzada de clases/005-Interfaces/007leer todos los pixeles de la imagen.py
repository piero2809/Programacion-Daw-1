from PIL import Image

imagen = Image.open("/home/piero/Escritorio/Github/Programacion-Daw-1/Segundo Trimestre/Clases/011-Utilizacion avanzada de clases/005-Interfaces/gatito123.jpg")

anchura,altura = imagen.size		# Cojo altura y anchura

for x in range(0,anchura):			# Repaso la anchura
	for y in range(0,altura):			# Repaso la altura
		pixel = imagen.getpixel((x, y))	# Cojo cada pixel
		print(pixel)										# Y lo saco por pantalla