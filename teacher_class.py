from tkinter import *
import tets

class Teacher:
    def __init__(self,TNO):
        self.TNO=TNO
        self.root = Tk()
        self.root.title(TNO)
        self.root.geometry("900x400")
        self.course_label = Label(self.root, text="请选择课程名：")
        self.student_label = Label(self.root, text="已选修此课程的学生：")
        self.student_text = Text(self.root, width=20, height=10)
        self.lb = Listbox(self.root, width=20, height=10)
        Label(self.root,text="学号：").grid(row=3,column=3)
        Label(self.root, text="成绩：").grid(row=5, column=3)
        self.student_id_entry = Entry(self.root, text="学号",width=5)
        self.student_grape_entry = Entry(self.root, text="成绩",width=5)
        self.student_button = Button(self.root, text="查询", command=self.find_score)
        self.score_button =Button(self.root, text="输入成绩", command=self.change_score)

    def inilize(self):
        self.course_label.grid(row=1, column=0)
        self.student_label.grid(row=1, column=1)
        self.student_text.grid(row=2, column=1)
        var = StringVar()
        for item in tets.find_teacher_course(self.TNO):
            self.lb.insert(END, item)
        self.lb.grid(row=2, column=0)
        self.student_id_entry.grid(row=4, column=3)
        self.student_grape_entry.grid(row=6, column=3)
        # 查询
        self.student_button.grid(row=4, column=0)
        # 输入成绩
        self.score_button.grid(row=4, column=1)

    # 查询选了该老师该课的学生成绩
    def find_score(self):
        CNAME = self.lb.get(self.lb.curselection())[0]
        self.student_text.delete(1.0, END)
        tets.find_student_score(self.student_text, CNAME, self.TNO)
    #修改成绩
    def change_score(self):
        SNO = self.student_id_entry.get()
        GRADE = self.student_grape_entry.get()
        CNAME = self.lb.get(self.lb.curselection())[0]
        tets.change_score(SNO, GRADE, CNAME)
        self.find_score()

    def start(self):
        self.inilize()
        self.root.mainloop()

if __name__=='__main__':
    c=Teacher('刘红')
    c.start()