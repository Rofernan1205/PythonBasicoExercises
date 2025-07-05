# Saludo personalizado: Escribe una función que reciba un nombre y devuelva un saludo de acuerdo al tiempo actual.
import datetime


def saludo_personalizado(nombre):
    fecha_hora = datetime.datetime.now()
    hora = fecha_hora.time().hour
    if 0 < hora <= 12:
        print(f"Buenos dias {nombre}")
    elif 12 < hora <= 18:
        print(f"Buenas tardes {nombre}")
    elif 18 < hora <= 23:
        print(f"buenas noches {nombre}")


nombre = input("Ingrese nombre : ").strip()
saludo_personalizado(nombre)
