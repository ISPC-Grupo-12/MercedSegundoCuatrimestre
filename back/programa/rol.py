class Rol:
    def __init__(self, id):
        self.__id = id
        self.__descripcion = "Estandar" if id == 0 else "Admin"
    
    def __str__(self):
        return self.__descripcion 
    
    @property
    def id(self):
        return self.__id
