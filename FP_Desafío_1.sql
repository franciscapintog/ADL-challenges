-- Creación de base de datos
create database Biblioteca
;

-- Creación de tabla Libro_
create table Libro_(
id_libro_pk int,
nombre_libro varchar(50),
autor varchar(30),
genero varchar(30),
primary key (id_libro_pk)
);

-- Inserción de valores a tabla Libro_
INSERT INTO public.Libro_
(id_libro_pk,nombre_libro,autor,genero) values 
(001, 'Sapo y Sepo', 'Mi Perro', 'Filosofía'),
(002, 'La Metamorfosis', 'Franz Kafka', 'Ficción')
;

-- Crear tabla Préstamo
create table Prestamo(
id_prestamo_pk int,
id_libro int,
nombre_persona varchar(30),
fecha_inicio date,
fecha_termino date,
primary key (id_prestamo_pk),
foreign key (id_libro) references Libro_(id_libro_pk)
);

-- Agregar columna a Libro_
alter table libro_ 
add prestado boolean
;

-- Ingresar estado de préstamo de "Sapo y Sepo"
update public.Libro_
set prestado = true where nombre_libro = 'Sapo y Sepo'
;
update public.Libro_
set prestado = false where nombre_libro = 'La Metamorfosis'
;

-- Ingresar historial de préstamos de "Sapo y Sepo"
insert into public.prestamo
(id_prestamo_PK, id_libro, nombre_persona, fecha_inicio, fecha_termino) values
(0001, 001, 'Ruairí Zinaida', '2021-08-22', '2021-09-01'),
(0002, 001, 'Boris Klavdia', '2021-08-23', '2021-09-05'),
(0003, 001, 'Liboria Eun-Yeong', '2021-08-24', '2021-09-09'),
(0004, 001, 'Vlasiy Kuzma', '2021-08-24', '2021-08-30'),
(0005, 001, 'Granya Ira', '2021-09-02', null),
(0006, 002, 'Ottone Bearach', '2021-04-03', '2021-04-10'),
(0007, 002, 'Geremia Somerled', '2021-04-03', '2021-04-10'),
(0008, 002, 'Boris Klavdia', '2021-04-03', '2021-04-10'),
(0009, 002, 'Lilia Fedelma', '2021-04-03', '2021-04-10'),
(0010, 002, 'Catriona Adamo', '2021-04-03', '2021-04-10'),
(0011, 002, 'Aithne Eva', '2021-04-03', '2021-04-10')
;

-- Creación de nuevo Libro
INSERT INTO public.Libro_
(id_libro_pk,nombre_libro,autor,genero, prestado) values 
(003, '¿Por qué tenemos el cerebro en la cabeza?', 'Pedro Maldonado', 'Ciencia', True)
;

-- Creación de préstamos de nuevo libro
insert into public.prestamo 
(id_prestamo_pk, id_libro, nombre_persona, fecha_inicio, fecha_termino) values
(00012, 003, 'Sinéad Iomhar', '2021-06-22', '2021-07-01'),
(00013, 003, 'Boris Klavdia', '2021-08-14', '2021-09-02'),
(00014, 003, 'Fabio Leontina','2021-11-25',  null)
;

-- Seleccionar libros y personas que pidieron prestado el último libro ingresado
select nombre_persona from public.prestamo where fecha_termino is null
;
select nombre_libro from public.libro_ where prestado = true
;

-- Seleccionar columnas de prestamo de "Sapo y Sepo" ordenados por fecha_inicio
select * from public.prestamo where id_libro = 001 order by fecha_inicio
;