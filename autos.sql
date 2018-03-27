/*
 Navicat Premium Data Transfer

 Source Server         : localhost_mysql_5.7.11
 Source Server Type    : MySQL
 Source Server Version : 50711
 Source Host           : localhost
 Source Database       : autos

 Target Server Type    : MySQL
 Target Server Version : 50711
 File Encoding         : utf-8

 Date: 03/27/2018 15:26:08 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `auto_submit_msg`
-- ----------------------------
DROP TABLE IF EXISTS `auto_submit_msg`;
CREATE TABLE `auto_submit_msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(512) DEFAULT NULL COMMENT '回复的信息',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `upd_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `auto_talk_msg`
-- ----------------------------
DROP TABLE IF EXISTS `auto_talk_msg`;
CREATE TABLE `auto_talk_msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(512) DEFAULT NULL COMMENT '回复的信息',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `upd_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `auto_talk_msg`
-- ----------------------------
BEGIN;
INSERT INTO `auto_talk_msg` VALUES ('1', '孙悟空', '2018-03-27 13:52:11', '2018-03-27 13:52:13');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
