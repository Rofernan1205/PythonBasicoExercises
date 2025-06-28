# 3. Nombres: Crea una lista con 5 nombres y muestra solo el tercero
nombres = []
def listaNombre(nombre):
    nombres.append(nombre)


conta = 0
while conta < 5:
    estado = True
    while estado:
        nombre_input = input("Ingrese nombre : ")
        if nombre_input.strip():
            listaNombre(nombre_input)
            estado = False
            conta += 1
        else:
            print("Ingrese datos")
print(nombres)
print(f"Elemento de la tercera posición es : {nombres[2]}")

