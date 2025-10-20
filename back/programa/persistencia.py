import sqlite3
import os

def crear_conexion():
    ruta_base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "merced.db"))
    return sqlite3.connect(ruta_base)

def crear_tablas():
    conexion = crear_conexion()
    cursor = conexion.cursor()

    # Tabla de roles
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rol (
        Id_Rol INTEGER PRIMARY KEY,
        Descripcion TEXT NOT NULL,
        FechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Tabla de usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        Id_Usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        Rol_Id INTEGER NOT NULL,
        Nombre TEXT NOT NULL,
        Apellido TEXT NOT NULL,
        mail TEXT UNIQUE NOT NULL,
        contrasena TEXT NOT NULL,
        DNI TEXT UNIQUE NOT NULL,
        Estado INTEGER DEFAULT 1,
        FechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (Rol_Id) REFERENCES rol(Id_Rol)
    )
    """)

    # Tabla de productos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio DECIMAL(10,2) NOT NULL,
        descripcion TEXT,
        imagen TEXT
    )
    """)

    # Tabla de pedidos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER NOT NULL,
        id_producto INTEGER NOT NULL,
        fecha TEXT,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(Id_Usuario),
        FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
    )
    """)

    # Roles por defecto
    cursor.execute("INSERT OR IGNORE INTO rol (Id_Rol, Descripcion) VALUES (1, 'admin')")
    cursor.execute("INSERT OR IGNORE INTO rol (Id_Rol, Descripcion) VALUES (2, 'usuario')")

    # Usuario admin por defecto
    cursor.execute("""
    INSERT OR IGNORE INTO usuarios (Id_Usuario, Rol_Id, Nombre, Apellido, mail, contrasena, DNI)
    VALUES (1, 1, 'Admin', 'Principal', 'admin@merced.com', 'admin123', '00000000')
    """)

    conexion.commit()
    cursor.close()
    conexion.close()
    print("✅ Tablas creadas correctamente.")