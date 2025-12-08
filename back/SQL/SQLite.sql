-- Se activan las claves foraneas, por defecto son desactivadas por compatibilidad. 
PRAGMA foreign_keys = ON;
-- Eliminar tablas si existen
DROP TABLE IF EXISTS Detalle_pedido;
DROP TABLE IF EXISTS Pedido;
DROP TABLE IF EXISTS Detalle_carrito;
DROP TABLE IF EXISTS Carrito;
DROP TABLE IF EXISTS Variante_producto;
DROP TABLE IF EXISTS Producto;
DROP TABLE IF EXISTS Usuario;
DROP TABLE IF EXISTS Rol;

-- Tabla de roles (opcional, si querés mantenerla separada)
CREATE TABLE Rol (
    id_rol INTEGER PRIMARY KEY,
    descripcion TEXT NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insertar roles
INSERT INTO Rol (id_rol, descripcion) VALUES (1, 'admin');
INSERT INTO Rol (id_rol, descripcion) VALUES (2, 'usuario');

-- Tabla de usuarios con campos extendidos
CREATE TABLE Usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    mail TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL,
    dni TEXT NOT NULL UNIQUE,
    rol_id INTEGER NOT NULL,
    estado INTEGER DEFAULT 1,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (rol_id) REFERENCES Rol(id_rol)
);

-- Tabla de productos
CREATE TABLE Producto (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    categoria TEXT,
    precio REAL NOT NULL
);

INSERT OR IGNORE INTO Producto (nombre, descripcion, categoria, precio)
    VALUES ("Campera de algodon con botones", "Campera gotica, ideal para combatir el frio con moda.", "campera", 11),
    ("Campera de cuero", "Campera gotica con materiales de primera calida. Su diseño permite no solo combatir el frio, sino ir a la moda.", "campera",30 ),
    ("Remera Gotica", "Remera con diseño unico, su material suave la hace apta para cualquier clima.", "remera", 20),
    ("Vestido delicado", "Vestido corto, su diseño y patrones unicos no solo dejan sorprendido a su dueño pero a todo aquel que lo mire.", "vestido", 21)


-- Tabla de variante producto
CREATE TABLE Variante_producto (
    id_variante INTEGER PRIMARY KEY AUTOINCREMENT,
    id_producto INTEGER NOT NULL,
    talle TEXT NOT NULL,
    color TEXT NOT NULL,
    stock INTEGER NOT NULL,
    UNIQUE (id_producto, talle, color),
    FOREIGN KEY (id_producto)
        REFERENCES Producto(id_producto)
        ON DELETE CASCADE
);

INSERT OR IGNORE INTO Variante_producto(id_producto, talle, color, stock)
    VALUES 
    (1, "S", "negro", 11), (1, "M", "negro", 5), (1, "L", "negro", 10), (1, "XL", "negro", 12), (1, "XL", "rojo", 2),
    (2, "S", "negro", 6), (2, "M", "negro", 8), (2, "L", "negro", 10), (2, "XL", "negro", 11), (2, "XL", "verde", 3),    
    (3, "XL", "negro", 15), (3, "XL", "blanco", 16), 
    (4, "L", "rojo", 10), (4, "XL", "rojo", 11), (4, "XL", "negro", 8)

-- Tabla de carritos
CREATE TABLE Carrito (
    id_carrito INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL UNIQUE,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
);

-- Detalle del carrito
CREATE TABLE Detalle_carrito (
    id_carrito INTEGER NOT NULL,
    id_variante INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    subtotal REAL GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
    PRIMARY KEY (id_carrito, id_variante),
    FOREIGN KEY (id_carrito)
        REFERENCES Carrito(id_carrito)
        ON DELETE CASCADE,
    FOREIGN KEY (id_variante)
        REFERENCES Variante_producto(id_variante)
);

-- Tabla de pedidos
CREATE TABLE Pedido (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    fecha DATE NOT NULL,
    estado TEXT NOT NULL,
    total REAL NOT NULL CHECK (total > 0),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
);

-- Detalle del pedido
CREATE TABLE Detalle_pedido (
    id_pedido INTEGER NOT NULL,
    id_variante INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    subtotal REAL GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
    PRIMARY KEY (id_pedido, id_variante),
    FOREIGN KEY (id_pedido)
        REFERENCES Pedido(id_pedido)
        ON DELETE CASCADE,
    FOREIGN KEY (id_variante)
        REFERENCES Variante_producto(id_variante)
);

