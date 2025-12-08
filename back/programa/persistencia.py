import sqlite3
import os

def crear_conexion():
    ruta_base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "merced.db"))
    return sqlite3.connect(ruta_base)

def crear_tablas():
    conexion = crear_conexion()
    cursor = conexion.cursor()

    # Roles por defecto
    cursor.execute("INSERT OR IGNORE INTO Rol (id_rol, descripcion) VALUES (1, 'admin')")
    cursor.execute("INSERT OR IGNORE INTO Rol (id_rol, descripcion) VALUES (2, 'usuario')")

    # Usuario admin por defecto
    cursor.execute("""
    INSERT OR IGNORE INTO Usuario (id_usuario, rol_id, nombre, apellido, mail, contrasena, dni)
    VALUES (1, 1, 'Admin', 'Principal', 'admin@merced.com', 'admin123', '00000000')
    """)

 
    conexion.commit()
    cursor.close()
    conexion.close()
    print("✅ Tablas creadas correctamente.")