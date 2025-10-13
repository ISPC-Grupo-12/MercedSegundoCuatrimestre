from persistencia import crear_conexion

class Gestor_producto:
    def __init__(self):
        pass

    def registrar_producto(self, nombre, precio, descripcion, imagen):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO productos (nombre, precio, descripcion, imagen)
            VALUES (?, ?, ?, ?)
        """, (nombre, precio, descripcion, imagen))
        conexion.commit()
        cursor.close()
        conexion.close()

    def crear_producto(self, nombre, precio, descripcion):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO productos (nombre, precio, descripcion)
            VALUES (?, ?, ?)
        """, (nombre, precio, descripcion))
        conexion.commit()
        cursor.close()
        conexion.close()

    def listar_productos(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, precio, descripcion FROM productos")
        productos = cursor.fetchall()
        for p in productos:
            print(f"🆔 {p[0]} | 📦 {p[1]} | 💲{p[2]} | 📝 {p[3]}")
        cursor.close()
        conexion.close()

    def buscar_producto(self, id_producto):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE id_producto = ?", (id_producto,))
        producto = cursor.fetchone()
        cursor.close()
        conexion.close()
        return producto

    def buscar_por_nombre(self, nombre):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_producto, nombre, precio, descripcion
            FROM productos
            WHERE nombre LIKE ?
        """, ('%' + nombre + '%',))
        productos = cursor.fetchall()
        for p in productos:
            print(f"🆔 {p[0]} | 📦 {p[1]} | 💲{p[2]} | 📝 {p[3]}")
        cursor.close()
        conexion.close()

    def filtrar_por_precio(self, minimo, maximo):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_producto, nombre, precio, descripcion
            FROM productos
            WHERE precio BETWEEN ? AND ?
        """, (minimo, maximo))
        productos = cursor.fetchall()
        for p in productos:
            print(f"🆔 {p[0]} | 📦 {p[1]} | 💲{p[2]} | 📝 {p[3]}")
        cursor.close()
        conexion.close()

    def modificar_producto(self, id_producto, campo_opcion, nuevo_valor):
        campos = {
            1: "nombre",
            2: "precio",
            3: "descripcion",
            4: "imagen"
        }

        campo = campos.get(campo_opcion)
        if not campo:
            return False

        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute(f"""
            UPDATE productos
            SET {campo} = ?
            WHERE id_producto = ?
        """, (nuevo_valor, id_producto))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True

    def eliminar_producto(self, id_producto):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = ?", (id_producto,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True