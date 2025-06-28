# 2. Conversión de tipos: Pide al usuario su edad y muestra cuántos meses ha vivido (edad * 12).
import datetime
def calculador_edad(fecha):
    fechaActual = datetime.datetime.now()
    fechaNacimiento = datetime.datetime.strptime(fecha, "%d/%m/%Y")
    edad = fechaActual.year - fechaNacimiento.year
    if fechaActual.month < fechaNacimiento.month or (fechaActual.month == fechaNacimiento.month and fechaActual.day < fechaNacimiento.day):
        edad = edad - 1
    return  edad

fecha_nacimiento = input("Ingrese fecha de nacimineto (DD/MM/YY) : ")
resultado = calculador_edad(fecha_nacimiento)
print(resultado)

