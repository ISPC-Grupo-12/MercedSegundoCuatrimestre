from rol import Rol

class Usuario:
    def __init__(self, id, nombre, apellido, mail, contrasena, dni, rol: Rol):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__contrasena = contrasena
        self.__dni = dni
        self.__rol = rol

    # Propiedades
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido

    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, nuevo_mail):
        self.__mail = nuevo_mail

    @property
    def contrasena(self):
        return self.__contrasena
    @contrasena.setter
    def contrasena(self, nuevo_contrasena):
        self.__contrasena = nuevo_contrasena

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, nuevo_dni):
        self.__dni = nuevo_dni

    @property
    def rol(self):
        return self.__rol
    @rol.setter
    def rol(self, nuevo_rol):
        self.__rol = nuevo_rol

    # Métodos
    def es_admin(self):
        return self.__rol.id == 1

    def validar_login(self, mail, contrasena):
        return self.__mail == mail and self.__contrasena == contrasena

    def __str__(self):
        return (
            f"\n🆔 ID: {self.__id}"
            f"\n👤 Nombre completo: {self.__apellido}, {self.__nombre}"
            f"\n🪪 DNI: {self.__dni}"
            f"\n📧 Mail: {self.__mail}"
            f"\n🔐 Rol: {self.__rol}"
        )