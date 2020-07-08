#import os
#envpath = r'home/dxs/anaconda3/lib/python3.7/site-packages/PySide2/plugins/platforms'
#os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = envpath
from PySide2.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
import sqlite3
import sys 

database = sqlite3.connect('WHU.db')
cursor = database.cursor()
username = ''
is_t = 0
is_s = 0
    
class MainWindow:
    def __init__(self):
        
        self.ui = QUiLoader().load('mainwindow.ui')
        self.ui.LoginButton.clicked.connect(self.Login)

    def Login(self):
        global is_t, is_s, username
        self.sql_s = "select stu_id,password from student"
        self.sql_t = "select t_id,password from teacher"
        cursor.execute(self.sql_s)
        self.result_s = cursor.fetchall()
        cursor.execute(self.sql_t)
        self.result_t = cursor.fetchall()
        self.result = self.result_s + self.result_t

        if (int(self.ui.Login_username.text()),self.ui.Login_password.text()) in self.result:
            username = self.ui.Login_username.text()
            if (int(self.ui.Login_username.text()),self.ui.Login_password.text()) in self.result_t:
                is_t = 1
            else:
                is_s = 1
            self.ui.close()
        else:
            QMessageBox.warning(self.ui,'登录失败','账号或密码输入错误，请重新输入')


class Password:
    def __init__(self):
        self.ui = QUiLoader().load('recover_password.ui')
        self.ui.confirmButton.clicked.connect(self.Confirm)
        
    def Confirm(self):
        self.sql_s = "select stu_id,stu_tel from student"
        self.sql_t = "select t_id,t_tel from teacher"
        cursor.execute(self.sql_s)
        self.result_s = cursor.fetchall()
        cursor.execute(self.sql_t)
        self.result_t = cursor.fetchall()
        self.result = self.result_s + self.result_t
        self.is_t = 0
        self.is_s = 0

        if (int(self.ui.username.text()),int(self.ui.tel_number.text())) in self.result:
            if (int(self.ui.username.text()),int(self.ui.tel_number.text())) in self.result_s:
                self.is_s = 1
            else:
                self.is_t = 1
            if self.ui.new_password.text() == self.ui.confirm_password.text():
                if self.is_s:
                    self.sql = "update student set password = '" + self.ui.new_password.text() + "' where stu_id = " + self.ui.username.text()
                if self.is_t:
                    self.sql = "update teacher set password = '" + self.ui.new_password.text() + "' where t_id = " + self.ui.username.text() 
                cursor.execute(self.sql)
                self.ui.close()
            else:
                QMessageBox.warning(self.ui,'输入错误','两次密码输入不一致')
        else:
            QMessageBox.warning(self.ui,'查无用户','请检查您输入的账号和手机号是否正确')

class Teacher:
    def __init__(self):
        global username
        self.ui = QUiLoader().load('teacherform.ui')
        self.sql = "select t_id,t_name,sex,t_birthday, t_tel from teacher where t_id = '" + username + "'"
        cursor.execute(self.sql)
        self.information = cursor.fetchone()
        self.ui.label_14.setText(str(self.information[0]))
        self.ui.label_15.setText(self.information[1])
        self.ui.label_16.setText(self.information[2])
        self.ui.label_17.setText(self.information[3])
        self.ui.label_19.setText(str(self.information[4]))

        self.sql = "select course_id from t_c where t_id = " + username
        cursor.execute(self.sql)
        lessons = cursor.fetchall()
        for lesson in lessons:
            self.ui.comboBox.addItem(str(lesson[0]))
            
        self.change_lesson()
        self.change_table()

        self.ui.comboBox.currentIndexChanged.connect(self.change_lesson)
        self.ui.pushButton.clicked.connect(self.change_score)

    def change_lesson(self):
        self.ui.comboBox_2.clear()
        current_lesson = self.ui.comboBox.currentText()
        self.sql = "select stu_id,stu_name,stu_class,score from s_c natural join student where course_id='" + current_lesson + "'"
        cursor.execute(self.sql)
        self.students = cursor.fetchall()
        for student in self.students:
            self.ui.comboBox_2.addItem(str(student[0]))
        self.change_table()

    def change_table(self):
        self.ui.tableWidget.setRowCount(len(self.students))
        for i in range(len(self.students)):
            for j in range(4):
                item = QTableWidgetItem()
                item.setText(str(self.students[i][j]))
                self.ui.tableWidget.setItem(i,j,item)

    def change_score(self):
        score = self.ui.Login_username.text()
        if score.isdigit():
            if int(score) < 0 or int(score) > 100:
                QMessageBox.warning(self.ui,'输入错误','请输入一个0~100的数字')
            else:
                current_student = self.ui.comboBox_2.currentText()
                self.sql = "update s_c set score=" + score + " where stu_id=" + current_student
                cursor.execute(self.sql)
                self.change_lesson()
        else:
            QMessageBox.warning(self.ui,'输入错误','请检查输入的是否为整数')
            
