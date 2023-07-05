class Plan():

    _id:str
    _nombre:str
    _costo:int
    _descricion:str
    _persona_id:str

    def __init__(self, id, nombre, costo, descripcion, persona_id):
        self._id = id
        self._nombre = nombre
        self._costo = costo
        self._descricion = descripcion
        self._persona_id =persona_id