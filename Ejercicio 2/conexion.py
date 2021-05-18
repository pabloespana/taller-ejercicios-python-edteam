import mysql.connector as mysql

def conectar():
    try:
        conexion = mysql.connect(
            host='localhost',
            user='root',
            password='',
            database='libros'
            )
        print('Se ha conectado a la base de datos')
        return conexion
    except mysql.Error as err:
        print('Ha ocurrido un error', err)