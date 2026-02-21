from inventario import *

print(" *** Sistema de Inventario ***")

lista_productos = cargar_inventario()

while True:
    opcion = mostrar_menu()

    if opcion == 1:
        nombre_producto = pedir_nombre()
        cantidad_producto = pedir_cantidad()
        precio_producto = pedir_precio()

        producto = almacenar_producto(nombre_producto, cantidad_producto, precio_producto)
        lista_productos.append(producto) # Agregar el producto almacenado en un diccionario en la lista
        guardar_inventario(lista_productos)

    elif opcion == 2:
        mostrar_productos(lista_productos)

    elif opcion == 3:
        buscar_producto(lista_productos, cantidad_producto)

    elif opcion == 4:
        actualizar_producto(lista_productos)
        guardar_inventario(lista_productos)

    elif opcion == 5:
        eliminar_producto(lista_productos)
        guardar_inventario(lista_productos)

    elif opcion == 6:
        calcular_valor_inventario(lista_productos)

    elif opcion == 7:
        print("\nSaliendo..")
        break

    else:
        print("Error!! Opcion invalida.")







