# Determinar si un número es par usando funciones lambda
try:
    numero = int(input("Ingrese número: ").strip())
    valor = lambda num : "par" if   num % 2 == 0 else "impar"
    print(valor(numero))
except ValueError as err:
    raise ValueError(err)
