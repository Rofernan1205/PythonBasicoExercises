# 3. Par o impar: Pide un número al usuario y di si es par o impar.
def detector_par_impar(numero):
    if numero % 2 == 0:
        print("Es un número par")
    else:
        print("Es un número impar")
try:
    numero_ingreso = int(input("Ingrese número a válidar : "))
    detector_par_impar(numero_ingreso)
except TypeError as err:
    raise TypeError(err)
