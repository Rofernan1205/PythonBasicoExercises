# Obtener el último carácter de una cadena de texto

caracter = lambda cadena: cadena[len(cadena) - 1]
texto = input("Ingrese cadena : ").strip()
resultado = caracter(texto)
print(resultado)
