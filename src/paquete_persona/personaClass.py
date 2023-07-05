from abc import ABC
from abc import abstractmethod
class Persona(ABC):

    @abstractmethod
    def reservaPlan(self):
        pass

    @abstractmethod
    def publicarPlan(self):
        pass

class Juridica(Persona):

    _NIT:str
    _nombre:str
    _clave:str
    _email:str
    _telefono:str

    def __init__(self,NIT,nombre,clave,email,telefono):
        self._NIT = NIT
        self._nombre = nombre
        self._clave = clave
        self._email = email
        self._telefono = telefono

    def publicarPlan(self):
        pass

    def reservaPlan(self):
        pass

    def getNombre(self):
        return self._nombre

class Natural(Persona):

    _CC: str
    _nombre: str
    _clave: str
    _email: str
    _telefono: str

    def __init__(self, CC, nombre, clave, email, telefono):
        self._CC = CC
        self._nombre = nombre
        self._clave = clave
        self._email = email
        self._telefono = telefono

    def publicarPlan(self):
        pass

    def reservaPlan(self):
        pass

    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre = nombre