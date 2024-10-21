print("Arzaba Diaz April")
print("1173")
print("3W")
#esta linea creara el diccionario de traducción
def crear_diccionario(traducciones):
    diccionario = {}
    pares = traducciones.split(", ")
    for par in pares:
        palabra, traduccion = par.split(":")
        diccionario[palabra.strip()] = traduccion.strip()
    return diccionario

#esta linea traducira la frase
def traducir_frase(diccionario, frase):
    palabras = frase.split()
    traduccion = []
    for palabra in palabras:
        #esta linea quitara los signos de puntuacion
        palabra_limpia = palabra.strip(",.!?;:")
        #esta linea traducira y agregara a la lista
        traduccion.append(diccionario.get(palabra_limpia, palabra))
    return " ".join(traduccion)

#esta linea dara un ejemplo de uso
traducciones = input("Introduce las traducciones (formato 'espanol:ingles'): ")
diccionario = crear_diccionario(traducciones)

frase = input("Introduce una frase en español: ")
resultado = traducir_frase(diccionario, frase)
print("Traducción:", resultado)
