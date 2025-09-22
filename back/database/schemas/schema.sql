DROP TABLE IF EXISTS Usuario;
create table Usuario(
id_usuario INTEGER primary key AUTOINCREMENT,
nombre text not null,
apellido text not null,
mail text not null unique,
contraseña text not null,
rol text not null,
dni text not null unique
);

create table Producto(
id_producto INTEGER primary key AUTOINCREMENT,
nombre text not null,
descripcion text not null,
precio real not null check (precio>0),
stock integer not null check (stock >0),
categoria text not null
);

create table Carrito(
id_carrito integer primary key AUTOINCREMENT,
id_usuario integer not null unique,
foreign key (id_usuario) references Usuario(id_usuario)
        on delete cascade 
);

create table Detalle_carrito(
id_carrito integer not null,
id_producto integer not null,
cantidad integer not null check (cantidad > 0),
precio_unitario real not null check (precio_unitario > 0),
subtotal real generated always as (precio_unitario * cantidad) stored,
primary key (id_carrito, id_producto),
foreign key (id_carrito) references Carrito(id_carrito) on delete cascade,
foreign key (id_producto) references Producto(id_producto)
);

create table Pedido(
id_pedido integer primary key AUTOINCREMENT,
id_usuario integer not null,
fecha date not null,
estado text not null,
total real not null check (total>0),
foreign key (id_usuario) references Usuario(id_usuario) on delete cascade 

);

create table Detalle_pedido(
id_pedido integer not null,
id_producto integer not null,
cantidad integer not null check (cantidad >0),
precio_unitario real not null check (precio_unitario>0),
subtotal real generated always as (precio_unitario* cantidad) stored,
primary key (id_pedido, id_producto),
foreign key (id_pedido) references Pedido(id_pedido) on delete cascade,
foreign key (id_producto) references Producto(id_producto)

);