import mysql.connector as cx
from Capas_log.Logger import log

def establecer_conexion():
    try:
        return cx.connect(
            host="localhost",
            user="root",
            password="root",
            database="centro_salud"
        )
    except cx.Error as e:
        log.error("Error al conectar a la base de datos:", e)

