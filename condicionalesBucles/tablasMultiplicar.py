# Tabla de multiplicar: Pide un número y muestra su tabla de multiplicar del 1 al 10 con for.
import time
def tablas_multiplicar():
    for x in range(1,13):
        for y in range(1,13):
            resultado = x * y
            print(f"{y} x {x} = {resultado}")
            time.sleep(0.5)
        print("\n")

tablas_multiplicar()