from abc import ABC
from abc import abstractmethod
from src.paquete_persona.personaClass import Juridica
from src.paquete_persona.personaClass import Natural
from src.paquete_plan.planClass import Plan

class ProducirFabrica():

    def fabrica(self,tipo):
        if tipo == 'persona':
            fabrica_persona = FabricaPersona()
            return fabrica_persona
        elif tipo == 'plan':
            fabrica_plan = FabricaPlan()
            return fabrica_plan


class InterfaceFabrica(ABC):

    @abstractmethod
    def fabricaPersona(self,tipo,tipoPersona, nombre, clave, email, telefono):
        pass

    @abstractmethod
    def fabricaPlan(self,tipo, id, nombre, costo, descripcion, persona_id):
        pass


class FabricaPersona(InterfaceFabrica):

    def fabricaPersona(self, tipo, tipoPersona, nombre, clave, email, telefono):
        if tipo == 'juridica':
            persona_juridica = Juridica(tipoPersona, nombre, clave, email, telefono)
            return persona_juridica
        elif tipo == 'natural':
            perosna_natural = Natural(tipoPersona, nombre, clave, email, telefono)
            return perosna_natural

    def fabricaPlan(self,tipo, id, nombre, costo, descripcion, persona_id):
        pass


class FabricaPlan(InterfaceFabrica):

    def fabricaPersona(self,tipo,tipoPersona, nombre, clave, email, telefono):
        pass

    def fabricaPlan(self,tipo, id, nombre, costo, descripcion, persona_id):
        if tipo == 'plan':
            plan =Plan(id, nombre, costo, descripcion, persona_id)
            return plan