import os
from tabulate import tabulate
import requests

def iniciar():
    os.system('cls')
    while True:
        print('Escoja una de las opciones: ')
        print('1. Registrar un producto')
        print('2. Consultar todos los productos')
        print('3. Buscar un producto')
        print('4. Modificar un producto')
        print('5. Eliminar un producto')
        print('6. Nueva venta')
        print('7. Salir')
        opcion = input('Ingrese la opción: ')
        if opcion == '1':
            nuevo_producto()
        if opcion == '2':
            ver_productos()
        if opcion == '3':
            buscar_producto()
        if opcion == '4':
            modificar_producto()
        if opcion == '5':
            eliminar_producto()
        if opcion == '6':
            nueva_venta()
        elif opcion == '7':
            break
        else:
            print('Ingrese una de las opciones')

def nuevo_producto():
    nombre = input('Ingrese el nombre: ')
    descripcion = input('Ingrese la descipción')
    precio = input('Ingrese el precio: ')
    data = { 'nombre': nombre, 'descripcion': descripcion, 'precio':precio }
    respuesta = requests.post(url='http://localhost:3000/productos/registrar', data=data)
    print(respuesta.text)

def ver_productos():
    respuesta = requests.get(url='http://localhost:3000/productos/todos')
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID', 'NOMBRE', 'DESCRIPCIÓN', 'PRECIO']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def buscar_producto():
    id = input('Ingrese el id del producto a buscar:')
    respuesta = requests.get(url='http://localhost:3000/productos/buscar/'+id)
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID', 'NOMBRE', 'DESCRIPCIÓN', 'PRECIO']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def modificar_producto():
    id = input('Ingrese el id del producto a modificar: ')
    campo = input('Seleccione el campo a modificar: \n1. Nombre\n2. Descripción\n3. Precio')
    nuevo_valor = input('Ingrese el nuevo valor: ')
    data = {'campo': campo, 'nuevo_valor': nuevo_valor}
    respuesta = requests.post(url='http://localhost:3000/productos/modificar/'+id, data=data)
    print(respuesta.text)

def eliminar_producto():
    id = input('Ingrese el id del producto a eliminar: ')
    respuesta = requests.post(url='http://localhost:3000/productos/eliminar/'+id)
    print(respuesta.text)

def nueva_venta():
    cliente = input('Ingrese el nombre del cliente: ')
    total = 0
    productos = []
    print('Seleccione los productos. Presione 0 para salir.')
    while True:
        id = input('Ingrese el id del producto: ')
        if (id == '0'):
            break
        else:
            producto = requests.get(url='http://localhost:3000/productos/buscar/'+id)
            if len(producto.json()):
                nombre = producto.json()[0]['nombre']
                precio = producto.json()[0]['precio']
                cantidad = input('Ingrese la cantidad: ')
                total_por_producto = int(cantidad) * float(precio)
                total += total_por_producto
                productos.append([id, nombre, precio, cantidad, total_por_producto])
                mostrar_venta(cliente, productos, total)
            else:
                print('Producto no encontrado')

def mostrar_venta(cliente, productos, total):
    print('\n\t\tComprobante de venta')
    print('\nCliente: '+cliente)
    headers = ['ID', 'NOMBRE', 'PRECIO', 'CANTIDAD', 'TOTAL']
    tabla = tabulate(productos, headers, tablefmt='simple')
    print(tabla)
    print('\t\t\tTotal a pagar: '+ str(total))

iniciar()