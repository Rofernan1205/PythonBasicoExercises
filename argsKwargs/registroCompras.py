# Crear una función que reciba:
# Una lista de productos comprados (*args)
# Una serie de opciones de pago u otros datos (**kwargs)
# Imprima todos los productos comprados.
# Imprima los datos del cliente y del pago.
# Devuelva un resumen general.
# Precios de productos y total.
# Validación de metodo de pago.
# Guardar la compra en un archivo JSON.

import json

PRECIO_PRODUCTO = {
    "Laptop": 2500,
    "Mouse": 150,
    "Teclado": 200,
    "Monitor": 1200,
    "Audífonos": 350
}

METODO_PAGO = ("Tarjeta", "Efectivo", "Yape", "plin")


def registro_compra(*productos, **detalle):
    detalle_productos = []
    total_pagar = 0
    resumen = {}
    for producto in productos:
        if producto in PRECIO_PRODUCTO:
            detalle_productos.append({"Producto": producto, "Precio": PRECIO_PRODUCTO[producto]})
            total_pagar += PRECIO_PRODUCTO[producto]
        else:
            raise ValueError(f"No existe producto {producto}")

    nombre = detalle.get("nombre", "Desconocido")
    modo_entrega = detalle.get("modo_entrega", "Tienda")
    metodo_pago = detalle.get("metodo_pago", METODO_PAGO[1])
    if not metodo_pago in METODO_PAGO:
        raise ValueError(f"No existe método de pago tipo {metodo_pago}")
    resumen = {
        "cliente": nombre,
        "metodo_pago": metodo_pago,
        "envio": modo_entrega,
        "productos": detalle_productos,
        "total": total_pagar
    }
    return resumen


salida = registro_compra(
    "Laptop", "Mouse", "Audífonos",
    nombre="Rodrigo",
    metodo_pago="Tarjeta",
    modo_entrega="Delivery"
)

with open("compra.json", "w", encoding="utf-8") as f:
    json.dump(salida, f, indent=4, ensure_ascii=False)


