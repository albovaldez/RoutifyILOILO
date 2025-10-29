-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: routify_iloilo_db
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `jeepny`
--

DROP TABLE IF EXISTS `jeepny`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jeepny` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jeepney_name` varchar(100) NOT NULL,
  `route` varchar(255) NOT NULL,
  `stops` text,
  `fare` decimal(6,2) NOT NULL,
  `distance_km` decimal(6,2) DEFAULT '0.00',
  `lat` decimal(9,6) NOT NULL,
  `lng` decimal(9,6) NOT NULL,
  `start_lat` decimal(9,6) DEFAULT NULL,
  `start_lng` decimal(9,6) DEFAULT NULL,
  `end_lat` decimal(9,6) DEFAULT NULL,
  `end_lng` decimal(9,6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jeepny`
--

LOCK TABLES `jeepny` WRITE;
/*!40000 ALTER TABLE `jeepny` DISABLE KEYS */;
INSERT INTO `jeepny` VALUES (1,'SM City Loop','SM City – Jaro Plaza – La Paz','SM City, Jaro Plaza, La Paz',15.00,0.00,10.720200,122.562100,10.701000,122.545000,10.716000,122.580000),(2,'Mandurriao Loop','Mandurriao – Molo – City Proper','Mandurriao, Molo, City Proper',14.00,0.00,10.708900,122.545500,10.708900,122.545500,10.692500,122.573000),(3,'La Paz Loop','La Paz – City Proper – Molo','La Paz, City Proper, Molo',13.00,0.00,10.713700,122.574500,10.716000,122.580000,10.693000,122.528000),(4,'Jaro CPU Route','CPU – Jaro Plaza – Iloilo City Proper','CPU, Jaro Plaza, Iloilo City Proper',12.00,0.00,10.723300,122.566100,10.723300,122.566100,10.692500,122.573000),(5,'Molo Arevalo Route','Molo – Arevalo – SM City','Molo, Arevalo, SM City',15.00,0.00,10.693100,122.512300,10.693100,122.528000,10.677200,122.505500);
/*!40000 ALTER TABLE `jeepny` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_account`
--

DROP TABLE IF EXISTS `user_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_account` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(300) NOT NULL,
  `email` varchar(300) NOT NULL,
  `password` varchar(300) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_account`
--

LOCK TABLES `user_account` WRITE;
/*!40000 ALTER TABLE `user_account` DISABLE KEYS */;
INSERT INTO `user_account` VALUES (1,'aliza','aliza.gmail.com','123'),(2,'alizah','alizah@gmail.com','scrypt:32768:8:1$Wtuta487KMBSU6Si$e0b46c2bff523882fd4bcc845a4d0ef1f7e83c6b88e413a732d35dc53c8422d274e7412ab7af0b5f75f6fa6a1e81d1f4c4fc27bd18af411337e5ee027ffd1260'),(3,'lily','lily@gmail.com','scrypt:32768:8:1$1EQt7zwodC0TSuxb$ebe4322e177fd626672e390fcb87231b480edf0be7cd37af26ad47aed08ddf282c21dad0969f1062a2299d8697b409d34bb31f7210e9a43f81400b7a8ae1a951'),(5,'mimi','mimi@gmail.com','scrypt:32768:8:1$SbUekXgGXIXRhYmG$4d52be15d8a65622dae0a73dd91c37572aaae5709b262e750bf03bc5e7f8cf599e2870022f88d8914ad13de998c323ace98aff39a372da20868934a0ffef6984'),(6,'maverick','maverick@gmail.com','scrypt:32768:8:1$ppn5WCMrn3vBqulQ$275c61f4ba5d231e4544624e93018aa7d3cf5a00c16d636ab5cb9fd2f39cbeb9b98f6058ca89c93a349acbc74948b46b28b385c15b14fa04d5bef55af5016674'),(7,'leza','leza@gmail.com','scrypt:32768:8:1$CzQAihJZdmpmtDce$da7274ac1783af2c21431480903bc545bac5d8a31a31140661fb32fb3ba96a88f2a54a1b54b7e5268777c399c4a88f4b5c917d687a0bd514b1381c3c61cb2fa5'),(8,'Angel','Angel@gmail.com','scrypt:32768:8:1$71qbzNS2yTrVySHu$012a2647a978ae4f998688ba3eff52265f884f68bb7c32de5c73a1d1465f814dbb1878543243fb7294d12680056728e00621c9c2e7200dc27deff41c828d4d2d'),(9,'Hanna','hanna@gmail.com','scrypt:32768:8:1$0m4pepmNZjUg7GO7$8170a737f363b18d7cf2b3f532c75b7f163869f7c9325e05855e3bc02be156f9d3119f0b515b4037ef35440c0144a81fa8920fd14d7f4e3117969bba514ebe7c'),(10,'MAMA','mama@gmail.com','scrypt:32768:8:1$s9uJVQHcy9LzcJbx$e339ac4966ad4d5696b8f61357c70fe3365170b392357d48a80d512c2057c46cb65a87998c8e22d9102708fe7e49dc8c11767dd8a183e298151430191b58001b'),(11,'haha','haha@gmail.com','scrypt:32768:8:1$SzhDzYfIPF0kB4uJ$a3cd4e62395ea4888f77957c15bec6bf7d99eaefabe1d1f0378ab1bd7b8af272832eeb7e4d602b0cc44d6a4aafa31e4d37cfc39f48d466ad651cc09ea088c616'),(12,'john','john@gmail.com','scrypt:32768:8:1$QeOJ6BgOkFZ71Jpk$a3be43f7c3c1da991cd12c237f65725d281aa2111cebe6d718082de368f408d45a83f2d67c75be7aa6256098be7dd348ba20ac4bfb5c9c0228be4bf2c573eb09'),(13,'cris','cris@gmail.com','scrypt:32768:8:1$vQpq7QaDsT8GUlul$3b03503b1625c05f52521de8b159f653bae1ea87d75969922796fd84a1c4e89a7ddd99cea44d53a1d57463f0e187304e923a919faee038560b1992b2d3b3a584');
/*!40000 ALTER TABLE `user_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_profile`
--

DROP TABLE IF EXISTS `user_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_profile` (
  `id_profile` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) NOT NULL,
  `country` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `province` varchar(200) NOT NULL,
  `profile_pic` varchar(200) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id_profile`),
  CONSTRAINT `fk_user_profile` FOREIGN KEY (`id_profile`) REFERENCES `user_account` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_profile`
--

LOCK TABLES `user_profile` WRITE;
/*!40000 ALTER TABLE `user_profile` DISABLE KEYS */;
INSERT INTO `user_profile` VALUES (1,'alizah','valdez','philippines','iloilo','oton ','uploads/profile.jpg',NULL);
/*!40000 ALTER TABLE `user_profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-28 22:34:41
