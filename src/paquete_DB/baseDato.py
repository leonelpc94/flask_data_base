import psycopg2
from decouple import config

class Base_dato():

    _instancia = None
    _conexion = psycopg2.connect(host = 'localhost',
                                 user = 'admin',
                                 password = 'fallout',
                                 DB = 'postgres')

    @staticmethod
    def instancia():
        if Base_dato._instancia == None:
            Base_dato._instancia = Base_dato()
        return Base_dato._instancia

    def registroPersona(self,id, nombre, clave, email, telefono):
        try:
            self._conexion.cursor().execute('INSERT INTO persona (id , nombre, clave,email, telefono) VALUES(%s,%s,%s,%s,%s)',
                                            (id,nombre,clave,email,telefono))
            self._conexion.commit()
            self._conexion.close()
            return True
        except psycopg2.Error:
            return False

    def registroPlan(self):
        pass

    def listaPlan(self):
        pass

    def inicioSeccion(self):
        pass

    def eliminarCuenta(self):
        pass

    def eliminarPlan(self):
        pass
