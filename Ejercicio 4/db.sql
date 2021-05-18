create table producto(
	id serial primary key,
	nombre varchar(50) not null,
	descripcion varchar(50) not null,
	precio decimal(6, 2) not null
)