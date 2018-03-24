#!/usr/bin/python3
# coding=utf-8
import pymysql
import numpy as np
from tkinter import *

#选课
def insert_choose_course(SNO,CNO,GRADE):
    db = pymysql.connect('localhost', 'root', 'huangxiao','student',charset='utf8')
    cursor = db.cursor()
    sql = "insert ignore SC (SNO,CNO,GRADE) values ('%s','%s',%d)" % (SNO,CNO,GRADE)
    cursor.execute(sql)
    db.commit()
    db.close()
#退课
def delete_choose_course(CNO):
    db = pymysql.connect('localhost', 'root', 'huangxiao','student',charset='utf8')
    cursor = db.cursor()
    sql = "delete from SC where CNO = '%s'" % CNO
    cursor.execute(sql)
    db.commit()
    db.close()

#打印学生信息
def display_student(text,LOGN):
    db = pymysql.connect('localhost', 'root', 'huangxiao', 'student',charset='utf8')
    cursor = db.cursor()
    sql = "SELECT * FROM S where S.LOGN='%s'"%LOGN
    cursor.execute(sql)
    col=[]
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END,'%s %4s %4s %4s %4s'%tuple(col[0:5]))
    text.insert(END,'\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END,'%s %4s %4s %4s %4s'%tuple(row[0:5]))
        text.insert(END,'\n')
    db.close()

#显示可选课程
def display_course(text,SNO):
    db = pymysql.connect('localhost', 'root', 'huangxiao', 'student',charset='utf8')
    cursor = db.cursor()
    sql = "select * from C where CNO not in (select C.CNO from  S,SC,C where S.SNO=SC.SNO and C.CNO=SC.CNO and S.SNO='%s')"%SNO
    cursor.execute(sql)
    col=[]
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END,col)
    text.insert(END,'\n')

    result = cursor.fetchall()

    for row in result:
        text.insert(END,row)
        text.insert(END,'\n')
    db.close()

#显示已选课程
def display_choose_course(text,SNO):
    db = pymysql.connect('localhost', 'root', 'huangxiao', 'student',charset='utf8')
    cursor = db.cursor()
    sql = "select C.CNO,C.CNAME,C.CREDI,C.CDEPT,C.TNAME from  S,SC,C where S.SNO=SC.SNO and C.CNO=SC.CNO and S.SNO='%s'" % SNO
    cursor.execute(sql)
    col=[]
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END,col)
    text.insert(END,'\n')

    result = cursor.fetchall()

    for row in result:
        text.insert(END,row)
        text.insert(END,'\n')
    db.close()

#显示学生成绩
def display_score(text,SNO):
    db = pymysql.connect('localhost', 'root', 'huangxiao', 'student',charset='utf8')
    cursor = db.cursor()
    sql = "select C.CNO,C.CNAME,GRADE from  S,SC,C where S.SNO=SC.SNO and C.CNO=SC.CNO and S.SNO='%s'"%SNO
    cursor.execute(sql)
    col=[]
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END,col)
    text.insert(END,'\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END,row)
        text.insert(END,'\n')
    db.close()
#老师所上的课程
def find_teacher_course(name):
    db = pymysql.connect('localhost', 'root', 'huangxiao', 'student',charset='utf8')
    cursor = db.cursor()
    sql = "SELECT CNAME FROM C where TNAME='%s'" % name
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result

#查询选了该老师该课的学生
def find_student_score(text,CNAME,TNAME):
    db = pymysql.connect('localhost', 'root', 'huangxiao', 'student',charset='utf8')
    cursor = db.cursor()
    sql = "select S.SNO,S.SNAME,SC.GRADE from  S,SC,C where S.SNO=SC.SNO and C.CNO=SC.CNO and C.CNAME='%s' and C.TNAME='%s'"%(CNAME,TNAME)
    cursor.execute(sql)
    col=[]
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END,col)
    text.insert(END,'\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END,row)
        text.insert(END,'\n')
    db.close()

#老师修改成绩
def change_score(SNO,GRADE,CNAME):
    db = pymysql.connect('localhost', 'root', 'huangxiao', 'student', charset='utf8')
    cursor = db.cursor()

    sql = "select CNO from  C where CNAME='%s'" % (CNAME)
    cursor.execute(sql)
    result = cursor.fetchall()
    sql = "replace into SC (SNO,CNO,GRADE) values ('%s','%s',%d)" % (SNO, result[0][0], int(GRADE))
    cursor.execute(sql)
    db.commit()
    db.close()


