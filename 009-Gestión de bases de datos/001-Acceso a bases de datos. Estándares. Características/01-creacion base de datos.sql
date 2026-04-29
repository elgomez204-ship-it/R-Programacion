sudo mysql -u root -p

CREATE DATABASE corporacion2026;
USE corporacion2026;

CREATE TABLE usuarios(
	nombre VARCHAR(255),
  apellidos VARCHAR(255),
  email VARCHAR(255)
);

INSERT INTO usuarios VALUES(
	"Juan",
  "Patino",
  "juan@empresa.com"
);

SELECT * FROM usuarios;