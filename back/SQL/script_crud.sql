-- CONSULTAS SQL

--CREAR LA TABLA USUARIOS

DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS rol;

CREATE TABLE usuarios (
    Id_Usuario INT PRIMARY KEY AUTO_INCREMENT,
    Rol_Id INT NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Email VARCHAR(50) UNIQUE NOT NULL,
    Contraseña VARCHAR(50) NOT NULL,
    DNI VARCHAR(50),
    Estado BIT DEFAULT 1,
    FechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Rol_Id) REFERENCES rol(Id_Rol)
);

--CREAR LA TABLA ROLES

CREATE TABLE rol (
    Id_Rol INT PRIMARY KEY,
    Descripcion VARCHAR(50) NOT NULL,
    FechaRegistro DATETIME DEFAULT CURRENT_TIMESTAMP
);

--INSERTAR ROLES

INSERT INTO rol (Id_Rol, Descripcion) VALUES (1, 'admin'); --Primero poner cero y 1 para que coincida con el id
INSERT INTO rol (Id_Rol, Descripcion) VALUES (2, 'usuario'); --Segundo el cero = estandar y el 1 = admin

--REGISTRAR USUARIOS

INSERT INTO usuarios (Rol_id, Nombre, Apellido, Email, Contraseña, DNI)
VALUES (1, 'Pedro', 'González', 'pedro@gmail.com', 'pass1234', '12345678');

--BUSCAR USUARIOS

--Listar todos los usuarios

SELECT * FROM usuarios;

--Por id

SELECT * FROM usuarios WHERE id = 1;

--Validar login

SELECT * FROM usuarios WHERE email = 'pedro@gmail.com' AND contraseña = 'pass1234';


--MODIFICAR USUARIOS

--Modificar datos

UPDATE usuarios
SET nombre = 'Pedro actualizado', apellido = 'González actualizado'
WHERE id = 1;

--Modificar rol

UPDATE usuarios
SET Rol_id = 2
WHERE id_usuario = 1;

--ELIMINAR USUARIO

DELETE FROM usuarios
WHERE id = 1;







