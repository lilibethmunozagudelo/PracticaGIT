import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='root',
                db='example_crud'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarPersonas(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM personas ORDER BY nombre ASC")
                resultados=cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarPersona(self, persona):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="INSERT INTO personas (Identificacion, nombre, edad) VALUES ('{0}','{1}',{2})"
                cursor.execute(sql.format(persona[0], persona[1], persona[2]))
                self.conexion.commit()
                print("Persona registrada\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarPersona(self, persona):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="UPDATE personas SET nombre = '{0}', edad = {1} WHERE identificacion = '{2}'"
                cursor.execute(sql.format(persona[1], persona[2], persona[0]))
                self.conexion.commit()
                print("Persona actualizada\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarPersona(self, identificacion):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="DELETE FROM personas WHERE identificacion = '{0}'"
                cursor.execute(sql.format(identificacion))
                self.conexion.commit()
                print("Persona eliminada\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))