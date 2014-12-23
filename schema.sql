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



INSERT INTO `user` VALUES (1,'yhf','pbkdf2:sha1:1000$B3dwLOsI$646bedc8dbe8d4fb6847549e6d71b34eeb464fad','a@b.c','2014-12-21 23:05:00','',0,0),(2,'admin','pbkdf2:sha1:1000$dSkQsb0x$614d526a3d43e0c20382a511e7a3672dec6f4f5f','a@b.cc','2014-12-21 23:05:09','',0,0);

INSERT INTO `question` VALUES (NULL,'第1个问题','这是第1个问题','2014-12-21 23:05:29',1);
INSERT INTO `question` VALUES (NULL,'第2个问题','这是第2个问题','2014-12-22 23:05:29',2);
INSERT INTO `question` VALUES (NULL,'第3个问题','这是第3个问题','2014-12-23 23:05:29',2);
INSERT INTO `question` VALUES (NULL,'第4个问题','这是第4个问题','2014-12-24 23:05:29',1);
INSERT INTO `question` VALUES (NULL,'第5个问题','这是第5个问题','2014-12-25 23:05:29',1);
INSERT INTO `question` VALUES (NULL,'第6个问题','这是第6个问题','2014-12-26 23:05:29',1);
INSERT INTO `question` VALUES (NULL,'第7个问题','这是第7个问题','2014-12-27 23:05:29',2);
INSERT INTO `question` VALUES (NULL,'第8个问题','这是第8个问题','2014-12-28 23:05:29',1);
INSERT INTO `question` VALUES (NULL,'第9个问题','这是第9个问题','2014-12-29 23:05:29',1);
