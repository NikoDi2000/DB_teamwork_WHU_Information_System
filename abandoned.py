'''
一个机票预订信息系统
系统功能基本要求：
能够实现多种关联查询
可参考：
航班基本信息的录入：航班的编号、飞机名称、机舱等级等
机票信息：票价、折扣、联系方式、证件及号码、付款情况等
客户基本信息：姓名、联系方式、证件及号码、付款情况等
'''
import tkinter as tk
from tkinter import messagebox
import pickle

# window init
window = tk.Tk()
window.title('Welcome to our system')
window.geometry('900x600')

tk.Label(window, text = 'AirCrash Airline\nTicket Reservation System',font = 'Helvetica 50').pack(pady = 100)
# user information
user_frame = tk.Frame(window)
window.geometry('200x100')
tk.Label(user_frame, text = 'User name', font = 'Helvetica 30').pack()
tk.Label(user_frame, text = 'Password', font = 'Helvetica 30').pack()
user_frame.pack()



var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable = var_usr_name).place(x = 320, y = 300)
var_usr_pw = tk.StringVar()
entry_usr_pw = tk.Entry(window, textvariable = var_usr_pw, show = '*').place(x = 320, y = 380)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pw = var_usr_pw.get()
    try:
        with open('usrs_info','rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info','wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info,usr_file)
    if usr_name in usrs_info:
        if usr_pw == usrs_info[usr_name]:
            tk.messagebox.showinfo(title = '登录成功', message = 'hahaha')
        else:
            tk.messagebox.showerror(message='输入错误')
    else:
        is_sign_up = tk.messagebox.askyesno('未注册')
        if is_sign_up:
            usr_sign_up()

def usr_sign_up():
    def sign_to_system():
        np = new_pw.get()
        npcf = new_pw_confirm.get()
        nn = new_name.get()
        with open('usrs_info','rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npcf:
            tk.messagebox.showerror('错误','两次输入的密码不同，请重新输入')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('错误','帐号已存在')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo('欢迎','注册成功')
            window_sign_up.destroy()
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('700x400')
    window_sign_up.title('注册')

    new_name = tk.StringVar()
    tk.Label(window_sign_up,text = '用户名').place(x = 20, y = 20)
    entry_new_name = tk.Entry(window_sign_up, textvariable = new_name)
    entry_new_name.place(x = 300, y = 20)

    new_pw = tk.StringVar()
    tk.Label(window_sign_up,text = '密码').place(x = 20, y = 100)
    entry_usr_pw = tk.Entry(window_sign_up, textvariable = new_pw, show = '*')
    entry_usr_pw.place(x = 300, y = 100)
    
    new_pw_confirm = tk.StringVar()
    tk.Label(window_sign_up,text = '确认密码').place(x = 20, y = 180)
    entry_usr_pw_cf = tk.Entry(window_sign_up, textvariable = new_pw_confirm, show = '*')
    entry_usr_pw_cf.place(x = 300, y = 180)

    btn_confirm_sign_up = tk.Button(window_sign_up, text = '注册', command = sign_to_system)
    btn_confirm_sign_up.place(x = 300, y = 260)

btn_login = tk.Button(window, text = '登录',command = usr_login).place(x = 340, y = 460)
btn_sign_up = tk.Button(window, text = '注册',command = usr_sign_up).place(x = 540, y = 460)

window.mainloop()





