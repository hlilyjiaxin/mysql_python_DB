from tkinter import *
import tets

class course:
    def __init__(self,SNO):
        self.root = Tk()
        self.root.wm_title(SNO)
        self.root.geometry("900x400")
        self.SNO=SNO
        self.student_label = Label(self.root, text="学生详细信息：")
        self.course_label = Label(self.root, text="可选课程")
        self.score_label = Label(self.root, text="已修课程成绩")
        self.choose_course_label = Label(self.root, text="已选课程")
        self.course_entry_label = Label(self.root, text="请输入课程号：")
        self.student_text = Text(self.root, height=10, width=50)
        self.course_text = Text(self.root, height=10, width=50)
        self.score_text = Text(self.root, height=10, width=50)
        self.choose_course_text = Text(self.root, height=10, width=50)
        self.course_entry = Entry(self.root, width=5)
        self.course_button = Button(self.root, text="选课", command=self.choose_course)
        self.course_button2 = Button(self.root, text="退课", command=self.delete_course)
        self.course_button3 = Button(self.root, text="关闭")
    def inilize(self):
        self.student_label.grid(row=0, column=0, sticky=W)
        self.student_text.grid(row=1, column=0, sticky=E)
        self.course_label.grid(row=0, column=1, sticky=W)
        self.course_text.grid(row=1, column=1, sticky=E)
        self.score_label.grid(row=3, column=0, sticky=W)
        self.score_text.grid(row=4, column=0, sticky=E)
        self.choose_course_label.grid(row=3, column=1, sticky=W)
        self.choose_course_text.grid(row=4, column=1, sticky=E)
        self.course_entry_label.grid(row=0, column=3)
        self.course_entry.grid(row=1, column=3)
        self.course_button.grid(row=1, column=4)
        self.course_button2.grid(row=2, column=4)
        self.course_button3.grid(row=4, column=4)

    # 选课
    def choose_course(self):
        course_number = self.course_entry.get()
        tets.insert_choose_course(self.SNO, str(course_number), 0)
        self.update_ui()

    # 退课
    def delete_course(self):
        course_number = self.course_entry.get()
        tets.delete_choose_course(str(course_number))
        self.update_ui()

    # 更新ui
    def update_ui(self):
        self.student_text.delete(1.0, END)
        self.course_text.delete(1.0, END)
        self.score_text.delete(1.0, END)
        self.choose_course_text.delete(1.0, END)
        tets.display_student(self.student_text, self.SNO)
        tets.display_course(self.course_text, self.SNO)
        tets.display_score(self.score_text, self.SNO)
        tets.display_choose_course(self.choose_course_text, self.SNO)

    def start(self):
        self.inilize()
        self.update_ui()
        self.root.mainloop()


if __name__=='__main__':
    c=course('S5')
    c.start()