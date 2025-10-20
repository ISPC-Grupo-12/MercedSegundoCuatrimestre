from persistencia import crear_conexion
from datetime import datetime

class Gestor_pedido:
    def __init__(self):
        pass

    def realizar_pedido(self, id_usuario, id_producto):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO pedidos (id_usuario, id_producto, fecha)
            VALUES (?, ?, ?)
        """, (id_usuario, id_producto, fecha))
        conexion.commit()
        cursor.close()
        conexion.close()

    def ver_pedidos_por_usuario(self, id_usuario):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT pedidos.id_pedido, productos.nombre, pedidos.fecha
            FROM pedidos
            JOIN productos ON pedidos.id_producto = productos.id_producto
            WHERE pedidos.id_usuario = ?
            ORDER BY pedidos.fecha DESC
        """, (id_usuario,))
        pedidos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return pedidos
    def ver_todos_los_pedidos(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT pedidos.id_pedido, usuarios.nombre || ' ' || usuarios.apellido AS usuario,
            productos.nombre AS producto, pedidos.fecha
            FROM pedidos
            JOIN usuarios ON pedidos.id_usuario = usuarios.id_usuario
            JOIN productos ON pedidos.id_producto = productos.id_producto
            ORDER BY pedidos.fecha DESC
            """)
        pedidos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return pedidos