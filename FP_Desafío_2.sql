-- Creación de base de datos y tablas, ingesta de .csv fue manual.

CREATE DATABASE spotify_2018
;

CREATE TABLE artista(
	nombre_artista_pk VARCHAR(30) NOT NULL,
	fecha_de_nacimiento DATE,
	nacionalidad VARCHAR(20),
	PRIMARY KEY (nombre_artista_pk)
);

CREATE TABLE cancion(
	titulo_cancion_pk VARCHAR(40),
	artista VARCHAR(30) NOT NULL,
	album VARCHAR (40),
	numero_del_track INT,
	PRIMARY KEY (titulo_cancion_pk),
	FOREIGN KEY (artista) REFERENCES artista(nombre_artista_pk)
);

CREATE TABLE album(
	titulo_album_pk VARCHAR(40),
	artista VARCHAR(30),
	year_ INT,
	PRIMARY KEY (titulo_album_pk),
	FOREIGN KEY (artista) REFERENCES artista(nombre_artista_pk)
);

/*
Comentario extra: se corrige archivo de cancion.CSV por problema
con una fila que contenía " 12" en vez de "12"
*/

-- 1., 2. Canciones del año 2018, artista y álbum
SELECT cancion.titulo_cancion_pk,
	   cancion.artista,
	   cancion.album
FROM cancion
INNER JOIN album
	ON album.titulo_album_pk = cancion.album 
	AND album.year_ = '2018'
;

/* 3. Número de track, canción, álbum, año de lanzamiento y artista
ordenado según año de lanzamiento, álbum y artista
 */
SELECT cancion.numero_del_track,
	   cancion.titulo_cancion_pk,
	   cancion.album,
	   album.year_,
	   album.artista
FROM cancion
INNER JOIN album
	   ON album.titulo_album_pk = cancion.album
	   AND album.year_ = '2018'
ORDER BY album.year_,
         album.titulo_album_pk,
         album.artista
;


