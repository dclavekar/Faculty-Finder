from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage,QPalette,QBrush,QPixmap
from PyQt5.QtWidgets import*
import sys
import os
import excel1 as e
import SlotSelect as s


username=''
app=QtWidgets.QApplication([])
fp=uic.loadUi('FirstPage.ui')
app1=QtWidgets.QApplication([]) #student window
sw=uic.loadUi('studentwindow.ui')
app2=QtWidgets.QApplication([]) #faculty window
fw=uic.loadUi('facultywindow.ui')
app3=QtWidgets.QApplication([])
pdisplay=uic.loadUi('PasswordDisplay.ui')
app4=QtWidgets.QApplication([])
tp=uic.loadUi('TeacherPortal1.ui')
app5=QtWidgets.QApplication([])
rw=uic.loadUi('resultwindow.ui')
app6=QtWidgets.QApplication([])#Calendar
cal=uic.loadUi('cal1.ui')

def studentwin():
    app1.exec()
    fp.setVisible(False)
    sw.setVisible(True)
    o1Image=QImage("bback.png")
    s1Image=o1Image.scaled(QSize(1091,851))
    palette1=QPalette()
    palette1.setBrush(QPalette.Window,QBrush(s1Image))
    sw.setPalette(palette1)
    sw.back_sw.clicked.connect(back_sw)
    #this will lead to previous window

    sw.submitNLW_2.clicked.connect(comboBox)

def comboBox():
    app5.exec()
    sw.setVisible(False)
    rw.setVisible(True)
    o3Image=QImage("nback.jpg")
    s3Image=o3Image.scaled(QSize(1091,425))
    palette3=QPalette()
    palette3.setBrush(QPalette.Window,QBrush(s3Image))
    rw.setPalette(palette3)
    rw.rback.clicked.connect(back_rw)
       
    


    tName=sw.comboBox1_2.currentText()
    #the above will return the value of the selected name in the drop down menu/Combo box
    tSlot=sw.comboBox2_2.currentIndex()
    #the above will get the time slot in string format
    tDate=sw.comboBox2_3.currentIndex()

    #Getting the cell value
    f,r=s.get_slot(tName,tSlot,tDate)
    print(f)
    print(r)
    #a=str(tName)+"  :  "+str(tSlot)
    rw.rfl.setText(f)
    rw.rsl.setText(r)
    

    
  
def facultywin():
    app2.exec()
    fp.setVisible(False)
    fw.setVisible(True)
    o1Image=QImage("bback.png")
    s1Image=o1Image.scaled(QSize(1091,851))
    palette1=QPalette()
    palette1.setBrush(QPalette.Window,QBrush(s1Image))
    fw.setPalette(palette1)
    fw.back_fw.clicked.connect(back_fw)
    #this will lead to previous window

def teacherlogin():
    
    global username
    username=fw.usernameLE.text()
    password=fw.passwordLE.text()

    v=e.logcheck()
    ver=v.verify(username,password)
    passwordDisplay(ver)
    
    
def passwordDisplay(ver):
    app3.exec()
    fw.setVisible(False)
    pdisplay.setVisible(True)
    o1Image=QImage("bback.png")
    s1Image=o1Image.scaled(QSize(1091,851))
    palette1=QPalette()
    palette1.setBrush(QPalette.Window,QBrush(s1Image))
    pdisplay.setPalette(palette1)
    
    if ver==True:
        pdisplay.PasswordDisplayLE.setText('The password is correct')
        pdisplay.proceedPB.clicked.connect(passwordCorrect)

        
    else:
        pdisplay.PasswordDisplayLE.setText('The password is incorrect')
        pdisplay.proceedPB.clicked.connect(passwordIncorrect)


def passwordCorrect():
    app4.exec()
    pdisplay.setVisible(False)
    tp.setVisible(True)
    o1Image=QImage("bback.png")
    s1Image=o1Image.scaled(QSize(1091,851))
    palette1=QPalette()
    palette1.setBrush(QPalette.Window,QBrush(s1Image))
    tp.setPalette(palette1)
    teacherPortal1()


def teacherPortal1():
    #tp1.show()
    #app1.exec()
    tp.EditTTPB.clicked.connect(editTT)
    tp.backPB.clicked.connect(backLogin)
    tp.MarkLeavePB.clicked.connect(opencal)
    

def editTT():
	os.startfile(username+'.xlsx')

def opencal():
    app6.exec()
    cal.setVisible(True)
    cal.pushButton.clicked.connect(markLeave)
	
def markLeave():
	#please add the required code
	#pass
        
    
    t=str(cal.calendarWidget.selectedDate())
    t=t.lstrip('PyQt5.QtCore.QDate')
    t=t.lstrip('(')
    t=t.rstrip(')')
    z=t.split(',')
    z=[i.lstrip(' ') for i in z]
    d=[]
    for i in z:
        if len(i)==1:
            d.append('0'+i)
        else:
            d.append(i)
   
            
    u=('-'.join(d))
    print(u)
        
    f=open(username+'.txt','a')
    f.write('\n')
    f.write(u)
    f.close()

def passwordIncorrect():
    pdisplay.setVisible(False)
    fw.setVisible(True)

def backLogin():
    tp.setVisible(False)
    fw.setVisible(True)
    fw.usernameLE.setText("")
    
    fw.passwordLE.setText("")

def back_fw():
    fw.setVisible(False)
    fp.setVisible(True)
def back_sw():
    sw.setVisible(False)
    fp.setVisible(True)
def back_rw():
    rw.setVisible(False)
    sw.setVisible(True)

fp.student_button.clicked.connect(studentwin)
fw.proceedFW.clicked.connect(teacherlogin)#this is the change.LOL
fp.teacher_button.clicked.connect(facultywin)
oImage=QImage("back.png")
sImage=oImage.scaled(QSize(939,939))
palette=QPalette()
palette.setBrush(QPalette.Window,QBrush(sImage))
fp.setPalette(palette)

fp.show()
app.exec()

