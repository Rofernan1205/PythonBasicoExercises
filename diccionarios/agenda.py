# # Agenda: Crea un diccionario con nombres como claves y teléfonos como valores. Permite buscar un número por nombre,
# agregar y eliminar.
import time

descripcion = """ Agenda
  --------------------------
  Eligir acción a realizar
  --------------------------
1. Registrar       3. Buscar
2. Mostrar lista   4. Eliminar
"""
agenda = {}


def menu_agenda(accion):
    if accion == 1:
        nombre = input("Ingrese nombre: ")
        telefono = input("Ingrese telefono: ")
        registro_agenda(nombre, telefono)
    elif accion == 2:
        print(agenda)
        time.sleep(2)
        ejecutar()
    elif accion == 3:
        nombre = input("Ingrese nombre: ").strip()
        buscar_agenda(nombre)
    elif accion == 4:
        nombre = input("Ingrese nombre: ").strip()
        eliminar_agenda(nombre)
    else:
        print("No existe esa accion")


def registro_agenda(nombre, telefono):
    agenda[nombre] = telefono
    print("registrado")
    ejecutar()


def buscar_agenda(nombre):
    for key, numero in agenda.items():
        if key == nombre:
            print(numero)
            time.sleep(2)
            break
        else:
            print("No existe contacto")
    ejecutar()


def eliminar_agenda(nombre):
    for key, numero in agenda.items():
        if key == nombre:
            agenda.pop(key)
            print("Eliminado")
            break
    ejecutar()


def ejecutar():
    print(descripcion)
    try:
        opcion = int(input("Ingrese opción a realizar : "))
        menu_agenda(opcion)
    except ValueError as err:
        raise ValueError(err)


ejecutar()


