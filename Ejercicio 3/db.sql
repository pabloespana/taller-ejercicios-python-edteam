create table movimiento(
	id integer auto_increment primary key,
    tipo text not null,
    cantidad float(6,2) not null,
    fecha date not null
)