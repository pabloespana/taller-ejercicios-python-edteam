import os
from tabulate import tabulate
from conexion import *
from Nota import Nota

con = conectar()

def iniciar():
    print('Seleccione una de las opciones: ')
    print('1. Nueva nota')
    print('2. Ver notas')
    print('3. Ver contenido')
    print('4. Modificar nota')
    print('5. Eliminar nota')
    print('6. Salir de la aplicación')
    opcion = input('Ingrese la opción: ')
    if opcion == '1':
        nueva_nota()
    elif opcion == '2':
        ver_notas()
    elif opcion == '3':
        ver_contenido()
    elif opcion == '4':
        modificar_contenido()
    elif opcion == '5':
        eliminar_nota()

def nueva_nota():
    nombre = input('Ingrese el nombre de la nota: ')
    contenido = input('Ingrese el contenido:\n')
    nota = Nota(nombre=nombre, contenido=contenido)
    respuesta = nota.registar()
    print(respuesta)

def ver_notas():
    nota = Nota()
    datos = nota.mostrar()
    headers = ['ID', 'NOMBRE DEL ARCHIVO', 'FECHA DE CREACIÓN']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def ver_contenido():
    id = input('Ingrese el id de la nota: ')
    nota = Nota(id=id)
    resultado = nota.buscar()
    if len(resultado):
        file = open(f'./notas/{resultado[0][1]}', 'r')
        print('\n'+file.read()+'\n')
        file.close()
    else:
        print('No se encontró el archivo')

def modificar_contenido():
    archivos = os.listdir('./notas')
    for numero, archivo in enumerate(archivos):
        print(f'{numero+1} {archivo}' )
    seleccionado = input('Escoja el archivo a modificar: ')
    nuevo_contenido = input('\nIngrese el nuevo contenido:\n')
    file = open(f'./notas/{archivos[int(seleccionado)-1]}', 'w')
    file.write(nuevo_contenido)
    file.close()
    print('Archivo modificado')

def eliminar_nota():
    id = input('Ingrese el id de la nota a eliminar: ')
    nota = Nota(id=id)
    resultado = nota.eliminar()
    print(resultado)

iniciar()