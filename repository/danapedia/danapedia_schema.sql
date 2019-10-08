DROP DATABASE IF EXISTS danapedia;
CREATE DATABASE danapedia;
use danapedia;

CREATE TABLE `users` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pass_hash` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `texts` (
  `id_text` int(11) NOT NULL AUTO_INCREMENT,
  `id_article` int(11) DEFAULT NULL,
  `text` TEXT DEFAULT NULL,
  `current` tinyint(4) DEFAULT NULL,
  `saved_date` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_text`),
  KEY `fk_article_idx` (`id_article`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;

CREATE TABLE `articles` (
  `id_article` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `id_text` int(11) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_article`),
  KEY `fk_text_idx` (`id_text`),
  KEY `fk_user_idx` (`id_user`),
  CONSTRAINT `fk_text` FOREIGN KEY (`id_text`) REFERENCES `texts` (`id_text`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_user` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;

ALTER TABLE `texts`ADD CONSTRAINT `fk_article` FOREIGN KEY (`id_article`) REFERENCES `articles` (`id_article`) ON DELETE NO ACTION ON UPDATE NO ACTION;


