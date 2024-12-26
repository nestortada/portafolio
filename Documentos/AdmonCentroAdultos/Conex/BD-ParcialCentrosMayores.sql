-- Reiniciar configuraciones
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION';

-- Crear esquema con configuración consistente
DROP SCHEMA IF EXISTS `sql10753480`;
CREATE SCHEMA IF NOT EXISTS `sql10753480` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `sql10753480`;

-- Crear tabla Centros
DROP TABLE IF EXISTS `Centros`;
CREATE TABLE `Centros` (
  `Nombre` VARCHAR(30) NOT NULL,
  `Direccion` VARCHAR(45) NOT NULL,
  `Telefono` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`Nombre`),
  UNIQUE INDEX `Direccion_UNIQUE` (`Direccion`),
  UNIQUE INDEX `Telefono_UNIQUE` (`Telefono`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Crear tabla Adultos
DROP TABLE IF EXISTS `Adultos`;
CREATE TABLE `Adultos` (
  `idAdulto` INT NOT NULL,
  `Nombre` VARCHAR(30) NOT NULL,
  `Apellido` VARCHAR(30) NOT NULL,
  `Nacimiento` DATE NOT NULL,
  `Peso` INT NOT NULL,
  `Altura` INT NOT NULL,
  `Contacto` VARCHAR(15) NOT NULL,
  `Centro` VARCHAR(30) NULL,
  PRIMARY KEY (`idAdulto`),
  CONSTRAINT `FK_CentrosAdultos_Centro`
    FOREIGN KEY (`Centro`)
    REFERENCES `Centros` (`Nombre`)
    ON DELETE SET NULL
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Crear tabla Categorias
DROP TABLE IF EXISTS `Categorias`;
CREATE TABLE `Categorias` (
  `idCategoria` INT NOT NULL,
  `Nombre` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`idCategoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Crear tabla Actividades
DROP TABLE IF EXISTS `Actividades`;
CREATE TABLE `Actividades` (
  `idActividad` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Descripcion` VARCHAR(100) NOT NULL,
  `Fecha` DATE NULL,
  `idCategoria` INT NULL,
  `Centro` VARCHAR(30) NULL,
  PRIMARY KEY (`idActividad`),
  INDEX `FK_CategoriasActividades_Categoria_idx` (`idCategoria`),
  INDEX `FK_Centros_Actividades_Centro_idx` (`Centro`),
  CONSTRAINT `FK_CategoriasActividades_Categoria`
    FOREIGN KEY (`idCategoria`)
    REFERENCES `Categorias` (`idCategoria`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `FK_Centros_Actividades_Centro`
    FOREIGN KEY (`Centro`)
    REFERENCES `Centros` (`Nombre`)
    ON DELETE SET NULL
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Crear tabla Inscripcion
DROP TABLE IF EXISTS `Inscripcion`;
CREATE TABLE `Inscripcion` (
  `IdAdulto` INT NOT NULL,
  `IdActividad` INT NOT NULL,
  `Calificacion` INT NULL,
  PRIMARY KEY (`IdAdulto`, `IdActividad`),
  INDEX `FK_ActividadesInscripcion_IdActividad_idx` (`IdActividad`),
  CONSTRAINT `FK_AdultosInscripcion_IdAdulto`
    FOREIGN KEY (`IdAdulto`)
    REFERENCES `Adultos` (`idAdulto`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `FK_ActividadesInscripcion_IdActividad`
    FOREIGN KEY (`IdActividad`)
    REFERENCES `Actividades` (`idActividad`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Insertar datos iniciales
INSERT INTO `Centros` VALUES
('Colina', 'Calle 134 # 7-16', '3202441778'),
('Usaquen', 'Calle 93#7-18', '3142543825'),
('Centro', 'Calle 72 #7-15', '3007143354');

INSERT INTO `Adultos` VALUES
(1111, 'Camila', 'Botero', '2001-09-11', 45, 150, '3003674499', 'Colina'),
(2222, 'Valeria', 'Diaz', '2001-10-22', 60, 168, '3212441778', 'Centro'),
(3333, 'Jean Carlo', 'Ruiz', '1999-06-23', 60, 170, '3238683038', 'Usaquen'),
(4444, 'Cristian', 'Ortiz', '2001-07-16', 70, 175, '3015657725', 'Centro');

INSERT INTO `Categorias` VALUES
(1, 'Salidas culturales'),
(2, 'Gimnasia'),
(3, 'Manualidades'),
(10, 'Paseos');

INSERT INTO `Actividades` VALUES
(1, 'Yoga para el alma', 'Realiza diferentes ejercicios para relajar tus músculos y aumentar tu flexibilidad', '2023-03-03', 2, 'Colina'),
(2, 'Conoce La Candelaria', 'Ven a nuestro tour por La Candelaria, donde conocerás la historia de este hermoso lugar', '2023-04-01', 1, 'Usaquen'),
(3, 'Termales imperdibles', 'Salida a las termales de Tabio para relajarte y disfrutar la hermosa vista de los bosques', '2023-04-12', 4, 'Centro'),
(4, 'Crochet: Teje tus prendas', 'Aprende a tejer desde cero tu propia bufanda', '2023-04-18', 3, 'Usaquen');

INSERT INTO `Inscripcion` VALUES
(1111, 1, 9),
(2222, 1, 8),
(4444, 1, 10),
(1111, 2, 9),
(2222, 2, 4),
(4444, 2, 10),
(3333, 3, 7),
(1111, 3, 9),
(2222, 3, 4),
(4444, 3, 10),
(1111, 4, 2),
(2222, 4, 3),
(4444, 4, 4);


DELIMITER //
CREATE PROCEDURE allCentros()
BEGIN
    SELECT Nombre, Direccion, Telefono FROM Centros;
END //
DELIMITER ;

DELIMITER //

CREATE PROCEDURE getCentro(IN nombreCentro VARCHAR(30))
BEGIN
    SELECT Nombre, Direccion, Telefono 
    FROM Centros 
    WHERE Nombre = nombreCentro;
END //
DELIMITER ;


DELIMITER //

CREATE PROCEDURE delCentro(IN nombreCentro VARCHAR(30))
BEGIN
    DELETE FROM Centros WHERE Nombre = nombreCentro;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE newCentro(IN nombreCentro VARCHAR(30), IN direccionCentro VARCHAR(45), IN telefonoCentro VARCHAR(15))
BEGIN
    INSERT INTO Centros (Nombre, Direccion, Telefono) VALUES (nombreCentro, direccionCentro, telefonoCentro);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE modCentro(IN nombreNew VARCHAR(30), IN direccionNew VARCHAR(45), IN telefonoNew VARCHAR(15), IN nombreOld VARCHAR(30))
BEGIN
    UPDATE Centros
    SET Nombre = nombreNew, Direccion = direccionNew, Telefono = telefonoNew
    WHERE Nombre = nombreOld;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE allActividades()
BEGIN
    SELECT * FROM Actividades;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE getActividad(IN id INT)
BEGIN
    SELECT * FROM Actividades WHERE idActividad = id;
END //

DELIMITER ;

DELIMITER //

DELIMITER //

DELIMITER //

CREATE PROCEDURE delActividad(IN idActividad INT)
BEGIN
    IF EXISTS (SELECT 1 FROM Inscripcion WHERE IdActividad = idActividad) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Hay inscripciones relacionadas con esta actividad. Elimine primero las inscripciones asociadas.';
    ELSE
        DELETE FROM Actividades WHERE idActividad = idActividad;
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE newActividad(
    IN idActividad INT,
    IN nombreActividad VARCHAR(45),
    IN descripcionActividad VARCHAR(100),
    IN fechaActividad DATE,
    IN idCategoria INT,
    IN nombreCentro VARCHAR(30)
)
BEGIN
    INSERT INTO Actividades (idActividad, Nombre, Descripcion, Fecha, idCategoria, Centro) 
    VALUES (idActividad, nombreActividad, descripcionActividad, fechaActividad, idCategoria, nombreCentro);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE allCategorias()
BEGIN
    SELECT * FROM Categorias;
END //

DELIMITER ;



DROP PROCEDURE IF EXISTS getCategoria;

DELIMITER //

CREATE PROCEDURE getCategoria(IN idCat INT)
BEGIN
    SELECT idCategoria, Nombre
    FROM Categorias
    WHERE idCategoria = idCat;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE delCategoria(IN idCat INT)
BEGIN
    DELETE FROM Categorias WHERE idCategoria = idCat;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE newCategoria(
    IN idCategoria INT,
    IN nombreCategoria VARCHAR(100)
)
BEGIN
    INSERT INTO Categorias (idCategoria, Nombre) 
    VALUES (idCategoria, nombreCategoria);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE modCategoria(
    IN idCategoriaNew INT,
    IN nombreNew VARCHAR(100),
    IN idCategoriaOld INT
)
BEGIN
    UPDATE Categorias 
    SET idCategoria = idCategoriaNew, Nombre = nombreNew
    WHERE idCategoria = idCategoriaOld;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE allAdultos()
BEGIN
    SELECT idAdulto, Nombre, Apellido, Nacimiento, Peso, Altura, Contacto, Centro FROM Adultos;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE getAdulto(IN idAdul INT)
BEGIN
    SELECT idAdulto, Nombre, Apellido, Nacimiento, Peso, Altura, Contacto, Centro
    FROM Adultos
    WHERE idAdulto = idAdul;
END //

DELIMITER ;



DELIMITER //

CREATE PROCEDURE delAdulto(IN idAdul INT)
BEGIN
    DELETE FROM Adultos WHERE idAdulto = idAdul;
END //

DELIMITER ;






DELIMITER //

CREATE PROCEDURE newAdulto(
    IN idAdulto INT,
    IN nombre VARCHAR(255),
    IN apellido VARCHAR(255),
    IN nacimiento DATE,
    IN peso FLOAT,
    IN altura FLOAT,
    IN contacto VARCHAR(255),
    IN centro VARCHAR(255)
)
BEGIN
    INSERT INTO Adultos (idAdulto, Nombre, Apellido, Nacimiento, Peso, Altura, Contacto, Centro)
    VALUES (idAdulto, nombre, apellido, nacimiento, peso, altura, contacto, centro);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE modAdulto(
    IN idAdultoNew INT,
    IN nombreNew VARCHAR(255),
    IN apellidoNew VARCHAR(255),
    IN nacimientoNew DATE,
    IN pesoNew FLOAT,
    IN alturaNew FLOAT,
    IN contactoNew VARCHAR(255),
    IN centroNew VARCHAR(255),
    IN idAdultoViejo INT
)
BEGIN
    UPDATE Adultos
    SET idAdulto = idAdultoNew,
        Nombre = nombreNew,
        Apellido = apellidoNew,
        Nacimiento = nacimientoNew,
        Peso = pesoNew,
        Altura = alturaNew,
        Contacto = contactoNew,
        Centro = centroNew
    WHERE idAdulto = idAdultoViejo;
END //

DELIMITER ;













-- Restablecer configuraciones originales
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
