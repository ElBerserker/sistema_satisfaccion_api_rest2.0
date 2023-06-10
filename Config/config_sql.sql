/* Nombre:  Raul Hernandez Lopez @Neo 
   Email:    freeenergy1975@gmail.com 
   fecha: sabado 10 de junio del 2023 */

-- Creacion de la base de datos.
CREATE DATABASE sistema_satisfaccion;
-- Crecion de usuario.
CREATE USER 'Berserker_db'@'%' IDENTIFIED BY 'db_maria1.1';
-- Asignacion de permisos a la base de datos.
GRANT ALL PRIVILEGES ON sistema_satisfaccion.*TO'Berserker_db'@'%'
FLUSH PRIVILEGES;

