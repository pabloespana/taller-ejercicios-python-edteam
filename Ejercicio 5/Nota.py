from conexion import *
from datetime import date

class Nota:
    def __init__(self, id='', nombre='', contenido=''):
        self.id = id
        self.nombre = f'{nombre}.txt'
        self.contenido = contenido
        self.fecha_creacion = date.today()

    def registar(self):
        try:
            con = conectar()
            cursor = con.cursor()
            sql = 'insert into nota (nombre, fecha_creacion) values (%s, %s)'
            datos = (self.nombre, self.fecha_creacion)
            cursor.execute(sql, datos)
            self.crear_archivo()
            con.commit()
            con.close()
            print('Registro correcto')
        except mysql.Error as err:
            print('Ha ocrrido un error ', err)

    def crear_archivo(self):
        try:
            file = open(f'./notas/{self.nombre}', 'w')
            file.write(self.contenido)
            file.close()
        except OSError as err:
            print('Ha ocrrido un error ', err)

    def mostrar(self):
        datos = []
        try:
            con = conectar()
            cursor = con.cursor()
            sql = 'select * from nota'
            cursor.execute(sql)
            datos = cursor.fetchall()
            con.close()
        except mysql.Error as err:
            print('Ha ocrrido un error ', err)
        return datos

    def buscar(self):
        datos = []
        try:
            con = conectar()
            cursor = con.cursor()
            sql = f'select * from nota where id={self.id}'
            cursor.execute(sql)
            datos = cursor.fetchall()
            con.close()
        except mysql.Error as err:
            print('Ha ocrrido un error ', err)
        return datos

    def eliminar(self):
        try:
            con = conectar()
            cursor = con.cursor()
            sql = f'delete from nota where id={self.id}'
            cursor.execute(sql)
            con.commit()
            con.close()
            return 'Se ha eliminado'
        except mysql.Error as err:
            print('Ha ocrrido un error ', err)