# Inventario simple: Crea un diccionario con productos y precios. Luego permite agregar un nuevo producto desde input.
import time

productos = [
    {"id": "001", "producto": "agua", "precio": 12.00, "cantidad": 6}
]

menu = """inventario
seleccione acción a realizar
1. agregar producto      4. mostrar productos
2. actualizar producto   5. Eliminar producto
3. buscar producto 
"""


def main_menu():
    print(menu)
    try:
        accion = int(input("Ingrese numero: "))
        select_menu(accion)
    except ValueError as err:
        raise ValueError(err)


def select_menu(accion):
    if accion == 1:
        id = input("id: ")
        producto = input("producto: ").strip()
        precio = float(input("precio: "))
        cantidad = int(input("cantidad: "))
        agregar_producto(id, producto, precio, cantidad)
    elif accion == 2:
        actualizar_producto()
    elif accion == 3:
        id = input("id :").strip()
        buscar_producto(id)
    elif accion == 4:
        mostrar_prodcutos()
    elif accion == 5:
        id = input("id :").strip()
        eliminar_producto(id)
    else:
        print("Opción no válido")


def agregar_producto(id, producto, precio, cantidad):
    productos.append({"id": id, "producto": producto, "precio": precio, "cantidad": cantidad})
    print("registro succes")
    time.sleep(2)
    main_menu()


def actualizar_producto():
    pass


def buscar_producto(id):
    for producto in productos:
        if producto["id"] == id:
            print(producto)
    time.sleep(5)
    main_menu()


def mostrar_prodcutos():
    if len(productos) < 1:
        print("Sin datos")
    for producto in productos:
        print(producto)
    time.sleep(5)
    main_menu()


def eliminar_producto(id):
    for producto in productos:
        if producto["id"] == id:
            productos.remove(producto)
            print("Producto eliminado")
            time.sleep(1)
    main_menu()


main_menu()
