CREATE DATABASE Tienda_Virtual;
USE Tienda_Virtual;

CREATE TABLE Rol (
    Id_Rol INT PRIMARY KEY AUTO_INCREMENT,
    Descripcion VARCHAR(50),
    FechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Usuario (
    Id_Usuario INT AUTO_INCREMENT PRIMARY KEY,
    Rol_Id INT,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Email VARCHAR(50) UNIQUE,
    Contrasena VARCHAR(50), 
    DNI VARCHAR(50),
    Estado BIT,
    FechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Rol_Id) REFERENCES Rol(Id_Rol)
);


