import pymysql
from pymysql.err import MySQLError

class Conexion:
    def __init__(self):
        print("Objeto tipo Conexion creado y listo para usarse..!!")
        self.conect = None  # Inicializamos la conexión como None

    def conectar(self):
        """
        Método para conectar a la base de datos.
        """
        try:
            self.conect = pymysql.connect(
                host="sql10.freemysqlhosting.net",
                user="sql10753480",
                password="2ALlslh4U3",
                database="sql10753480",
                port=3306,
                connect_timeout=10  # Tiempo máximo de espera para la conexión
            )
            print("Conexión lista para usarse ...!!")
            return self.conect
        except MySQLError as error:
            print("Error al intentar abrir la conexión:")
            print(error)  # Imprime el error específico de MySQL
        except Exception as ex:
            print("Excepción inesperada:")
            print(ex)  # Imprime cualquier otro tipo de error inesperado

    def desconectar(self):
        """
        Método para cerrar la conexión a la base de datos.
        """
        if self.conect:
            try:
                self.conect.close()
                print("Conexión cerrada ..!!")
            except MySQLError as error:
                print("Error al intentar cerrar la conexión:")
                print(error)
        else:
            print("No hay una conexión activa para cerrar.")

if __name__ == "__main__":
    con = Conexion()  # Crear una instancia de la clase
    connection = con.conectar()  # Intentar conectar
    if connection:  # Verificar si la conexión fue exitosa
        try:
            print("Ejecutando operaciones con la base de datos...")
            # Aquí puedes realizar operaciones como consultas
        finally:
            con.desconectar()  # Cerrar la conexión al finalizar
