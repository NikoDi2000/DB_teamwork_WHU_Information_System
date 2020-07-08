CREATE TABLE `course` (
  `course_id` decimal(4,0) NOT NULL,
  `course_name` varchar(16) COLLATE utf8_bin NOT NULL,
  `credit` decimal(1,0) NOT NULL,
  `course_type` varchar(6) COLLATE utf8_bin NOT NULL,
  `time` varchar(16) COLLATE utf8_bin NOT NULL,
  `tuition` decimal(5,0) NOT NULL,
  `term_start` decimal(4,0) NOT NULL,
  `term_end` decimal(4,0) NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES ('1801', '数据库', '3', '必修', '周二3-5', '300', '2019', '2020');
INSERT INTO `course` VALUES ('1802', '机器学习', '3', '必修', '周四3-5', '300', '2018', '2019');
INSERT INTO `course` VALUES ('1803', '数据新闻', '2', '选修', '周二1-2', '200', '2019', '2020');
INSERT INTO `course` VALUES ('1804', '专业英语', '2', '选修', '周一6-8', '200', '2018', '2019');
INSERT INTO `course` VALUES ('1901', '汇编语言', '2', '选修', '周三3-4', '200', '2018', '2019');
INSERT INTO `course` VALUES ('1902', '数据结构', '3', '必修', '周三6-8', '300', '2019', '2020');
INSERT INTO `course` VALUES ('1903', '近代史', '3', '必修', '周五3-5', '300', '2019', '2020');

-- ----------------------------
-- Table structure for `major`
-- ----------------------------
DROP TABLE IF EXISTS `major`;
CREATE TABLE `major` (
  `major_id` decimal(4,0) NOT NULL,
  `major_name` varchar(16) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`major_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of major
-- ----------------------------
INSERT INTO `major` VALUES ('1001', '信息安全');
INSERT INTO `major` VALUES ('1002', '网络空间安全');
INSERT INTO `major` VALUES ('2001', '计算机科学');
INSERT INTO `major` VALUES ('2002', '软件工程');

-- ----------------------------
-- Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `stu_id` decimal(6,0) NOT NULL,
  `stu_name` varchar(8) CHARACTER SET utf8 NOT NULL,
  `sex` varchar(2) CHARACTER SET utf8 NOT NULL,
  `stu_birthday` date NOT NULL,
  `stu_tel` decimal(8,0) NOT NULL,
  `stu_class` decimal(6,0) NOT NULL,
  `password` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('180001', '刘晨', '女', '2001-08-14', '87265432', '100101', 'lc0814');
INSERT INTO `student` VALUES ('180002', '冯燕', '女', '2000-09-27', '88952346', '100201', 'qwerty');
INSERT INTO `student` VALUES ('180003', '吴磊', '男', '1999-12-28', '80123456',  '100101', 'abc123');
INSERT INTO `student` VALUES ('190001', '邸肖烁', '男', '2000-05-16', '89030031', '100202', '123456');
INSERT INTO `student` VALUES ('190002', '刘洁', '女', '2001-09-09', '82170568', '200101', '200109');
INSERT INTO `student` VALUES ('190003', '欧阳杨', '男', '2001-03-26', '89176543', '200201', '010326');

-- ----------------------------
-- Table structure for `s_c`
-- ----------------------------
DROP TABLE IF EXISTS `s_c`;
CREATE TABLE `s_c` (
  `stu_id` decimal(6,0) NOT NULL,
  `course_id` decimal(4,0) NOT NULL,
  `score` decimal(2,0) NOT NULL,
  PRIMARY KEY (`stu_id`,`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of s_c
-- ----------------------------
INSERT INTO `s_c` VALUES ('180001', '1801', '93');
INSERT INTO `s_c` VALUES ('180001', '1802', '89');
INSERT INTO `s_c` VALUES ('180001', '1803', '88');
INSERT INTO `s_c` VALUES ('180001', '1804', '94');
INSERT INTO `s_c` VALUES ('180002', '1801', '85');
INSERT INTO `s_c` VALUES ('180002', '1802', '84');
INSERT INTO `s_c` VALUES ('180003', '1801', '90');
INSERT INTO `s_c` VALUES ('180003', '1802', '91');
INSERT INTO `s_c` VALUES ('180003', '1803', '86');
INSERT INTO `s_c` VALUES ('190001', '1901', '75');
INSERT INTO `s_c` VALUES ('190001', '1902', '81');
INSERT INTO `s_c` VALUES ('190002', '1901', '82');
INSERT INTO `s_c` VALUES ('190002', '1902', '83');
INSERT INTO `s_c` VALUES ('190002', '1903', '84');
INSERT INTO `s_c` VALUES ('190003', '1902', '85');
INSERT INTO `s_c` VALUES ('190003', '1903', '86');


-- ----------------------------
-- Table structure for `teacher`
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `t_id` decimal(6,0) NOT NULL,
  `t_name` varchar(8) COLLATE utf8_bin NOT NULL,
  `sex` varchar(2) COLLATE utf8_bin NOT NULL,
  `t_birthday` varchar(10) COLLATE utf8_bin NOT NULL,
  `t_tel` decimal(11,0) NOT NULL,
  `password` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`t_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('100001', '王致博', '男', '03-05', '13478923069', 'database01');
INSERT INTO `teacher` VALUES ('100002', '李琛亮', '男', '01-24', '18759883254', 'ml10086');
INSERT INTO `teacher` VALUES ('100003', '史笑川', '男', '02-12', '13890260314', '321321');
INSERT INTO `teacher` VALUES ('100004', '蔡衡津', '男', '12-29', '15029063839', 'asdfghjkl');
INSERT INTO `teacher` VALUES ('100005', '董宏彬', '女', '05-28', '13020345875', 'zxcvbnm');
INSERT INTO `teacher` VALUES ('100006', '张楚', '女', '11-13', '18209169876', '11122234');

-- ----------------------------
-- Table structure for `t_c`
-- ----------------------------
DROP TABLE IF EXISTS `t_c`;
CREATE TABLE `t_c` (
  `course_id` decimal(4,0) NOT NULL,
  `t_id` decimal(6,0) NOT NULL,
  PRIMARY KEY (`course_id`,`t_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of t_c
-- ----------------------------
INSERT INTO `t_c` VALUES ('1801', '100001');
INSERT INTO `t_c` VALUES ('1802', '100002');
INSERT INTO `t_c` VALUES ('1803', '100003');
INSERT INTO `t_c` VALUES ('1804', '100002');
INSERT INTO `t_c` VALUES ('1901', '100004');
INSERT INTO `t_c` VALUES ('1902', '100005');
INSERT INTO `t_c` VALUES ('1903', '100006');

