import os

import zipfile

origen = 'DAW_UD2-Instalación de sistemas operativos.pdf'

destino = 'comprimido pdf.zip'

archivo = zipfile.ZipFile(destino, 'w')
archivo.write (origen)