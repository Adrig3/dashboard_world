import pymysql
from pymysql.err import MySQLError

def get_connection():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='usuario_world',
            password='1234',
            database='world',
            cursorclass=pymysql.cursors.DictCursor  # para obtener resultados como diccionario
        )
        return connection
    except MySQLError as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
