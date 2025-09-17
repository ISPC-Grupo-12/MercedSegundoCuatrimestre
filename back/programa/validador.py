import re
from persistencia import crear_conexion

class Validador:
    def validar_opcion(self, min, max):
        while True:
            try:
                opcion = int(input("Opción:"))
                if min <= opcion <= max:
                    return opcion
                else:
                    print(f"Error. Ingrese un valor entre {min} y {max}.\n")
            except ValueError:
                print("Por favor, ingresá un número válido.\n")

    def validar_email_patron(self, email):
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(patron, email) is not None

    def validar_email_repetido(self, email):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT 1 FROM usuarios WHERE Email = ?", (email,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado is None  # True si no existe, False si ya está registrado

    def validar_contraseña(self, contraseña):
        if len(contraseña) < 6:
            return False
        contiene_letra = any(caracter.isalpha() for caracter in contraseña)
        contiene_numeros = any(caracter.isdigit() for caracter in contraseña)
        return contiene_letra and contiene_numeros

    def validar_dni(self, dni):
        patron = r"^\d{8}$"
        if not re.match(patron, dni):
            return False
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT 1 FROM usuarios WHERE DNI = ?", (dni,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado is None  # True si no existe, False si ya está registrado

    def validar_str(self, cadena):
        patron = r"^[a-zA-Z ]+$"
        return re.match(patron, cadena) is not None