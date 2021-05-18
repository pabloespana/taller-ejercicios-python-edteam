from conexion import *

def registrar(nombre, apellidos, empresa, telefono, email, direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' INSERT INTO contacto(
            nombre, apellidos, empresa, telefono, email, direccion) values 
            ( ?, ?, ?, ?, ?, ? ) '''
        datos = (nombre, apellidos, empresa, telefono, email, direccion)
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return 'Registro correcto'
    except sqlite3.Error as err:
        print('Ha ocurrido un error', err)

def mostrar():
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' SELECT * FROM contacto ''' 
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        con.close()
    except sqlite3.Error as err:
        print('Ha ocurrido un error', err)
    return datos

def buscar(id):
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = '''SELECT * FROM contacto WHERE id=?'''
        cursor.execute(sentencia_sql, (id,))
        datos = cursor.fetchall()
        con.close()
    except sqlite3.Error as err:
        print('Ha ocrrido un error', err)
    return datos

def modificar(id, nombre, apellidos, empresa, telefono, email, direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql  = ''' UPDATE contacto SET nombre=?, apellidos=?, 
        empresa=?, telefono=?, email=?, direccion=? WHERE id=? '''
        datos = (nombre, apellidos, empresa, telefono, email, direccion, id)
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return "Se actualizó correctamente"
    except sqlite3.Error as err:
        print('Ha ocurrido un error', err)

def eliminar(id):
    try:
        con = conectar()
        cursor= con.cursor()
        sentencia_sql = '''DELETE FROM contacto where id=?'''
        cursor.execute(sentencia_sql, (id,))
        con.commit()
        con.close()
        return "Se eliminó correctamente"
    except sqlite3.Error as err:
        print('Ha ocurrido un error', err)