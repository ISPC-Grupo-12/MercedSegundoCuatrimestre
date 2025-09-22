class Rol:
    def __init__(self, id):
        self.__id = id
        if id == 1:
            self.__descripcion = "Admin"
        elif id == 2:
            self.__descripcion = "Usuario"
        else:
            self.__descripcion = "Estandar"

    def __str__(self):
        return self.__descripcion

    @property
    def id(self):
        return self.__id