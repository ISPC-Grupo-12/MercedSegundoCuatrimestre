create database Merced;
use merced; 


create table Usuario(
id_usuario INT primary key auto_increment,
nombre varchar(100) not null,
apellido varchar(100) not null,
mail varchar(150) not null unique,
contrasena varchar(255) not null,
rol varchar(50) not null,
dni varchar(50) not null unique
);

create table Producto(
id_producto INT primary key auto_increment,
nombre varchar(200) not null,
descripcion varchar(1500) not null,
precio decimal(12,2) not null check (precio>0),
stock int not null check (stock >0),
categoria varchar(80) not null
);

create table Carrito(
id_carrito int primary key auto_increment,
id_usuario int not null unique,
foreign key (id_usuario) references Usuario(id_usuario)
        on delete cascade 
);

create table Detalle_carrito(
id_carrito int not null,
id_producto int not null,
cantidad int not null check (cantidad > 0),
precio_unitario decimal(12,2) not null check (precio_unitario > 0),
subtotal decimal(12,2) generated always as (precio_unitario * cantidad) stored,
primary key (id_carrito, id_producto),
foreign key (id_carrito) references Carrito(id_carrito) on delete cascade,
foreign key (id_producto) references Producto(id_producto)
);

create table Pedido(
id_pedido int primary key auto_increment,
id_usuario int not null,
fecha date not null,
estado varchar(150) not null,
total decimal(12,2) not null check (total>0),
foreign key (id_usuario) references Usuario(id_usuario) on delete cascade 

);

create table Detalle_pedido(
id_pedido int not null,
id_producto int not null,
cantidad int not null check (cantidad >0),
precio_unitario decimal(12,2) not null check (precio_unitario>0),
subtotal decimal(12,2) generated always as (precio_unitario* cantidad) stored,
primary key (id_pedido, id_producto),
foreign key (id_pedido) references Pedido(id_pedido) on delete cascade,
foreign key (id_producto) references Producto(id_producto)

);