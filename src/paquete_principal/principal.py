from src.paquete_DB.baseDato import Base_dato
from src.paquete_fabrica.fabricaClass import ProducirFabrica
class Principal():

    _instancia:None

    @staticmethod
    def instancia():
        if Principal._instancia == None:
            Principal._instancia = Principal()
        return Principal._instancia

    def fabricaPersona(self,tipo, id, nombre, clave, email, telefono):
        tipoFabrica = 'persona'
        fabrica = ProducirFabrica()
        DB = Base_dato.instancia()
        fabrica_persona = fabrica.fabrica(tipoFabrica)
        print(DB.registroPersona(id, nombre, clave, email, telefono))
        persona = fabrica_persona.fabricaPersona(tipo, id, nombre, clave, email, telefono)
        return persona