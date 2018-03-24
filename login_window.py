from tkinter import *
import course_class
import teacher_class
import pymysql
def judge():
    login=user_entry.get()
    password=password_entry.get()
    db = pymysql.connect('localhost', 'root', 'huangxiao', 'student', charset='utf8')
    cursor = db.cursor()
    sql = "SELECT S.SNO FROM S where S.LOGN='%s' and S.PSWD='%s'" % (login,password)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result)==0:
        cursor = db.cursor()
        sql = "SELECT T.TNAME FROM T where T.LOGN='%s' and T.PSWD='%s'" % (login, password)
        cursor.execute(sql)
        result = cursor.fetchall()
    else:
        return result
    return result

def start():

    result=judge()
    if len(result)!=0:
        root.destroy()
        if result[0][0][0]=='S':
            c=course_class.course(result[0][0])
            c.start()
        else:
            t=teacher_class.Teacher(result[0][0])
            t.start()
    else:
        Label(root, text="用户名或密码错误，请重新输入").grid(row=3, column=1)

root = Tk()
root.title("用户登录界面")
root.geometry("300x200")

Label(root,text="用户名").grid(row=0,column=0)
user_entry=Entry(root,width=15)
user_entry.grid(row=0,column=1)
Label(root,text="密码").grid(row=1,column=0)
password_entry=Entry(root,width=15)
password_entry.grid(row=1,column=1)

star_button=Button(root,text="登陆",command=start)
star_button.grid(row=2,column=1)
root.mainloop()