class Student:
    def __init__(self):
        self.ui = QUiLoader().load('studentform.ui')
        self.sql = "select stu_id,stu_name,sex,stu_birthday,stu_tel,stu_class from student where stu_id = '" + username + "'"
        cursor.execute(self.sql)
        self.information = cursor.fetchone()
        self.ui.label_14.setText(str(self.information[0]))
        self.ui.label_15.setText(self.information[1])
        self.ui.label_16.setText(self.information[2])
        self.ui.label_17.setText(self.information[3])
        self.ui.label_19.setText(str(self.information[4]))
        self.ui.label_20.setText(str(self.information[5]))
        self.sql = "select major_name from major where major_id = " + str(self.information[5])[0:4]
        cursor.execute(self.sql)
        self.major_information = cursor.fetchone()
        self.ui.label_18.setText(self.major_information[0])

        self.change_table_calendar()
        self.change_table_b()
        self.change_table_x()
        self.change_table_score()
        self.change_table_fee()

        self.ui.pushButton_2.clicked.connect(self.select_b)
        self.ui.pushButton_3.clicked.connect(self.select_x)
        self.ui.pushButton_4.clicked.connect(self.delete_c)
        self.ui.pushButton.clicked.connect(self.change_table_fee)
        
    def change_table_calendar(self):
        self.sql = "select course_id,course_name,course_type,t_name,credit,time from course natural join t_c natural join teacher natural join s_c where stu_id = '" + username + "'"
        cursor.execute(self.sql)
        self.lessons = cursor.fetchall()
        self.ui.tableWidget.setRowCount(len(self.lessons))
        for i in range(len(self.lessons)):
            for j in range(6):
                item = QTableWidgetItem()
                item.setText(str(self.lessons[i][j]))
                self.ui.tableWidget.setItem(i,j,item)
                
        self.ui.tableWidget_6.setRowCount(len(self.lessons))
        for i in range(len(self.lessons)):
            for j in range(6):
                item = QTableWidgetItem()
                item.setText(str(self.lessons[i][j]))
                self.ui.tableWidget_6.setItem(i,j,item)
                
        self.ui.comboBox_3.clear()
        for lesson in self.lessons:
            self.ui.comboBox_3.addItem(str(lesson[0]))
                
    def change_table_b(self):
        self.sql = "select course_id,course_name,t_name,credit,time from course natural join t_c natural join teacher where course_type = '必修'"
        cursor.execute(self.sql)
        self.blessons = cursor.fetchall()
        self.ui.tableWidget_4.setRowCount(len(self.blessons))
        for i in range(len(self.blessons)):
            for j in range(5):
                item = QTableWidgetItem()
                item.setText(str(self.blessons[i][j]))
                self.ui.tableWidget_4.setItem(i,j,item)
                
        self.ui.comboBox.clear()
        for lesson in self.blessons:
            self.ui.comboBox.addItem(str(lesson[0]))

    def change_table_x(self):
        self.sql = "select course_id,course_name,t_name,credit,time from course natural join t_c natural join teacher where course_type = '选修'"
        cursor.execute(self.sql)
        self.xlessons = cursor.fetchall()
        self.ui.tableWidget_5.setRowCount(len(self.xlessons))
        for i in range(len(self.xlessons)):
            for j in range(5):
                item = QTableWidgetItem()
                item.setText(str(self.xlessons[i][j]))
                self.ui.tableWidget_5.setItem(i,j,item)
                
        self.ui.comboBox_2.clear()
        for lesson in self.xlessons:
            self.ui.comboBox_2.addItem(str(lesson[0]))

    def select_b(self):
        self.course_id = self.ui.comboBox.currentText()
        self.lesson_selected = []
        for lesson in self.lessons:
            self.lesson_selected.append(lesson[0])
        if int(self.course_id) in self.lesson_selected:
             QMessageBox.warning(self.ui,'错误','本课程已选')
        else:
            self.sql = "insert into s_c(stu_id,course_id) values(" + username + ", " + self.course_id + ")"
            cursor.execute(self.sql)
            self.change_table_calendar()
            self.change_table_score()
            self.change_table_fee()
 
    def select_x(self):
        self.course_id = self.ui.comboBox_2.currentText()
        self.lesson_selected = []
        for lesson in self.lessons:
            self.lesson_selected.append(lesson[0])
        if int(self.course_id) in self.lesson_selected:
             QMessageBox.warning(self.ui,'错误','本课程已选')
        else:
            self.sql = "insert into s_c(stu_id,course_id) values(" + username + "', " + self.course_id + ")"
            cursor.execute(self.sql)
            self.change_table_calendar()
            self.change_table_score()
            self.change_table_fee()

    def delete_c(self):
        self.delete = self.ui.comboBox_3.currentText()
        self.sql = "delete from s_c where stu_id = '" + username + "' and course_id ='" + self.delete + "'"
        cursor.execute(self.sql)
        self.change_table_calendar()
        self.change_table_score()
        self.change_table_fee()

    def change_table_score(self):
        self.sql = "select term_start,course_id,course_name,t_name,credit,score from s_c natural join course natural join teacher natural join t_c where stu_id = " + username
        cursor.execute(self.sql)
        self.scores = cursor.fetchall()
        self.ui.tableWidget_2.setRowCount(len(self.scores))
        for i in range(len(self.scores)):
            for j in range(6):
                item = QTableWidgetItem()
                item.setText(str(self.scores[i][j]))
                self.ui.tableWidget_2.setItem(i,j,item)

    def change_table_fee(self):
        self.fees = 0
        termstart = self.ui.spinBox.value()
        termend = self.ui.spinBox_2.value()
        self.sql = "select course_id,course_name,credit,tuition,term_start,term_end from s_c natural join course where stu_id = " + username + " and term_start>= " + str(termstart) + " and term_end <= " + str(termend)
        cursor.execute(self.sql)
        self.fee = cursor.fetchall()
        self.term_count = []
        self.ui.tableWidget_3.setRowCount(len(self.fee))
        for i in range(len(self.fee)):
            self.term_count.append(self.fee[i][4])
            self.term_count.append(self.fee[i][5])
            for j in range(4):
                if j == 3:
                    self.fees += self.fee[i][j]
                item = QTableWidgetItem()
                item.setText(str(self.fee[i][j]))
                self.ui.tableWidget_3.setItem(i,j,item)
        self.sql = "select major_fee from major where major_id =  " + str(self.information[5])[0:4]
        cursor.execute(self.sql)
        self.major_fee = cursor.fetchone()
        self.ui.label_5.setText(str(self.major_fee[0]))  
        self.year = 1
        if len(self.term_count) != 0:
            self.year =max(self.term_count)-min(self.term_count)
        self.ui.label_3.setText(str(self.major_fee[0] * 2 * self.year + self.fees))

app = QApplication([])
app.setWindowIcon(QIcon('WHU.ico'))
MW = MainWindow()
RP = Password()
    
MW.ui.show()
MW.ui.Forget_password.clicked.connect(RP.ui.show)
app.exec_()
if is_s:
    S = Student()
    S.ui.show()
else:
    T = Teacher()
    T.ui.show()

    
    

