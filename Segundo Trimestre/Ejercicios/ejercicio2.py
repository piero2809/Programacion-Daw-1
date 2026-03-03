cadena = "Jose Vicente"

def procesar_caracteres(texto):
    print("Cadena:" + texto)
    for letra in texto:
       #Convertir cada caracter a ASCII ya que ord no acepta cadenas ("Lo aprendi a la mala")
        valor_ascii = ord(letra)
        
        # Revertir el ASCII a caracter con chr() ("Lo aprendi a la mala tambien")
        letra_recuperada = chr(valor_ascii)
        
        print(f"Carácter: '{letra}' \t ASCII: {valor_ascii} \t Recuperado: '{letra_recuperada}'")

procesar_caracteres(cadena)
