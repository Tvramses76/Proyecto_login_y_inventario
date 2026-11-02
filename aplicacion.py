
import json
from pathlib import Path

def pagina():
    print('\nBIENVENIDO AL SISTEMA DE CONTROL DE INVENTARIO')

    archivo_json = Path(__file__).with_name('guardado.json')

    try:
        with archivo_json.open('r', encoding='utf-8') as archivo:
            inventario = json.load(archivo).get('inventario', [])
    except FileNotFoundError:
        inventario = []
    except json.JSONDecodeError as error:
        print(f'No se pudieron cargar los datos de guardado.json: {error}')
        inventario = []

    def guardar_inventario():
        with archivo_json.open('w', encoding='utf-8') as archivo:
            json.dump({'inventario': inventario}, archivo, ensure_ascii=False, indent=4)

    def agregar_producto():
        print('\nAgregar producto')
        nombre = input('Ingrese el nombre del producto: ').lower().strip()
        cantidad = int(input('Ingrese la cantidad del producto: '))
        precio_unitario = float(input('Ingrese el precio unitario del producto: '))
        precio_total = cantidad * precio_unitario
        producto = {'nombre': nombre, 'cantidad': cantidad, 'precio unitario': precio_unitario,
                    'precio total': precio_total}
        inventario.append(producto)
        print(f'Producto {nombre} agregado al inventario.')
        guardar_inventario()

    def mostrar_inventario():
        print('\nINVENTARIO ACTUAL')
        if not inventario:
            print('El inventario está vacío.')
        else:
            for producto in inventario:
                print("-" * 100)
                print(f"Nombre: {producto['nombre']}")
                print(f"Cantidad: {producto['cantidad']}")
                print(f"Precio unitario: {producto['precio unitario']}")
                print(f"Precio total: {producto['precio total']}")


    def eliminar_producto():
        print('\nEliminar producto')
        for producto in inventario:
            print(f"Nombre: {producto['nombre']} |")
            print("-" * 10)
        nombre = input('Ingrese el nombre del producto a eliminar: ')
        nombre = nombre.lower().strip()
        for producto in inventario:
            if producto['nombre'] == nombre:
                inventario.remove(producto)
                print(f'Producto {nombre} eliminado del inventario.')
                guardar_inventario()
                return
        print(f'Producto {nombre} no encontrado en el inventario.')

    menu = 0

    while menu == 0:
        print('\n--- Menú ---')
        print('1. Agregar producto')
        print('2. Mostrar inventario')
        print('3. Eliminar producto')
        print('4. Salir')
        menu = int(input('Seleccione una opción: '))

        if menu == 1:
            agregar_producto()
            menu = 0
        elif menu == 2:
            mostrar_inventario()
            menu = 0
        elif menu == 3:
            eliminar_producto()
            menu = 0
        elif menu == 4:
            print('Saliendo del sistema y cerrando secion...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida.')