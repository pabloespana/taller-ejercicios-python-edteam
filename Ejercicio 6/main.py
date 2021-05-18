import os
import requests
from tabulate import tabulate
from datetime import date

def iniciar():
    os.system('cls')
    while True:
        print('Seleccione una opción: ')
        print('1. Registar una cita médica')
        print('2. Ver todas las citas')
        print('3. Ver citas médicas de hoy')
        print('4. Modificar estado de cita')
        print('5. Eliminar cita')
        print('6. Salir')
        opcion = input('Ingrese la opción: ')
        if opcion == '1':
            nueva_cita()
        elif opcion == '2':
            mostrar_citas()
        elif opcion == '3':
            buscar_citas()
        elif opcion == '4':
            modificar_estado()
        elif opcion == '5':
            eliminar_cita()
        elif opcion == '6':
            break
        else:
            print('Escoja una de las opciones')

def nueva_cita():
    paciente = input('Ingrese el nombre del paciente: ')
    detalle = input('Ingrese el detalle de la cita: ')
    dia = input('Ingrese el día de la cita: ')
    hora = input('Ingrese la hora de la cita: ')
    data = {'paciente': paciente, 'detalle': detalle, 
    'dia':dia, 'hora':hora, 'estado':'Agendada'}
    respuesta = requests.post(url='http://localhost:3000/citas-medicas/registrar', data=data)
    print(respuesta.text)

def mostrar_citas():
    respuesta = requests.get(url='http://localhost:3000/citas-medicas/todas')
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID', 'PACIENTE', 'DETALLE', 'DÍA', 'HORA', 'ESTADO']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def buscar_citas():
    dia = date.today()
    respuesta = requests.get(url='http://localhost:3000/citas-medicas/buscar', data={'dia':dia})
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID', 'PACIENTE', 'DETALLE', 'DÍA', 'HORA', 'ESTADO']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def modificar_estado():
    id = input('Ingrese el id de la cita médica: ')
    estado = input('Ingrese el estado:\n- Agendada\n- Atendida\n')
    respuesta = requests.post(url='http://localhost:3000/citas-medicas/modificar/'+id, data={'estado':estado})
    print(respuesta.text)

def eliminar_cita():
    id = input('Ingrese el id de la cita médica: ')
    respuesta = requests.post(url='http://localhost:3000/citas-medicas/eliminar/'+id)
    print(respuesta.text)

iniciar()
