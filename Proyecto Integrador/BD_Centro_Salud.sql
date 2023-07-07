CREATE DATABASE IF NOT EXISTS centro_salud;

USE centro_salud;

CREATE TABLE IF NOT EXISTS individuos (
  idIndividuo int,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  contraseña VARCHAR(10) NOT NULL,
  email VARCHAR(100),
  PRIMARY KEY (idIndividuo)
);
SELECT * FROM individuos;
