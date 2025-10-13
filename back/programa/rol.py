class Rol:
    def __init__(self, id):
        self.__id = id
        self.__descripcion = self._definir_descripcion(id)

    def _definir_descripcion(self, id):
        if id == 1:
            return "Admin"
        elif id == 2:
            return "Usuario"
        else:
            return "Estandar"

    @property
    def id(self):
        return self.__id

    @property
    def descripcion(self):
        return self.__descripcion

    def __str__(self):
        return self.__descripcion