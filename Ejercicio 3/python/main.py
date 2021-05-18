import os
from tabulate import tabulate
import requests

def iniciar():
    os.system('cls')
    while True:
        print('Seleccione una opción: ')
        print('\t1. Registrar movimiento')
        print('\t2. Ver todos los movimientos')
        print('\t3. Buscar un movimiento')
        print('\t4. Modificar un movimiento')
        print('\t5. Eliminar un movimiento')
        print('\t6. Salir')
        opcion = input('Ingrese una opción: ')
        if opcion == '1':
            nuevo_movimiento()
        elif opcion == '2':
            mostrar_movimientos()
        elif opcion == '3':
            buscar_movimiento()
        elif opcion == '4':
            modificar_movimiento()
        elif opcion == '5':
            eliminar_movimiento()
        elif opcion == '6':
            break
        else:
            print('Escoja una opción correcta')

def nuevo_movimiento():
    tipo = input('Ingrese el tipo de movimiento \n- Ingreso\n- Gasto\n')
    cantidad = input('Ingrese la cantidad: ')
    fecha = input('Ingrese la fecha: ')
    data = { 'tipo': tipo, 'cantidad': cantidad, 'fecha': fecha}
    respuesta = requests.post(url='http://localhost:3000/movimientos/registrar', data=data)
    print(respuesta.text)

def mostrar_movimientos():
    response = requests.get(url='http://localhost:3000/movimientos/todos')
    datos = []
    for dato in response.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID', 'TIPO DE MOVIMIENTO', 'CANTIDAD', 'FECHA']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def buscar_movimiento():
    id = input('Ingrese el id del movimiento a buscar: ')
    response = requests.get(url='http://localhost:3000/movimientos/buscar/'+id)
    datos = []
    for dato in response.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID', 'TIPO DE MOVIMIENTO', 'CANTIDAD', 'FECHA']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def modificar_movimiento():
    id = input('Ingrese el id del movimiento a modificar: ')
    campo = input('Ingrese el campo a modificar:\n1. Tipo\n2. Cantidad\n3. Fecha')
    nuevo_valor = ''
    if(campo == '1'):
        campo = 'tipo'
        nuevo_valor = input('Ingrese el tipo de movimiento: ')
    elif(campo == '2'):
        campo = 'cantidad'
        nuevo_valor = input('Ingrese la cantidad: ')
    elif(campo == '3'):
        campo = 'fecha'
        nuevo_valor = input('Ingrese la fecha: ')
    data = {'campo': campo, 'nuevo_valor': nuevo_valor}
    respuesta = requests.post(url='http://localhost:3000/movimientos/modificar/'+id, data=data)
    print(respuesta.text)

def eliminar_movimiento():
    id = input('Ingrese el id del movimiento a elimina: ')
    respuesta = requests.post(url='http://localhost:3000/movimientos/eliminar/'+id)
    print(respuesta.text)

iniciar()