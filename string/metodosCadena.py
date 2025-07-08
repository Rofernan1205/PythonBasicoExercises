# Transforma "Hola Mundo" a mayúsculas y minúsculas.

cadena = "Hola Mundo"


def mayus_minus(texto, formato):
    if formato == "mayuscula":
        print(texto.upper())
    elif formato == "minuscula":
        print(texto.lower())
    else:
        print("No existe formato")


mayus_minus(cadena, "mayuscula")


# Reemplaza "Mundo" por "Python" en "Hola Mundo".

def reemplaza_palabra(texto, palabra, cambio):
    text_cambio = texto.replace(palabra, cambio)
    print(text_cambio)


reemplaza_palabra(cadena, "Mundo", "Python")

# Divide "uno, dos, tres" en una lista.

cadena_numeros = "uno, dos, tres"


def dividir_item(texto, caracter):
    numeros = texto.split(caracter)
    print(numeros)


dividir_item(cadena_numeros, ",")

# Cuenta cuántas veces aparece la letra "a" en "abracadabra".

texto_prueba = "abracadabra"


def contar_letras(texto, letra):
    numero = texto.count(letra)
    print(f'La "{letra}" aparace {numero} en el texto')


contar_letras(texto_prueba, "a")
