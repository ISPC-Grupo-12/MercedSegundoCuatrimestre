-- Eliminar tablas si existen
DROP TABLE IF EXISTS detalle_pedido;
DROP TABLE IF EXISTS pedido;
DROP TABLE IF EXISTS detalle_carrito;
DROP TABLE IF EXISTS carrito;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS rol;

-- Tabla de roles
CREATE TABLE rol (
    id_rol INTEGER PRIMARY KEY,
    descripcion TEXT NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insertar roles
INSERT INTO rol (id_rol, descripcion) VALUES (1, 'admin');
INSERT INTO rol (id_rol, descripcion) VALUES (2, 'usuario');

-- Tabla de usuarios
CREATE TABLE usuarios (
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
CREATE TABLE productos (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL CHECK (precio > 0),
    stock INTEGER NOT NULL CHECK (stock > 0),
    categoria TEXT NOT NULL
);

-- Tabla de carritos
CREATE TABLE carrito (
    id_carrito INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL UNIQUE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Detalle del carrito
CREATE TABLE detalle_carrito (
    id_carrito INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unitario REAL NOT NULL CHECK (precio_unitario > 0),
    subtotal REAL, -- si tu SQLite no soporta GENERATED
    PRIMARY KEY (id_carrito, id_producto),
    FOREIGN KEY (id_carrito) REFERENCES carrito(id_carrito) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Tabla de pedidos
CREATE TABLE pedido (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    fecha DATE NOT NULL,
    estado TEXT NOT NULL,
    total REAL NOT NULL CHECK (total > 0),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Detalle del pedido
CREATE TABLE detalle_pedido (
    id_pedido INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unitario REAL NOT NULL CHECK (precio_unitario > 0),
    subtotal REAL, -- si tu SQLite no soporta GENERATED
    PRIMARY KEY (id_pedido, id_producto),
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);