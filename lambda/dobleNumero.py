# Crea una función lambda que reciba un número y devuelva el doble.

try:
    numero = int(input("Ingrese numero : ").strip())
    variable = lambda a: a * a
    print(variable(numero))
except ValueError as err:
    raise ValueError(err)
