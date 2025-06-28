# 1. Suma de números: Crea un programa que pida dos números al usuario y muestre su suma.

def suma_numeros():
    num_01 = int(input("Ingrese numero 1 : "))
    num_02 = int(input("Ingrese numero 2 : "))
    suma = lambda a, b: a + b
    resultado = suma(num_01, num_02)
    print(f"L a suma es {resultado}")

suma_numeros()
