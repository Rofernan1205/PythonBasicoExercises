# Contador de vocales: Escribe una función que reciba una palabra y cuente cuántas vocales tiene.

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def contador_vocales(cadena):
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    print(f"Cadena : {cadena} ")
    print(f"Cantidad de vocales : {contador}")


texto = input("Ingrese cadena de texto : ").strip()
contador_vocales(texto)