/*
Navicat MySQL Data Transfer

Source Server         : db
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : news

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-06-16 21:17:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for news
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `ID` varchar(20) NOT NULL,
  `splitTitle` varchar(255) DEFAULT NULL,
  `splitContent` longtext,
  `c0` varchar(255) DEFAULT NULL,
  `weight` double DEFAULT NULL,
  `c1` varchar(255) DEFAULT NULL,
  `sc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
