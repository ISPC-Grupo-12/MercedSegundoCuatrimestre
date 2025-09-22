from persistencia import crear_conexion
from usuario import Usuario
from rol import Rol

class Gestor_usuario:
    def __init__(self):
        pass

    def registrar_usuario(self, nombre, apellido, mail, contrasena, dni):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Usuario (rol_id, nombre, apellido, mail, contrasena, dni)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (2, nombre, apellido, mail, contrasena, dni))
        conexion.commit()
        cursor.close()
        conexion.close()

    def login_usuario(self, mail, contrasena):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_usuario, nombre, apellido, mail, contrasena, dni, rol_id
            FROM Usuario
            WHERE mail = ? AND contrasena = ?
        """, (mail, contrasena))
        fila = cursor.fetchone()
        cursor.close()
        conexion.close()

        if fila:
            rol_obj = Rol(fila[6])
            usuario = Usuario(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], rol_obj)
            print(f"✅ Bienvenido, {usuario.nombre}!\n")
            return usuario
        else:
            print("❌ Credenciales inválidas.")
            return None

    def listar_usuarios(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Usuario")
        usuarios = cursor.fetchall()
        for u in usuarios:
            print(u)
        cursor.close()
        conexion.close()

    def buscar_usuario(self, id):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_usuario, nombre, apellido, mail, contrasena, dni, rol_id
            FROM Usuario
            WHERE id_usuario = ?
        """, (id,))
        fila = cursor.fetchone()
        cursor.close()
        conexion.close()

        if fila:
            rol_obj = Rol(fila[6])
            return Usuario(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], rol_obj)
        return None

    def modificar_datos(self, id, dato_opcion, dato_valor):
        campos = {
            1: "nombre",
            2: "apellido",
            3: "mail",
            4: "dni",
            5: "contrasena"
        }

        campo = campos.get(dato_opcion)
        if not campo:
            return False

        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute(f"""
            UPDATE Usuario
            SET {campo} = ?
            WHERE id_usuario = ?
        """, (dato_valor, id))
        conexion.commit()
        cursor.close()
        conexion.close()

        return True

    def eliminar_usuario(self, id):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            DELETE FROM Usuario
            WHERE id_usuario = ?
        """, (id,))
        conexion.commit()
        cursor.close()
        conexion.close()

        return True

    def modificar_rol(self, id, id_rol):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Usuario
            SET rol_id = ?
            WHERE id_usuario = ?
        """, (id_rol, id))
        conexion.commit()
        cursor.close()
        conexion.close()

        return True