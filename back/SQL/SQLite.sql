-- Eliminar tablas si existen
DROP TABLE IF EXISTS Detalle_pedido;
DROP TABLE IF EXISTS Pedido;
DROP TABLE IF EXISTS Detalle_carrito;
DROP TABLE IF EXISTS Carrito;
DROP TABLE IF EXISTS Producto;
DROP TABLE IF EXISTS Usuario;
DROP TABLE IF EXISTS rol;

-- Tabla de roles (opcional, si querés mantenerla separada)
CREATE TABLE rol (
    id_rol INTEGER PRIMARY KEY,
    descripcion TEXT NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insertar roles
INSERT INTO rol (id_rol, descripcion) VALUES (1, 'admin');
INSERT INTO rol (id_rol, descripcion) VALUES (2, 'usuario');

-- Tabla de usuarios con campos extendidos
CREATE TABLE Usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    mail TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL,
    rol_id INTEGER NOT NULL,
    dni TEXT NOT NULL UNIQUE,
    estado INTEGER DEFAULT 1,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (rol_id) REFERENCES rol(id_rol)
);

-- Tabla de productos
CREATE TABLE Producto (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL CHECK (precio > 0),
    stock INTEGER NOT NULL CHECK (stock > 0),
    categoria TEXT NOT NULL
);

-- Tabla de carritos
CREATE TABLE Carrito (
    id_carrito INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL UNIQUE,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
);

-- Detalle del carrito
CREATE TABLE Detalle_carrito (
    id_carrito INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unitario REAL NOT NULL CHECK (precio_unitario > 0),
    subtotal REAL GENERATED ALWAYS AS (precio_unitario * cantidad) STORED,
    PRIMARY KEY (id_carrito, id_producto),
    FOREIGN KEY (id_carrito) REFERENCES Carrito(id_carrito) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
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
    id_producto INTEGER NOT NULL,
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unitario REAL NOT NULL CHECK (precio_unitario > 0),
    subtotal REAL GENERATED ALWAYS AS (precio_unitario * cantidad) STORED,
    PRIMARY KEY (id_pedido, id_producto),
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);






