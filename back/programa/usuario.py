from rol import Rol
class Usuario:
    #contructor
    def __init__(self, id, nombre, apellido, email, contraseña, dni, rol: Rol):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contraseña = contraseña
        self.__rol = rol
        self.__dni = dni

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
    def email(self):
        return self.__email
    @email.setter
    def email(self, nuevo_email):
        self.__email = nuevo_email

    @property
    def contraseña(self):
        return self.__contraseña
    @contraseña.setter
    def contraseña(self, nuevo_contraseña):
        self.__contraseña = nuevo_contraseña

    @property
    def rol(self):
        return self.__rol
    @rol.setter
    def rol(self, nuevo_rol):
        self.__rol = nuevo_rol

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, nuevo_dni):
        self.__dni = nuevo_dni


    #métodos 
    def es_admin(self):
        return self.__rol.id == 1  #En vez de revistar un str, revisa el id del Rol
    
    def validar_login(self, email, contraseña):
        return self.__email == email and self.__contraseña == contraseña
    
    def __str__(self):
        return f"\nID: {self.__id}\nNombre completo: {self.__apellido}, {self.__nombre}\nDni: {self.__dni}\nEmail: {self.__email}\nRol: {self.__rol}"

