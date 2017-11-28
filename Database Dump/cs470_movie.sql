-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: cs470
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movie` (
  `MID` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `theater_ID` int(11) DEFAULT NULL,
  `rating` varchar(5) DEFAULT NULL,
  `price_per_ticket` decimal(5,2) DEFAULT NULL,
  `poster_title` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`MID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (1,'A Bad Moms Christmas',1,'R',7.50,NULL),(2,'Blade Runner 2049',1,'R',7.50,NULL),(3,'Casablanca 75th Anniversary',4,'NR',5.25,NULL),(4,'Daddys Home 2',3,'PG13',7.25,NULL),(5,'The Foreigner',2,'R',6.50,NULL),(6,'Genesis: Paradise Lost',3,'NR',6.50,NULL),(7,'Geostorm',2,'PG13',7.50,NULL),(8,'Happy Death Day',4,'PG13',6.75,NULL),(9,'IT',3,'R',7.25,NULL),(10,'Jigsaw',2,'R',5.75,NULL),(11,'Justice League',3,'PG13',7.25,NULL),(12,'LBJ',1,'R',6.50,NULL),(13,'The Lego Ninjago Movie',4,'PG',7.50,NULL),(14,'Let There Be Light',3,'PG13',7.50,NULL),(15,'Marshall',2,'PG13',6.25,NULL),(16,'Murder on the Orient Express',1,'PG13',6.50,NULL),(17,'My Little Pony: The Movie',4,'PG',5.25,NULL),(18,'Only The Brave',1,'PG13',6.25,NULL),(20,'Pottersville',2,'PG13',7.25,NULL),(21,'The Star',1,'PG',5.25,NULL),(22,'Thank You For Your Service',2,'R',6.25,NULL),(23,'Thor: Ragnarok',3,'PG13',7.50,NULL),(25,'Wonder',3,'PG',7.25,NULL),(26,'Tyler Perrys Boo 2!',4,'PG13',7.50,NULL);
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-27 22:16:10
