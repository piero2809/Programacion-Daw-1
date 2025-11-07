import os

import zipfile

origen = 'DAW_UD2-Instalación de sistemas operativos.pdf'

destino = 'comprimido pdf2.zip'

archivo = zipfile.ZipFile(destino, 'w', compression = zipfile.ZIP_DEFLATED)
archivo.write (origen)