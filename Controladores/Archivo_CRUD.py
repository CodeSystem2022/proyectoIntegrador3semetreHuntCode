from Conexion.Bd_conexion import establecer_conexion
from Capas_log.Logger import log


# Aca empieza el CRUD

def crear_registro(nombre, apellido, contraseña, email=None):
    try:
        conexion = establecer_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO individuos (nombre, apellido, contraseña, email) VALUES (%s, %s, %s, %s)"
            valores = (nombre, apellido, contraseña, email)
            cursor.execute(sql, valores)
        conexion.commit()
        log.debug("Registro creado exitosamente.")
    except Exception as e:
        log.error("Error al crear el registro:", e)
        if conexion:
            conexion.rollback()
    finally:
        if conexion:
            conexion.close()
            log.debug("Conexión cerrada")


def obtener_registros():
    try:
        conexion = establecer_conexion()
        with conexion:
            with conexion.cursor() as cursor:
                sql = "SELECT * FROM individuos"
                cursor.execute(sql)
                registros = cursor.fetchall()
                return registros
    except Exception as e:
        log.error(f'Ocurrio un error, se hizo un rollback: {e}')
    finally:
        conexion.close()

print('Termina la transaccion.')


def obtener_registro_por_id(idIndividuo):
    try:
        conexion = establecer_conexion()
        with conexion:
            with conexion.cursor() as cursor:
                sql = "SELECT * FROM individuos WHERE idIndividuo = %s"
                valores = (idIndividuo,)
                cursor.execute(sql, valores)
                registro = cursor.fetchone()
                return registro
    except Exception as e:
        log.error(f'Ocurrio un error, se hizo un rollback: {e}')
    finally:
        conexion.close()


def actualizar_registro(idIndividuo, nombre, apellido, contraseña, email):
    try:
        conexion = establecer_conexion()
        with conexion:
            with conexion.cursor() as cursor:
                sql = "UPDATE individuos SET nombre = %s, apellido = %s, contraseña = %s, email = %s WHERE idIndividuo = %s"
                valores = (nombre, apellido, contraseña, email, idIndividuo)
                cursor.execute(sql, valores)
    except Exception as e:
        log.error(f'Ocurrio un error, se hizo un rollback: {e}')
    finally:
        conexion.close()


def eliminar_registro(idIndividuo):
    try:
        conexion = establecer_conexion()
        with conexion:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM personas WHERE idIndividuo = %s"
                valores = (idIndividuo,)
                cursor.execute(sql, valores)
    except Exception as e:
        log.error(f'Ocurrio un error, se hizo un rollback: {e}')
    finally:
        conexion.close()