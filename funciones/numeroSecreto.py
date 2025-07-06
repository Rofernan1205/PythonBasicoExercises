# Número secreto: El usuario tiene 3 intentos para adivinar un número entre 1 y 10.
import random

numeros = []
for numero in range(1, 11):
    numeros.append(numero)


def numero_secreto(num):
    tu_numero = random.choice(numeros)
    if num == tu_numero:
        print("Ganastes")
        return True
    else:
        return False


def ejecutar_funcion():
    contador = 1
    while contador <= 3:
        try:
            dato = int(input("Ingrese número: ").strip())
            resultado = numero_secreto(dato)
            if resultado:
                contador = 3
                break
            else:
                contador += 1
        except ValueError as err:
            raise ValueError(err)


ejecutar_funcion()
