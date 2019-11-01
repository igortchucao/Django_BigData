-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema enade
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema enade
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `enade` DEFAULT CHARACTER SET utf8 ;
USE `enade` ;

-- -----------------------------------------------------
-- Table `enade`.`area`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`area` (
  `areaNome` VARCHAR(45) NOT NULL,
  `numQuestoes` INT NULL,
  `login` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`areaNome`),
  INDEX `fk_area_usuario1_idx` (`login` ASC),
  CONSTRAINT `fk_area_usuario1`
    FOREIGN KEY (`login`)
    REFERENCES `enade`.`usuario` (`login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `enade`.`questao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`questao` (
  `idQuestao` INT NOT NULL,
  `texto` BLOB NULL,
  `ano` VARCHAR(4) NOT NULL,
  `resposta` VARCHAR(1) NOT NULL,
  `diretorioImagem` VARCHAR(45) NOT NULL,
  `altA` BLOB NULL,
  `altB` BLOB NULL,
  `altC` BLOB NULL,
  `altD` BLOB NULL,
  `altE` BLOB NULL,
  `areaNome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idQuestao`),
  INDEX `fk_questao_area1_idx` (`areaNome` ASC) ,
  CONSTRAINT `fk_questao_area1`
    FOREIGN KEY (`areaNome`)
    REFERENCES `enade`.`area` (`areaNome`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `enade`.`cadastra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`cadastra` (
  `loginProfessor` VARCHAR(45) NOT NULL,
  `idQuestao` INT NOT NULL,
  `data` DATE NOT NULL,
  PRIMARY KEY (`idQuestao`),
  INDEX `fk_professor_has_questao_questao1_idx` (`idQuestao` ASC),
  INDEX `fk_professor_has_questao_professor1_idx` (`loginProfessor` ASC),
  CONSTRAINT `fk_professor_has_questao_professor1`
    FOREIGN KEY (`loginProfessor`)
    REFERENCES `enade`.`professor` (`loginProfessor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_professor_has_questao_questao1`
    FOREIGN KEY (`idQuestao`)
    REFERENCES `enade`.`questao` (`idQuestao`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `enade`.`proReitor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`proReitor` (
  `loginReitor` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NULL,
  `cpf` VARCHAR(11) NOT NULL,
  PRIMARY KEY (`loginReitor`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `enade`.`Aluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`Aluno` (
  `login` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NULL,
  `cpf` VARCHAR(11) NOT NULL,
  PRIMARY KEY (`login`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `enade`.`professor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`professor` (
  `loginProfessor` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `especialidade` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`loginProfessor`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `enade`.`Administrador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`Administrador` (
  `login` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `areaNome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`login`),
  INDEX `fk_administrador_area1_idx` (`areaNome` ASC),
  CONSTRAINT `fk_administrador_area1`
    FOREIGN KEY (`areaNome`)
    REFERENCES `enade`.`area` (`areaNome`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `enade`.`avalia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`avalia` (
  `loginReitor` VARCHAR(45) NOT NULL,
  `loginProfessor` VARCHAR(45) NOT NULL,
  `nota` DECIMAL(10,2) NOT NULL,
  `data` DATE NOT NULL,
  `comentario` VARCHAR(45) NULL,
  PRIMARY KEY (`loginReitor`, `loginProfessor`),
  INDEX `fk_proReitor_has_professor_professor1_idx` (`loginProfessor` ASC),
  INDEX `fk_proReitor_has_professor_proReitor1_idx` (`loginReitor` ASC),
  CONSTRAINT `fk_proReitor_has_professor_proReitor1`
    FOREIGN KEY (`loginReitor`)
    REFERENCES `enade`.`proReitor` (`loginReitor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_proReitor_has_professor_professor1`
    FOREIGN KEY (`loginProfessor`)
    REFERENCES `enade`.`professor` (`loginProfessor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `enade`.`cadastra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`cadastra` (
  `loginProfessor` VARCHAR(45) NOT NULL,
  `idQuestao` INT NOT NULL,
  `data` DATE NOT NULL,
  PRIMARY KEY (`idQuestao`),
  INDEX `fk_professor_has_questao_questao1_idx` (`idQuestao` ASC),
  INDEX `fk_professor_has_questao_professor1_idx` (`loginProfessor` ASC),
  CONSTRAINT `fk_professor_has_questao_professor1`
    FOREIGN KEY (`loginProfessor`)
    REFERENCES `enade`.`professor` (`loginProfessor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_professor_has_questao_questao1`
    FOREIGN KEY (`idQuestao`)
    REFERENCES `enade`.`questao` (`idQuestao`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
