# Dado el string texto = "Programar es divertido", imprime:
# El primer carácter.
# Los últimos 5 caracteres.
# La palabra "divertido" usando slicing.

cadena = "Programar es divertido"


def primera_letra(texto):
    print(texto[0])


def ultima_cinco_letra(texto):
    print(texto[len(texto) - 5::])


def buscar_palabra(texto, palabra):
    resultado = texto[texto.find(palabra):]
    print(resultado)


primera_letra(cadena)
ultima_cinco_letra(cadena)
buscar_palabra(cadena, "divertido")
