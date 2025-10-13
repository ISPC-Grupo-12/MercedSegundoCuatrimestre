import re
from persistencia import crear_conexion

class Validador:
    def validar_opcion(self, min, max):
        while True:
            try:
                opcion = int(input("Opción: "))
                if min <= opcion <= max:
                    return opcion
                else:
                    print(f"❌ Error. Ingrese un valor entre {min} y {max}.\n")
            except ValueError:
                print("❌ Por favor, ingresá un número válido.\n")

    def validar_mail_patron(self, mail):
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(patron, mail) is not None

    def validar_mail_repetido(self, mail):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT 1 FROM usuarios WHERE mail = ?", (mail,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado is None  # True si no existe, False si ya está registrado

    def validar_contrasena(self, contrasena):
        if len(contrasena) < 6:
            print("❌ La contraseña debe tener al menos 6 caracteres.")
            return False
        contiene_letra = any(caracter.isalpha() for caracter in contrasena)
        contiene_numeros = any(caracter.isdigit() for caracter in contrasena)
        if not contiene_letra or not contiene_numeros:
            print("❌ La contraseña debe contener letras y números.")
        return contiene_letra and contiene_numeros

    def validar_dni(self, dni):
        patron = r"^\d{8}$"
        if not re.match(patron, dni):
            print("❌ El DNI debe tener exactamente 8 dígitos.")
            return False
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT 1 FROM usuarios WHERE DNI = ?", (dni,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado is None  # True si no existe, False si ya está registrado

    def validar_str(self, cadena):
        patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$"
        return re.match(patron, cadena) is not None