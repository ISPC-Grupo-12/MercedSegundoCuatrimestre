import sqlite3

def crear_conexion():
    # Crea (o abre) la base de datos llamada "merced.db"
    return sqlite3.connect("merced.db")

def crear_tablas():
    conexion = crear_conexion()
    cursor = conexion.cursor()

    # Crear tabla de roles
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rol (
        Id_Rol INTEGER PRIMARY KEY,
        Descripcion TEXT NOT NULL,
        FechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Crear tabla de usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        Id_Usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        Rol_Id INTEGER NOT NULL,
        Nombre TEXT NOT NULL,
        Apellido TEXT NOT NULL,
        Email TEXT UNIQUE NOT NULL,
        Contraseña TEXT NOT NULL,
        DNI TEXT,
        Estado INTEGER DEFAULT 1,
        FechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (Rol_Id) REFERENCES rol(Id_Rol)
    )
    """)

    # Insertar roles si no existen
    cursor.execute("INSERT OR IGNORE INTO rol (Id_Rol, Descripcion) VALUES (1, 'admin')")
    cursor.execute("INSERT OR IGNORE INTO rol (Id_Rol, Descripcion) VALUES (2, 'usuario')")

    conexion.commit()
    cursor.close()
    conexion.close()
    print("✅ Tablas creadas correctamente.")