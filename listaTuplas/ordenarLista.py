# Ordenar lista: Pide 3 números al usuario, guárdalos en una lista y ordénalos.
numeros = []
def registro_numeros(numero):
    numeros.append(numero)



for i in range(1, 4):
    try:
        dato_input = int(input("Ingrese número : "))
        registro_numeros(dato_input)
    except TypeError as err:
        raise TypeError(err)

print(f"Números : {numeros}")

def ordenar(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    derecha = [x for x in lista[1:] if x <= pivote]
    izquierda = [x for x in lista[1:] if x > pivote]
    return ordenar(derecha) + [pivote] + ordenar(izquierda)

resultado = ordenar(numeros)
print(resultado)


