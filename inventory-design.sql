-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema inventory
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `inventory` ;

-- -----------------------------------------------------
-- Schema inventory
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `inventory` DEFAULT CHARACTER SET utf8 ;
USE `inventory` ;

-- -----------------------------------------------------
-- Table `inventory`.`Container`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `inventory`.`Container` ;

CREATE TABLE IF NOT EXISTS `inventory`.`Container` (
  `Container_id` INT NOT NULL,
  `color` VARCHAR(30) NULL,
  `Container_col` VARCHAR(30) NULL,
  PRIMARY KEY (`Container_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `inventory`.`type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `inventory`.`type` ;

CREATE TABLE IF NOT EXISTS `inventory`.`type` (
  `type_id` INT NOT NULL,
  `type` VARCHAR(30) NULL,
  PRIMARY KEY (`type_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `inventory`.`item`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `inventory`.`item` ;

CREATE TABLE IF NOT EXISTS `inventory`.`item` (
  `item_id` INT NOT NULL,
  `item_name` VARCHAR(50) NOT NULL,
  `quantity` INT NOT NULL DEFAULT 1,
  `Container_id` INT NOT NULL,
  `type_id` INT NOT NULL,
  PRIMARY KEY (`item_id`),
  INDEX `fk_item_Container_idx` (`Container_id` ASC) VISIBLE,
  INDEX `fk_item_type1_idx` (`type_id` ASC) VISIBLE,
  CONSTRAINT `fk_item_Container`
    FOREIGN KEY (`Container_id`)
    REFERENCES `inventory`.`Container` (`Container_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_item_type1`
    FOREIGN KEY (`type_id`)
    REFERENCES `inventory`.`type` (`type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- INVENTORY TESTING SCRIPTS