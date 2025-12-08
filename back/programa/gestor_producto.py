from persistencia import crear_conexion

class Gestor_producto:
    def __init__(self):
        pass


    def crear_producto(self, nombre,descripcion, categoria, precio):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Producto (nombre, descripcion, categoria, precio)
            VALUES (?, ?, ?, ?)
        """, (nombre, descripcion, categoria, precio))
        conexion.commit()
        cursor.close()
        conexion.close()
    
    def agregar_variante(self, id_producto, talle, color, stock):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Variante_producto (id_producto, talle, color, stock)
            VALUES (?, ?, ?, ?)
        """, (id_producto, talle, color, stock))
        conexion.commit()
        cursor.close()
        conexion.close()
    

    def listar_productos(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""SELECT *
                        FROM Producto""")
        productos = cursor.fetchall()
        for p in productos:
            print(f"🆔 {p[0]} | 📦 {p[1]} | 📝 {p[2]} | 📑 {p[3]} | 💲 {p[4]} ")
        cursor.close()
        conexion.close()
        
    def listar_stock(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""SELECT P.id_producto, P.nombre, P.descripcion, P.categoria, P.precio, 
                        Vp.talle, Vp.color, Vp.stock 
                        FROM Producto P
                        LEFT JOIN Variante_producto Vp
                        ON P.id_producto = VP.id_producto;""")
        productos = cursor.fetchall()
        for p in productos:
            print(f"🆔 {p[0]} | 📦 {p[1]} | 📝 {p[2]} | 📑 {p[3]} | 💲 {p[4]} | 🎨  {p[5]} | 👗 {p[6]} | 📦 {p[7]}")
        cursor.close()
        conexion.close()

    def buscar_producto(self, id_producto):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, descripcion, categoria, precio FROM Producto WHERE id_producto = ?", (id_producto,))
        producto = cursor.fetchone()
        cursor.close()
        conexion.close()
        return producto

    def buscar_por_nombre(self, nombre):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_producto, nombre, descripcion, categoria, precio
            FROM Producto
            WHERE nombre LIKE ?
        """, ('%' + nombre + '%',))
        productos = cursor.fetchall()
        for p in productos:
            print(f"🆔 {p[0]} | 📦 {p[1]} | 📝 {p[2]} | 📑 {p[3]} | 💲  {p[4]} ") 
        cursor.close()
        conexion.close()

    def filtrar_por_precio(self, minimo, maximo):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_producto, nombre, descripcion, categoria, precio
            FROM Producto
            WHERE precio BETWEEN ? AND ?
        """, (minimo, maximo))
        productos = cursor.fetchall()
        for p in productos:
            print(f"🆔 {p[0]} | 📦 {p[1]} | 📝 {p[2]} | 📑 {p[3]} | 💲  {p[4]} ")        
        cursor.close()
        conexion.close()
    
    # Filtrar por categoria
    def filtrar_por_categoria(self, categoria):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_producto, nombre, descripcion, categoria, precio
            FROM Producto
            WHERE categoria LIKE ?
        """, ('%' + categoria + '%',))
        productos = cursor.fetchall()
        for p in productos:
            print(f"🆔 {p[0]} | 📦 {p[1]} | 📝 {p[2]} | 📑 {p[3]} | 💲  {p[4]} ")
        cursor.close()
        conexion.close()

    def modificar_producto(self, id_producto, campo_opcion, nuevo_valor):
        campos = {
            1: "nombre",
            2: "precio",
            3: "descripcion"
        }

        campo = campos.get(campo_opcion)
        if not campo:
            return False

        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute(f"""
            UPDATE Producto
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
        cursor.execute("DELETE FROM Producto WHERE id_producto = ?", (id_producto,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True