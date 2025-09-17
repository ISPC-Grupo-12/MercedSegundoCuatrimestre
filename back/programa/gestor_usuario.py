from persistencia import crear_conexion
from usuario import Usuario
from rol import Rol

class Gestor_usuario:
    def __init__(self):
        pass  # Ya no necesitás self.__usuarios

    def registrar_usuario(self, nombre, apellido, email, contraseña, dni):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO usuarios (Rol_Id, Nombre, Apellido, Email, Contraseña, DNI)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (2, nombre, apellido, email, contraseña, dni))
        conexion.commit()
        cursor.close()
        conexion.close()

    def login_usuario(self, email, contraseña):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT Id_Usuario, Nombre, Apellido, Email, Contraseña, DNI, Rol_Id
            FROM usuarios
            WHERE Email = ? AND Contraseña = ?
        """, (email, contraseña))
        fila = cursor.fetchone()
        cursor.close()
        conexion.close()

        if fila:
            rol = Rol(fila[6])
            usuario = Usuario(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], rol)
            print(f"✅ Bienvenido, {usuario.nombre}!\n")
            return usuario
        else:
            print("❌ Credenciales inválidas.")
            return None

    def listar_usuarios(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        for u in usuarios:
            print(u)
        cursor.close()
        conexion.close()

    def buscar_usuario(self, id):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT Id_Usuario, Nombre, Apellido, Email, Contraseña, DNI, Rol_Id
            FROM usuarios
            WHERE Id_Usuario = ?
        """, (id,))
        fila = cursor.fetchone()
        cursor.close()
        conexion.close()

        if fila:
            rol = Rol(fila[6])
            return Usuario(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], rol)
        return None

    def modificar_datos(self, id, dato_opcion, dato_valor):
        campos = {
            1: "Nombre",
            2: "Apellido",
            3: "Email",
            4: "DNI",
            5: "Contraseña"
        }

        campo = campos.get(dato_opcion)
        if not campo:
            return False

        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute(f"""
            UPDATE usuarios
            SET {campo} = ?
            WHERE Id_Usuario = ?
        """, (dato_valor, id))
        conexion.commit()
        cursor.close()
        conexion.close()

        return True

    def eliminar_usuario(self, id):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            DELETE FROM usuarios
            WHERE Id_Usuario = ?
        """, (id,))
        conexion.commit()
        cursor.close()
        conexion.close()

        return True

    def modificar_rol(self, id, id_rol):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE usuarios
            SET Rol_Id = ?
            WHERE Id_Usuario = ?
        """, (id_rol, id))
        conexion.commit()
        cursor.close()
        conexion.close()

        return True