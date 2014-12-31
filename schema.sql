create database if not exists wenwen default charset="utf8";
use wenwen;

DROP TABLE IF EXISTS `question`;
CREATE TABLE `question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(60) DEFAULT NULL,
  `description` varchar(10000) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(250) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `reg_time` datetime DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `n_uped` int(11) DEFAULT 0,
  `n_downed` int(11) DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `answer`;
CREATE TABLE `answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `content` varchar(10000) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `user` VALUES (1,'yhf','pbkdf2:sha1:1000$B3dwLOsI$646bedc8dbe8d4fb6847549e6d71b34eeb464fad','a@b.c','2014-12-21 23:05:00','',0,0),(2,'admin','pbkdf2:sha1:1000$dSkQsb0x$614d526a3d43e0c20382a511e7a3672dec6f4f5f','a@b.cc','2014-12-21 23:05:09','',0,0),(3,'admin2','pbkdf2:sha1:1000$I1nO5zw4$6316761a24ad5cd521973999fe10d878eb18606d',NULL,'2014-12-24 13:48:24',NULL,0,0),(4,'admin3','pbkdf2:sha1:1000$c28XyrZl$20f40ed7e12b4deae614d568e7ebc2bb29789821',NULL,'2014-12-24 13:48:41',NULL,0,0),(5,'yhf2','pbkdf2:sha1:1000$Vugz6MfB$1b58c7801ecc94f205795d3a4ec5354c66df367e',NULL,'2014-12-24 13:55:35',NULL,0,0),(9,'yhf3','pbkdf2:sha1:1000$8TdACp1j$07c138a535988268eecb91861c6e5baf4836c62a',NULL,'2014-12-24 14:06:01',NULL,0,0),(12,'yhf4','pbkdf2:sha1:1000$Fb5l97NA$4d1a0bd512416f808a39020c9127c5680b326302',NULL,'2014-12-24 14:10:28',NULL,0,0),(13,'yhf5','pbkdf2:sha1:1000$ptWw5E1F$300f6d59a5fdcbc940ebf0a85bc786eb1fefd5e5',NULL,'2014-12-24 14:11:02',NULL,0,0),(14,'aaaaabbbbbaaaaabbbbb','pbkdf2:sha1:1000$QTnbsQIm$267f366726e03a92c22a749159e1508aebf04489',NULL,'2014-12-24 14:12:14',NULL,0,0),(16,'yhf09','pbkdf2:sha1:1000$3qe9b6v3$744b1a446b867b3e4516460631d4874765e91fe2',NULL,'2014-12-24 14:18:11',NULL,0,0),(17,'','pbkdf2:sha1:1000$PCjnvEhT$6145de3389ea6db58e803a4d916f5051f6169f58',NULL,'2014-12-28 20:50:50',NULL,0,0),(18,'test','pbkdf2:sha1:1000$Rqvl3sna$3dc5c9d25f2dcf57dbb4ab240ffd3bcbabd5e3a6',NULL,'2014-12-28 20:51:15',NULL,0,0),(19,'test2','pbkdf2:sha1:1000$IC9x2u1t$b4b366ed7ee04a65621b1eac710e35fc86d48a33',NULL,'2014-12-28 20:52:50',NULL,0,0),(20,'test3','pbkdf2:sha1:1000$UJIlcD1B$28a9c5c012fb7eb2fa979948b6d127121ddadd2f',NULL,'2014-12-28 20:53:03',NULL,0,0),(21,'test4','pbkdf2:sha1:1000$tCTsNbya$93196db6f5f9e236001156fb85661d60ddfe0fea',NULL,'2014-12-28 20:54:39',NULL,0,0),(22,'test5','pbkdf2:sha1:1000$Tim7OMia$b08d0aa7d5956dad5557af52f3457634912d9493',NULL,'2014-12-28 20:56:32',NULL,0,0),(23,'test6','pbkdf2:sha1:1000$nYLRjT8I$6ea6c9dc3a802520aba443b2ae9b0463b8791b30',NULL,'2014-12-28 20:59:47',NULL,0,0),(24,'test7','pbkdf2:sha1:1000$6waTenrl$7b11ccbc1e1a8310ae410bc82c909d6333ad852c',NULL,'2014-12-28 20:59:56',NULL,0,0);

INSERT INTO `question` VALUES (1,'第1个问题','这是第1个问题','2014-12-21 23:05:29',1),(2,'第2个问题','这是第2个问题','2014-12-22 23:05:29',2),(3,'第3个问题','这是第3个问题','2014-12-23 23:05:29',2),(4,'第4个问题','这是第4个问题','2014-12-24 23:05:29',1),(5,'第5个问题','这是第5个问题','2014-12-25 23:05:29',1),(6,'第6个问题','这是第6个问题','2014-12-26 23:05:29',1),(7,'第7个问题','这是第7个问题','2014-12-27 23:05:29',2),(8,'第8个问题','这是第8个问题','2014-12-28 23:05:29',1),(9,'第9个问题','这是第9个问题','2014-12-29 23:05:29',1);
