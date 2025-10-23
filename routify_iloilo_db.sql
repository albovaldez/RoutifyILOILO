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
  `id` int NOT NULL,
  `jeep_name` varchar(200) NOT NULL,
  `stops` varchar(200) NOT NULL,
  `fare` int NOT NULL,
  `distance_km` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jeepny`
--

LOCK TABLES `jeepny` WRITE;
/*!40000 ALTER TABLE `jeepny` DISABLE KEYS */;
INSERT INTO `jeepny` VALUES (1,'jaro ','jaro-plaza',12,5.00),(2,'villa ','villa supermart',15,5.00),(3,'tagbak ','tagbak terminal ',25,10.00);
/*!40000 ALTER TABLE `jeepny` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jeepny_route`
--

DROP TABLE IF EXISTS `jeepny_route`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jeepny_route` (
  `route_id` int NOT NULL AUTO_INCREMENT,
  `route_name` varchar(200) NOT NULL,
  `route_code` varchar(200) NOT NULL,
  `start_lat` decimal(10,7) NOT NULL,
  `start_lng` decimal(10,7) NOT NULL,
  `end_lat` decimal(10,7) NOT NULL,
  `end_lng` decimal(10,7) NOT NULL,
  `distance_km` decimal(10,7) NOT NULL,
  `fare` int NOT NULL,
  PRIMARY KEY (`route_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jeepny_route`
--

LOCK TABLES `jeepny_route` WRITE;
/*!40000 ALTER TABLE `jeepny_route` DISABLE KEYS */;
INSERT INTO `jeepny_route` VALUES (1,'villa','villa bay-bay',10.6806170,122.4997190,10.6836420,122.5003090,2.0000000,10);
/*!40000 ALTER TABLE `jeepny_route` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_account`
--

LOCK TABLES `user_account` WRITE;
/*!40000 ALTER TABLE `user_account` DISABLE KEYS */;
INSERT INTO `user_account` VALUES (1,'aliza','aliza.gmail.com','123'),(2,'alizah','alizah@gmail.com','scrypt:32768:8:1$Wtuta487KMBSU6Si$e0b46c2bff523882fd4bcc845a4d0ef1f7e83c6b88e413a732d35dc53c8422d274e7412ab7af0b5f75f6fa6a1e81d1f4c4fc27bd18af411337e5ee027ffd1260'),(3,'lily','lily@gmail.com','scrypt:32768:8:1$1EQt7zwodC0TSuxb$ebe4322e177fd626672e390fcb87231b480edf0be7cd37af26ad47aed08ddf282c21dad0969f1062a2299d8697b409d34bb31f7210e9a43f81400b7a8ae1a951'),(4,'maverick','maverick@gmail.com','scrypt:32768:8:1$J32E63zARTqNPawp$f28fc59a3d68c1e25d76696deee8ca7a231f02a36f92b8e92b6f018016868ba8a09118ef8a30629c14e74ddec49035b4edcc6fffb7e2b1a5a891836ea5bec9b2'),(5,'mimi','mimi@gmail.com','scrypt:32768:8:1$SbUekXgGXIXRhYmG$4d52be15d8a65622dae0a73dd91c37572aaae5709b262e750bf03bc5e7f8cf599e2870022f88d8914ad13de998c323ace98aff39a372da20868934a0ffef6984');
/*!40000 ALTER TABLE `user_account` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-23 18:45:45
