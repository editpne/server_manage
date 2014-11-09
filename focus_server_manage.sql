/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50612
Source Host           : localhost:3306
Source Database       : focus_server_manage

Target Server Type    : MYSQL
Target Server Version : 50612
File Encoding         : 65001

Date: 2014-11-09 23:24:19
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `s_application`
-- ----------------------------
DROP TABLE IF EXISTS `s_application`;
CREATE TABLE `s_application` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(35) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of s_application
-- ----------------------------
INSERT INTO `s_application` VALUES ('1', 'nginx前端');
INSERT INTO `s_application` VALUES ('2', 'Mysql数据库');
INSERT INTO `s_application` VALUES ('3', 'apache前端');

-- ----------------------------
-- Table structure for `s_business`
-- ----------------------------
DROP TABLE IF EXISTS `s_business`;
CREATE TABLE `s_business` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(35) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of s_business
-- ----------------------------
INSERT INTO `s_business` VALUES ('1', '论坛');
INSERT INTO `s_business` VALUES ('2', '新房');
INSERT INTO `s_business` VALUES ('3', '家居');
INSERT INTO `s_business` VALUES ('4', '二手房');
INSERT INTO `s_business` VALUES ('5', 'WEB');
INSERT INTO `s_business` VALUES ('7', 'ok');

-- ----------------------------
-- Table structure for `s_idc`
-- ----------------------------
DROP TABLE IF EXISTS `s_idc`;
CREATE TABLE `s_idc` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(55) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of s_idc
-- ----------------------------
INSERT INTO `s_idc` VALUES ('1', '兆维');
INSERT INTO `s_idc` VALUES ('2', '酒仙桥');

-- ----------------------------
-- Table structure for `s_isp`
-- ----------------------------
DROP TABLE IF EXISTS `s_isp`;
CREATE TABLE `s_isp` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of s_isp
-- ----------------------------
INSERT INTO `s_isp` VALUES ('1', '中国电信');
INSERT INTO `s_isp` VALUES ('2', '中国联通');
INSERT INTO `s_isp` VALUES ('3', '中国移动');
INSERT INTO `s_isp` VALUES ('4', '中国铁通');

-- ----------------------------
-- Table structure for `s_servers`
-- ----------------------------
DROP TABLE IF EXISTS `s_servers`;
CREATE TABLE `s_servers` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(35) NOT NULL DEFAULT '',
  `ip_addr` char(15) NOT NULL DEFAULT '0',
  `isp_id` smallint(5) NOT NULL DEFAULT '0',
  `idc_id` smallint(4) NOT NULL DEFAULT '0',
  `environment` tinyint(4) NOT NULL DEFAULT '0',
  `business_id` smallint(5) NOT NULL DEFAULT '0',
  `application_id` smallint(5) NOT NULL DEFAULT '0',
  `cluster` varchar(55) NOT NULL DEFAULT '',
  `role` tinyint(4) NOT NULL DEFAULT '0',
  `head_name` varchar(35) NOT NULL DEFAULT '',
  `status` tinyint(1) NOT NULL DEFAULT '0',
  `sort_order` tinyint(4) unsigned NOT NULL DEFAULT '100',
  `user_id` mediumint(8) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_ipaddr` (`ip_addr`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of s_servers
-- ----------------------------
INSERT INTO `s_servers` VALUES ('1', '论坛测试机', '192.168.242.28', '1', '2', '2', '2', '2', '55555', '2', '于振国', '2', '100', '1');
INSERT INTO `s_servers` VALUES ('2', 'oop', '192.168.242.151', '2', '2', '2', '2', '2', 'oop', '2', 'yuzhenguo', '1', '102', '1');
INSERT INTO `s_servers` VALUES ('3', 'abd', '2', '1', '1', '3', '3', '1', 'abd', '1', 'yuguoguo', '1', '100', '1');
INSERT INTO `s_servers` VALUES ('4', '论坛开发服务器', '1010', '2', '2', '3', '1', '1', 'web1', '3', '龙念', '1', '100', '1');

-- ----------------------------
-- Table structure for `s_users`
-- ----------------------------
DROP TABLE IF EXISTS `s_users`;
CREATE TABLE `s_users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uname` varchar(55) NOT NULL DEFAULT '',
  `passwd` char(32) NOT NULL DEFAULT '',
  `real_name` varchar(35) NOT NULL DEFAULT '',
  `role` tinyint(1) NOT NULL DEFAULT '0',
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `idx_uname` (`uname`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of s_users
-- ----------------------------
INSERT INTO `s_users` VALUES ('1', 'yuzhenguo', 'c0ebaa5b5646c148850c3ee465329bed', '于振国', '0', '1');
INSERT INTO `s_users` VALUES ('2', '1111', '698d51a19d8a121ce581499d7b701668', '111', '0', '1');
INSERT INTO `s_users` VALUES ('3', '222', 'bcbe3365e6ac95ea2c0343a2395834dd', '222', '0', '1');
INSERT INTO `s_users` VALUES ('4', '333', '310dcbbf4cce62f762a2aaa148d556bd', '333', '0', '1');
INSERT INTO `s_users` VALUES ('6', '777', 'f1c1592588411002af340cbaedd6fc33', '777', '0', '1');
