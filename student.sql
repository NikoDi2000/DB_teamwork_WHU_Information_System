查询学生的各种信息
self.sql = "select stu_id,stu_name,sex,stu_birthday,stu_tel,stu_class from student where stu_id = '" + username + "'"
self.sql = "select major_name from major where major_id = '" + str(self.information[5])[0:4] + "'"

查询该学生所选课程
self.sql = "select course_id,course_name,course_type,t_name,credit,time from course natural join t_c natural join teacher natural join s_c where stu_id = '" + username + "'"

查询该学生的各科成绩
self.sql = "select term_start,course_id,course_name,t_name,credit,score from s_c natural join course natural join teacher natural join t_c where stu_id = " + username

查询该学生的各科学费
self.sql = "select course_id,course_name,credit,tuition from s_c natural join course where stu_id = " + username + " and term_start>= " + str(termstart) + " and term_end <= " + str(termend)
self.sql = "select major_fee from major where major_id =  " + str(self.information[5])[0:4]

必修课
self.sql = "select course_id,course_name,t_name,credit,time from course natural join t_c natural join teacher where course_type = '必修'"

选修课
self.sql = "select course_id,course_name,t_name,credit,time from course natural join t_c natural join teacher where course_type = '选修'"

选课
self.sql = "insert into s_c(stu_id,course_id) values(" + username + ", " + self.course_id + ")"

撤课
self.sql = "delete from s_c where stu_id = '" + username + "' and course_id ='" + self.delete + "'"
