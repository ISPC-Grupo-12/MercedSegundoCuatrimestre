-- Crear base de datos
CREATE DATABASE IF NOT EXISTS Tienda_Virtual;
USE Tienda_Virtual;

-- Eliminar tablas si existen (en orden por dependencias)
DROP TABLE IF EXISTS Detalle_pedido;
DROP TABLE IF EXISTS Pedido;
DROP TABLE IF EXISTS Detalle_carrito;
DROP TABLE IF EXISTS Carrito;
DROP TABLE IF EXISTS Producto;
DROP TABLE IF EXISTS Usuario;
DROP TABLE IF EXISTS Rol;

-- Tabla de roles
CREATE TABLE Rol (
    Id_Rol INT PRIMARY KEY AUTO_INCREMENT,
    Descripcion VARCHAR(50) NOT NULL,
    FechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insertar roles
INSERT INTO Rol (Id_Rol, Descripcion) VALUES (1, 'admin');
INSERT INTO Rol (Id_Rol, Descripcion) VALUES (2, 'usuario');

-- Tabla de usuarios
CREATE TABLE Usuario (
    Id_Usuario INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Contrasena VARCHAR(100) NOT NULL,
    Rol_Id INT NOT NULL,
    DNI VARCHAR(20) NOT NULL UNIQUE,
    Estado BOOLEAN DEFAULT TRUE,
    FechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Rol_Id) REFERENCES Rol(Id_Rol)
);

-- Tabla de productos
CREATE TABLE Producto (
    Id_Producto INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion TEXT NOT NULL,
    Precio DECIMAL(10,2) NOT NULL CHECK (Precio > 0),
    Stock INT NOT NULL CHECK (Stock > 0),
    Categoria VARCHAR(50) NOT NULL
);

-- Tabla de carritos
CREATE TABLE Carrito (
    Id_Carrito INT AUTO_INCREMENT PRIMARY KEY,
    Id_Usuario INT NOT NULL UNIQUE,
    FOREIGN KEY (Id_Usuario) REFERENCES Usuario(Id_Usuario) ON DELETE CASCADE
);

-- Detalle del carrito
CREATE TABLE Detalle_Carrito (
    Id_Carrito INT NOT NULL,
    Id_Producto INT NOT NULL,
    Cantidad INT NOT NULL CHECK (Cantidad > 0),
    Precio_Unitario DECIMAL(10,2) NOT NULL CHECK (Precio_Unitario > 0),
    Subtotal DECIMAL(10,2) GENERATED ALWAYS AS (Cantidad * Precio_Unitario) STORED,
    PRIMARY KEY (Id_Carrito, Id_Producto),
    FOREIGN KEY (Id_Carrito) REFERENCES Carrito(Id_Carrito) ON DELETE CASCADE,
    FOREIGN KEY (Id_Producto) REFERENCES Producto(Id_Producto)
);

-- Tabla de pedidos
CREATE TABLE Pedido (
    Id_Pedido INT AUTO_INCREMENT PRIMARY KEY,
    Id_Usuario INT NOT NULL,
    Fecha DATE NOT NULL,
    Estado VARCHAR(50) NOT NULL,
    Total DECIMAL(10,2) NOT NULL CHECK (Total > 0),
    FOREIGN KEY (Id_Usuario) REFERENCES Usuario(Id_Usuario) ON DELETE CASCADE
);

-- Detalle del pedido
CREATE TABLE Detalle_Pedido (
    Id_Pedido INT NOT NULL,
    Id_Producto INT NOT NULL,
    Cantidad INT NOT NULL CHECK (Cantidad > 0),
    Precio_Unitario DECIMAL(10,2) NOT NULL CHECK (Precio_Unitario > 0),
    Subtotal DECIMAL(10,2) GENERATED ALWAYS AS (Cantidad * Precio_Unitario) STORED,
    PRIMARY KEY (Id_Pedido, Id_Producto),
    FOREIGN KEY (Id_Pedido) REFERENCES Pedido(Id_Pedido) ON DELETE CASCADE,
    FOREIGN KEY (Id_Producto) REFERENCES Producto(Id_Producto)
);


