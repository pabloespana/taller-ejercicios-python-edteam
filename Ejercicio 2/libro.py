from conexion import *

def registrar(titulo, autor, estado):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' INSERT INTO libro (titulo, autor, estado) 
        values (%s, %s, %s)'''
        datos = (titulo, autor, estado)
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return 'Registro correcto'
    except mysql.Error as err:
        print('Ha ocurrido un error', err)

def mostrar():
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = "Select * from libro"
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        con.close()
    except mysql.Error as err:
        print('Ha ocurrido un error', err)
    return datos

def buscar(id):
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = "Select * from libro where id=%s"
        cursor.execute(sentencia_sql, (id,))
        datos = cursor.fetchall()
        con.close()
    except mysql.Error as err:
        print('Ha ocurrido un error', err)
    return datos

def modificar(id, campo, nuevo_valor):
    try:
        sentencia_sql = ''
        con = conectar()
        cursor = con.cursor()
        if campo == '1':
            sentencia_sql = 'UPDATE libro SET titulo=%s WHERE id=%s'
        elif campo == '2':
            sentencia_sql = 'UPDATE libro SET autor=%s WHERE id=%s'
        elif campo == '3':
            sentencia_sql = 'UPDATE libro SET estado=%s WHERE id=%s'
        datos = (nuevo_valor, id)
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return 'Se actualizó correctamente'
    except mysql.Error as err:
        print('Ha ocurrido un error', err)

def eliminar(id):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = 'DELETE FROM libro WHERE id=%s'
        cursor.execute(sentencia_sql, (id,))
        con.commit()
        con.close()
        return 'Se ha eliminado'
    except mysql.Error as err:
        print('Ha ocurrido un error', err)
