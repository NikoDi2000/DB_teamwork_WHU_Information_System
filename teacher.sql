登陆页面
self.sql_s = "select stu_id,stu_tel from student"
self.sql_t = "select t_id,t_tel from teacher"
           
教师端基本信息
self.sql = "select t_id,t_name,sex,t_birthday, t_tel from teacher where t_id = '" + username + "'"
           
查询课程下的学生信息&给分
self.sql = "select stu_id,stu_name,stu_class,score from s_c natural join student where course_id='" + current_lesson + "'"

修改学生的分数
self.sql = "update s_c set score=" + score + " where stu_id=" + current_student
          
忘记密码页面 
self.sql = "update student set password = '" + self.ui.new_password.text() + "' where stu_id = " + self.ui.username.text()
           