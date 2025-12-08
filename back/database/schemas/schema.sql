--Schema realizado en mysql para crear el modelo relacional
-- Eliminamos las tablas si existen 
DROP TABLE IF EXISTS Detalle_pedido;
DROP TABLE IF EXISTS Pedido;
DROP TABLE IF EXISTS Detalle_carrito;
DROP TABLE IF EXISTS Carrito;
DROP TABLE IF EXISTS Variante_producto;
DROP TABLE IF EXISTS Producto;
DROP TABLE IF EXISTS Usuario;
DROP TABLE IF EXISTS Rol;

-- Tabla Rol
CREATE TABLE Rol (
    id_rol INT PRIMARY KEY,
    descripcion VARCHAR(50) NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
)

-- Valores de Rol por defecto
INSERT INTO Rol (id_rol, descripcion)
VALUES (1, 'admin'), (2, 'usuario');

-- Tabla Usuario
CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    mail VARCHAR(150) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    dni VARCHAR(20) NOT NULL UNIQUE,
    rol_id INT NOT NULL,
    estado TINYINT DEFAULT 1,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_usuario_rol
        FOREIGN KEY (rol_id) REFERENCES Rol(id_rol)
)

-- Tabla Producto
CREATE TABLE Producto (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT NOT NULL,
    categoria VARCHAR(100),
    precio DECIMAL(10,2) NOT NULL CHECK (precio > 0)
) 

-- Tabla de las Variantes de los productos
CREATE TABLE Variante_producto (
    id_variante INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT NOT NULL,
    talle VARCHAR(10) NOT NULL,
    color VARCHAR(50) NOT NULL,
    stock INT NOT NULL CHECK (stock >= 0),
    CONSTRAINT fk_variante_producto
        FOREIGN KEY (id_producto)
        REFERENCES Producto(id_producto)
        ON DELETE CASCADE,
    CONSTRAINT uq_producto_talle_color
        UNIQUE (id_producto, talle, color)
)


-- Tabla Carrito(unico)
CREATE TABLE Carrito (
    id_carrito INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL UNIQUE,
    CONSTRAINT fk_carrito_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES Usuario(id_usuario)
        ON DELETE CASCADE
)

-- Detalles del carrito
CREATE TABLE Detalle_carrito (
    id_carrito INT NOT NULL,
    id_variante INT NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    precio_unitario DECIMAL(10,2) NOT NULL CHECK (precio_unitario > 0),
    subtotal DECIMAL(10,2)
        GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
    PRIMARY KEY (id_carrito, id_variante),
    CONSTRAINT fk_detalle_carrito_carrito
        FOREIGN KEY (id_carrito)
        REFERENCES Carrito(id_carrito)
        ON DELETE CASCADE,
    CONSTRAINT fk_detalle_carrito_variante
        FOREIGN KEY (id_variante)
        REFERENCES Variante_producto(id_variante)
)

-- Tabla Pedido
CREATE TABLE Pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    fecha DATE NOT NULL,
    estado VARCHAR(50) NOT NULL,
    total DECIMAL(10,2) NOT NULL CHECK (total > 0),
    CONSTRAINT fk_pedido_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES Usuario(id_usuario)
        ON DELETE CASCADE
)

-- Detalles de los pedidos
CREATE TABLE Detalle_pedido (
    id_pedido INT NOT NULL,
    id_variante INT NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    precio_unitario DECIMAL(10,2) NOT NULL CHECK (precio_unitario > 0),
    subtotal DECIMAL(10,2)
        GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
    PRIMARY KEY (id_pedido, id_variante),
    CONSTRAINT fk_det_pedido_pedido
        FOREIGN KEY (id_pedido)
        REFERENCES Pedido(id_pedido)
        ON DELETE CASCADE,
    CONSTRAINT fk_det_pedido_variante
        FOREIGN KEY (id_variante)
        REFERENCES Variante_producto(id_variante)
)