import json
import os

def mostrar_menu():
    print('''\nMenu:
1. Registrar producto
2. Mostrar productos
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Calcular valor del inventario
7. Salir
''')

    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            return opcion
        except ValueError:
            print("Error!! Debes ingresar un número válido.")


def pedir_nombre():
    nombre_producto = input("\nIngresa el nombre del producto: ").strip().capitalize()
    return nombre_producto

def pedir_cantidad():
    while True:
        try:
            cantidad_producto = int(input("Ingresa la cantidad de productos: ").strip())
            if cantidad_producto <= 0:
                print("Error!! La cantidad debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Error!! No se permiten letras ni caracteres especiales.")
    return cantidad_producto

def pedir_precio():
    while True:
        try:
            precio_producto = float(input("Ingresa el precio del producto: "))
            if precio_producto <= 0:
                print("Error!! El prcio debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Error!! No se permiten letras ni caracteres especiales.")
    return precio_producto


def almacenar_producto(nombre_producto, cantidad_producto, precio_producto):

    producto = {
        "nombre": nombre_producto,
        "precio": precio_producto,
        "cantidad": cantidad_producto
    }
    return producto

def mostrar_productos(lista_productos):
    if lista_productos:
        print("\nLos productos registrados son:")
        for i, producto in enumerate(lista_productos,start=1):  # Recorre la lista de productos y me da el número del producto y el producto mismo, empezando a contar desde 1.
            print(f"\nProducto {i}:")
            print(f'''
                    Nombre: {producto["nombre"]}
                    Cantidad: {producto["cantidad"]}
                    Precio: ${producto["precio"]:.3f}''')
    else:
        print("No hay productos registrados.")


def buscar_producto(lista_productos, cantidad_producto):
    nombre = input("\nIngresa el nombre del producto que quieres buscar: ").strip().capitalize()

    for proucto in lista_productos:
        if nombre == proucto["nombre"]:
            print(f"Sí existe el producto, hay {cantidad_producto} unidades.")
        else:
            print("No existe el producto.")

def actualizar_producto(lista_productos):
    nombre_actualizar = input("\nIngresa el nombre del producto que quieres actualizar: ").strip().capitalize()

    encontrado = False

    for producto in lista_productos:
        if nombre_actualizar == producto["nombre"]:
            print(f"Producto encontrado.")

            nueva_cantidad = pedir_cantidad()
            nuevo_precio = pedir_precio()

            producto["cantidad"] = nueva_cantidad
            producto["precio"] = nuevo_precio

            print("Producto actualizado correctamente.")
            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")


def eliminar_producto(lista_productos):
    nombre_eliminar = input("\nIngresa el nombre del producto que quieres eliminar: ").strip().capitalize()

    encontrado = False

    for producto in lista_productos:
        if nombre_eliminar == producto["nombre"]:
            print("Producto encontrado y eliminado de la lista.")

            lista_productos.remove(producto)
            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")


def calcular_valor_inventario(lista_productos):

    if lista_productos:
        suma = 0
        for producto in lista_productos:
            if producto["cantidad"] > 0:
                valor = producto["precio"] * producto["cantidad"]
                suma += valor

        print(f"El valor total del inventario es de: {suma:.3f}")

    if not lista_productos:
        print("No hay productos registrados para calcular el valor.")


# Crear funciones para guardar los datos de la lista en archivos


def guardar_inventario(lista_productos):
    with open("inventario.json", "w") as archivo:
        json.dump(lista_productos, archivo)

def cargar_inventario():
    if os.path.exists("inventario.json"):
        with open("inventario.json", "r") as archivo:
            return json.load(archivo)

    return []


