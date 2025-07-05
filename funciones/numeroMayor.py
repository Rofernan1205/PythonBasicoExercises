# Mayor de dos: Escribe una función que reciba números y devuelva el mayor.
def numero_mayor(*args):
    numeros = list(args)
    numeros.sort()
    mayor = numeros[len(numeros) - 1]
    print(mayor)


numero_mayor(1, 2, 34, 21, 33, 22, 33, 65)
