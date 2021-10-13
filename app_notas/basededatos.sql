CREATE DATABASE IF NOT EXISTS appnotas;
use appnotas;

"""Me crea la base de datos llamada appnotas si no existe y con use la usamenos"""


CREATE TABLE usuarios(
   
   id  int(25) auto_increment NOT NULL,
   nombre varchar(30) ,
   apellidos varchar(35),
   email varchar(35) not null ,
   pass  varchar(15) not null ,
   fecha_alta date not null,
   CONSTRAINT pk_usuarios PRIMARY KEY(id),
   CONSTRAINT uq_email UNIQUE(email)

)ENGINE=InnoDb;

CREATE TABLE notas(

   id int(25) auto_increment NOT NULL,
   usuario_id int(25) ,
   titulo varchar(30) not null ,
   descripcion MEDIUMTEXT,
   fecha date not null ,
   CONSTRAINT pk_notas PRIMARY KEY (id),
   CONSTRAINT fk_notas_user FOREIGN KEY (usuario_id) REFERENCES usuarios(id)

)ENGINE=InnoDb;

