from tkinter import *

import tkinter.messagebox 
import sqlite3
from tkinter import scrolledtext
from sqlite3 import dbapi2 as sqlite

from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import time
import datetime
import random

#from PIL import ImageTk
#import fud

con = sqlite3.connect("supermarket.db")
cursor = con.cursor()

con.commit()
#con.close()


#from PIL import ImageTk

#for calling different interfaces
def handle(frame):
    frame.tkraise()

window = tk.Tk()
window.geometry('8000x8000')
window.title("DIAZ BUSINESS DEVELOPER")

frame5 = Frame(window,bg= 'turquoise',width = 8000,height= 8000)
frame1 = Frame(window,bg= 'turquoise',width = 8000,height= 8000)
frame2 = Frame(window,bg= 'turquoise',width = 8000,height= 8000,)
frame3 = Frame(window,bg= 'turquoise',width = 8000,height= 8000,)
frame4 = Frame(window,bg= 'turquoise',width = 8000,height= 8000,)
frame4_1 = Frame(window,bg= 'turquoise',width = 10000,height= 1000,)
frame4_2 = Frame(window,bg= 'turquoise',width = 10000,height= 1000,)
frame6 = Frame(window,bg= 'turquoise',width = 8000,height= 8000,)
frame7 = Frame(window,bg= 'turquoise',width = 8000,height= 8000,)
frame8 = Frame(window,bg= 'turquoise',width = 8000,height= 8000,)
frame9 = Frame(window,bg= 'turquoise',width = 8000,height= 8000,)
frame10 = Frame(window,bg= 'turquoise',width = 8000,height= 8000,)
frame11= Frame(window,bg= 'turquoise',width = 8000,height= 8000,)






for frame in (frame5,frame1,frame2,frame3,frame4,frame4_1,frame4_2,frame6,frame7,frame8,frame9,frame10,frame11):
    frame.grid(row =0 ,column=0,sticky = 'news')


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas, height=10)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")



#------------------frame5 start-------------------------#


labelt=Label(frame5,text="DIAZ BUSINESS DEVELOPER\n YOUR EVER SOLUTION IN BUSINESS\n BRINGS TO YOU BUSINESS SOLUTIONS\n HAVE A CHANCE TO BE PART OF THE BLESSED FEW WHO USE",font=('times new roman', 20 ,'bold',))
labelt.place(x=400,y=100)
buton1=Button(frame5,text="WEBSITE",bg='red',fg='white',width='10',font=("calbri 15 bold"),command = lambda:handle())
buton1.place(x=30,y=10)
buton1=Button(frame5,text="SHARE YOUR NEED",bg='red',fg='white',width='17',font=("calbri 15 bold"),command = lambda:handle())
buton1.place(x=180,y=10)
buton1=Button(frame5,text="PRICE CALCULATOR",bg='red',fg='white',width='20',font=("calbri 15 bold"),command = lambda:handle(frame6))
buton1.place(x=410,y=10)
buton1=Button(frame5,text="PERFORMANCE RECORDS",bg='red',fg='white',width='25',font=("calbri 15 bold"),command = lambda:handle(frame7))
buton1.place(x=680,y=10)
buton1=Button(frame5,text="BUSINESS RECORDS",bg='red',fg='white',width='25',font=("calbri 15 bold"),command = lambda:handle(frame1))
buton1.place(x=1000,y=10)

#------------------frame5 end-------------------------#

#------------------frame6 start-------------------------#


    
    
    
labelx=Label(frame6, text="PRICE CALCULATOR ACTS AS YOUR BLOCKER TO HELP EASILY DETERMINE THE APPROPRIATE PRICE AT WHICH YOU\n\n CAN SELL YOUR ANIMAL OR POULTRY. \n\n DIAZ PRICE CALCULATOR, THE ONLY WAY TO ESCAPE CHEATERS", font=('times new roman', 20 ,'bold'), fg="blue", bg="yellow")
labelx.place(x=20, y=10)


def show_entry_fields():
    ans.config(text=str((int(e1.get()))*(int(e2.get()))))

ans = tk.Label(frame6, text="0")
ans.place(x=300,y=500)

labelx=Label(frame6, text="ENTER THE ANIMAL'S WEIGHT HERE", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=10, y=270)
e1 = ttk.Entry(frame6, width="15", font=('times new roman', 20 ,'bold'))
e1.place(x=700, y=270)
labelx=Label(frame6, text="ENTER THE PRICE OF 1KG OF ITS MEAT", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=10, y=350)
e2 = ttk.Entry(frame6, width="15", font=('times new roman', 20 ,'bold'))
e2.place(x=700, y=350)
labelx=Label(frame6, text="CLICK THE PRICE BUTTON BELOW TO DETERMINE YOUR ANIMAL'S PRICE", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=200, y=220)
buttonx=Button(frame6, text="PRICE", font=('times new roman', 18 ,'bold'), fg="orange", bg="black",command="show_entry_fields")
buttonx.place(x=1000, y=350,)
buton1=Button(frame6,text="BACK",bg='red',fg='white',width='5',font=("calbri 15 bold"),command = lambda:handle(frame5))
buton1.place(x=0,y=400)






#------------------frame6 end-------------------------#

#------------------frame7 start-------------------------#

buton1=Button(frame7,text="BACK",bg='red',fg='white',width='5',font=("calbri 15 bold"),command = lambda:handle(frame5))
buton1.place(x=0,y=5)

labelx=Label(frame7, text="REGULARLY RECORD YOUR DAILY EARNINGS AND EXPENDITURE HERE \n\nTO TRACK YOUR FARMS' OR BUSINESS' PERFORMANCE", font=('times new roman', 20 ,'bold'), fg="blue", bg="yellow")
labelx.place(x=250,y=10)
labelx=Label(frame7, text="CHOOSE THE MONTH OF THE YEAR BELOW", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=200, y=150)
#mlabel6=Label(frame7,text='MONTH',width=18,height=1,bg="light blue",fg="black",font=("Calibri light",15))
#mlabel6.place(x=30,y=200)
#list1=['JANUARY','FEBRUARY','MARCH','APRIL',"MAY",'JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER'];
#drop=OptionMenu(frame7,MONTH,*list1)
#drop.config(width=15)
#MONTH.set('Choose a Month')
#drop.place(x=300,y=200)
labelx=Label(frame7, text="DATE", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=300)
labelx=Label(frame7, text="EARNINGS", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=250, y=300)
labelx=Label(frame7, text="EXPENDITURE", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=600, y=300)
labelx=Label(frame7, text="PROFITS", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=900, y=300)



#----------------------------------------------------#
labelx=Label(frame7, text="1ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=350)
labelx=Label(frame7, text="2ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=400)
labelx=Label(frame7, text="3ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=450)
labelx=Label(frame7, text="4ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=500)
labelx=Label(frame7, text="5ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=550)
labelx=Label(frame7, text="6ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=600)
labelx=Label(frame7, text="7ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=650)
labelx=Label(frame7, text="8ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=700)
labelx=Label(frame7, text="9ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=750)
labelx=Label(frame7, text="10ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=800)
labelx=Label(frame7, text="11ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=850)
labelx=Label(frame7, text="12ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=900)
labelx=Label(frame7, text="13ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=950)
labelx=Label(frame7, text="14ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1000)
labelx=Label(frame7, text="15ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1050)
labelx=Label(frame7, text="16ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1100)
labelx=Label(frame7, text="17ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1150)
labelx=Label(frame7, text="18ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1200)
labelx=Label(frame7, text="19ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1250)
labelx=Label(frame7, text="20ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1300)
labelx=Label(frame7, text="21ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1350)
labelx=Label(frame7, text="22ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1400)
labelx=Label(frame7, text="23ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1450)
labelx=Label(frame7, text="24ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1500)
labelx=Label(frame7, text="25ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1550)
labelx=Label(frame7, text="26ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1600)
labelx=Label(frame7, text="27ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1650)
labelx=Label(frame7, text="28ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1700)
labelx=Label(frame7, text="29ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1750)
labelx=Label(frame7, text="30ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1800)
labelx=Label(frame7, text="31ST", font=('times new roman', 20 ,'bold'), fg="white", bg="black")
labelx.place(x=20, y=1850)
#---------------------------------------------------------------------#
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=350)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=400)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=450)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=500)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=550)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=600)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=650)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=700)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=750)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=800)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=850)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=900)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=950)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1000)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1050)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1100)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1150)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1200)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1250)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1300)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1350)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1400)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1450)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1500)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1550)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1600)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1130)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1160)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1190)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1220)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=250, y=1250)
#------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------#
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=350)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=400)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=450)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=500)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=550)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=600)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=650)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=700)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=750)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=800)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=850)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=900)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=950)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1000)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1050)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1100)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1150)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1200)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1250)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1300)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1350)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1400)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1450)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1500)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1550)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1600)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1130)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1160)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1190)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1220)
labele = ttk.Entry(frame7, width="15", font=('times new roman', 20 ,'bold'))
labele.place(x=600, y=1250)


##
##frame = ScrollableFrame(window)
##
##frame.pack()





#-----------------------------------------------------------------------------------------#




#------------------frame7 end-------------------------#
image3=PhotoImage(file="sp.PNG")
panel=Label(frame1,image=image3)
panel.place(x=30,y=10)
panel.image=image3
label1=Label(frame1,text="KIRAMA SUPERMARKET  ",font=('impact', 40, 'bold'))
label1.place(x=400,y=70)
label2=Label(frame1,text="Welcome to KIRAMA\n SUPERMARKET MANAGEMENT SYSTEM\n \nThe system that will help\nyou to control the inaccurate needs analysis, \n how to identify, fully evaluate and priotize customer needs, \n on tracking what fully takesplace within the supermarket\n to identify the locations of the misplaced items in the supermarket\n and how to generate reports about the supermarket\n for high productivity.  ", width=60,bg="white",fg="blue",font=("Helvetica 15"))#label
label2.place(x=170,y=280)


#===============================================================================

buton1=Button(frame1,text="NEXT",bg='red',fg='white',width='5',font=("calbri 15 bold"),command = lambda:handle(frame2))
buton1.place(x=1300,y=750)

buton1=Button(frame1,text="BACK",bg='red',fg='white',width='5',font=("calbri 15 bold"),command = lambda:handle(frame5))
buton1.place(x=0,y=70)

frameH = Frame(frame1, height=65, width=1377, bg='#3C6739').place(x=0, y=0)
frameC = Frame(frame1, height=95, width=1377, bg='#3C6739').place(x=0, y=515)


framem = Frame(frame1,bg='yellow', width=1500, height=80) 
framem.place(x=1, y=600)
footer1 = Label(framem, text="Contact Us On:",  fg='darkblue',bg="yellow", font=('times new roman', 14))
footer1.place(x=50, y=5)
footer2 = Label(framem, text="+256 776 468 124", fg='black',bg="yellow", font=('times new roman', 11))
footer2.place(x=180, y=5)
footer3 = Label(framem, text="+256 757 254 271", fg='black',bg="yellow", font=('times new roman', 11))
footer3.place(x=180, y=25)

footer4 = Label(framem, text="E-mail:",  fg='darkblue',bg="yellow", font=('times new roman', 14))
footer4.place(x=380, y=5)

footer5 = Label(framem, text="info@Kiramasupmrkt.org.ug",  fg='black',bg="yellow", font=('times new roman', 11))
footer5.place(x=450, y=5)

footer6 =Label(framem,text="ptersont@gmail.com",fg='black',bg="yellow",font=('times new roman',11))
footer6.place(x=450, y=25)

footer7 = Label(framem, text="Media:",  fg='darkblue',bg="yellow", font=('times new roman', 14))
footer7.place(x=700, y=5)

footer8 = Label(framem, text="Facebook Peterson Diaz Junior",  fg='yellow',bg="yellow", font=('times new roman', 11))
footer8.place(x=780, y=5)
footer9 = Label(framem, text="YouTube",  fg='black',bg="yellow", font=('times new roman', 11))
footer9.place(x=780, y=25)
footer10 = Label(framem, text="Twitter  @petersondiaz",  fg='black',bg="yellow", font=('times new roman', 11))
footer10.place(x=880, y=5)
footer11 = Label(framem, text="Instagram @petersondiaz",  fg='black',bg="yellow", font=('times new roman', 11))
footer11.place(x=880, y=25)

footer = Label(framem, text="copy;2020 copyright. All rights Reserved",  fg='red',bg="yellow",
                    font=('times new roman', 16))
footer.place(x=350, y=50)
        
#buton2=Button(frame1,text="NEXT",bg='green',fg='white',width='5',font=("calbri 18 bold"),command = lambda:handle(frame2))
#buton2.place(x=200,y=600)



window.title('KIRAMA  SUPERMARKET SYSTEM')
window.wm_iconbitmap('favicon.ico')


IconTeacherButton = PhotoImage(file="TeacherIcon.gif")


#Label1 = Label(frame2, image=background).place(x=30, y=0)
#Label2 = Label(frame2, image=image).place(x=200, y=300, anchor='center', height=450, width=920)
#Label3 = Label(frame2, image=image).place(x=800, y=300, anchor='center', height=450, width=920)


TeacherButton = Button( frame2, image= IconTeacherButton, text='Teacher', width=200, height=235,
                             bg='#3C6739',
                             ).place(x=300, y=200, anchor='center')
StudentButton = Button(frame2, image= IconTeacherButton, text='Teacher', width=200, height=235,
                             bg='#3C6739',
                             ).place(x=920, y=200, anchor='center')

#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD= StringVar()



#==============================LABELS=========================================
frameH = Frame(frame2, height=50, width=1377, bg='#3C6739').place(x=0, y=0)
frameC = Frame(frame2, height=80, width=1377, bg='#3C6739').place(x=0, y=550)
lbl_title = Label(frame2, text = "LOGIN TO HAVE ACCESS", bg="white", font=('impact', 30, 'bold'))
lbl_title.place(x=420,y=20)



lbl1_title=Label(frame2, text = "ADMINISTRATOR", bg="yellow", font=('times new roman', 15))
lbl1_title.place(x=210,y=320)

lbl_username = Label(frame2, text = "Admin ID:", bg="yellow", font=('times new roman', 15))
lbl_username.place(x=100,y=370)

lbl_password = Label(frame2, text = "Password:", bg="yellow", font=('times new roman', 15))
lbl_password.place(x=100,y=420)
 
#==============================ENTRY WIDGETS==================================
username = ttk.Entry(frame2, textvariable=USERNAME,width=25 ,font=('times new roman', 15))
username.place(x=300,y=370)

password = ttk.Entry(frame2, textvariable=PASSWORD,width=25, show="*", font=('times new roman', 15))
password.place(x=300,y=420)


def Database():
    
    #cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        con.commit()



def Login(event=None):
    global un, pwd, WinStat,Home
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        messagebox.showinfo("ERROR", "Mendatory Field is empty")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (username.get(), password.get()))
    if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
    else:
            messagebox.showinfo("ERROR", "Invalid Username or Password")
            USERNAME.set("")
            PASSWORD.set("")
            
    #cursor.close()
    #con.close()
    
btn_login1 = Button(frame2, text="Login", width=20, command=Login,bg='#3C6739')
btn_login1.place(x=300, y=500)
button2=Button(frame2,text='BACK',font=('calbri 15 bold'),bg='red',fg='white',width='10',command=lambda:handle(frame1))
button2.place(x=0,y=0)

framem = Frame(frame2,bg='yellow', width=1500, height=80) 
framem.place(x=1, y=600)
footer1 = Label(framem, text="Contact Us On:",  fg='darkblue',bg="yellow", font=('times new roman', 14))
footer1.place(x=50, y=5)
footer2 = Label(framem, text="+256 776 468 124", fg='black',bg="yellow", font=('times new roman', 11))
footer2.place(x=180, y=5)
footer3 = Label(framem, text="+256 757 254 271", fg='black',bg="yellow", font=('times new roman', 11))
footer3.place(x=180, y=25)

footer4 = Label(framem, text="E-mail:",  fg='darkblue',bg="yellow", font=('times new roman', 14))
footer4.place(x=380, y=5)

footer5 = Label(framem, text="info@kiramasupmrkt.org.ug",  fg='black',bg="yellow", font=('times new roman', 11))
footer5.place(x=450, y=5)

footer6 =Label(framem,text="ptersont@gmail.com",fg='black',bg="yellow",font=('times new roman',11))
footer6.place(x=450, y=25)

footer7 = Label(framem, text="Media:",  fg='darkblue',bg="yellow", font=('times new roman', 14))
footer7.place(x=700, y=5)

footer8 = Label(framem, text="Facebook Peterson Diaz Junior",  fg='yellow',bg="yellow", font=('times new roman', 11))
footer8.place(x=780, y=5)
footer9 = Label(framem, text="YouTube Kirama Super Market",  fg='black',bg="yellow", font=('times new roman', 11))
footer9.place(x=780, y=25)
footer10 = Label(framem, text="Twitter  @petersondiazjunior",  fg='black',bg="yellow", font=('times new roman', 11))
footer10.place(x=880, y=5)
footer11 = Label(framem, text="Instagram @petersondiazjunior",  fg='black',bg="yellow", font=('times new roman', 11))
footer11.place(x=880, y=25)

footer = Label(framem, text="copy;2020 copyright. All rights Reserved",  fg='red',bg="yellow",
                    font=('times new roman', 16))
footer.place(x=350, y=50)

login=sqlite3.connect("grocery.sqlite")
l=login.cursor()
WinStat = ''


def stock():
    
    #Home.destroy()
    
    login.close()
    
    import stockdetails
    a = stockdetails.stock()
    
    HomeWindow()
def dailyincome():
    
    #Home.destroy()
    
    login.close()
    
    import billingdetails
    a = billingdetails.dailyincome()
    
    HomeWindow()    
    
def billingitems():
    
    #Home.destroy()
    
    login.close()
    
    import billingdetails
    a = billingdetails.billingitems()
    
    HomeWindow()
    
def delstock():
    
    #Home.destroy()
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    login.close()
    
    import stockdetails
    a = stockdetails.deletestock()
    
    HomeWindow()
    
def updatestock():
    
    #Home.destroy()
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    login.close()
    
    import stockdetails
    a = stockdetails.updatestock()
    
    HomeWindow()
    
def expirycheck():
    
    #Home.destroy()
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    login.close()
    
    import expirycheck
    a = expirycheck.expiry()
    
    HomeWindow()
def TellerAccount():
    
    #Home.destroy()
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    login.close()
    
    import teller
    a = teller.TellerAccount()
    
    HomeWindow()


#def HomeWindow():

def HomeWindow():
    global Home, WinStat
    WinStat='Home'
    window.withdraw()
    Home = Toplevel()
    Home.wm_iconbitmap('favicon.ico')

    acc=0 
    Home.geometry('10000x9500')

    Home.title("KIRAMA SUPERMARKET MANAGEMENT SYSTEM)")
    Home.config(bg="turquoise")

#=========================================================================================================
    menu_bar = Menu(Home)
    stock_menu = Menu(menu_bar,tearoff=0)
    expiry_menu = Menu(menu_bar,tearoff=25)
    billing_menu = Menu(menu_bar,tearoff=50)
    teller_menu = Menu(menu_bar,tearoff=75)
    '''Stock Maintainance'''
    stock_menu.add_command(label="Add Items", command=stock)
    stock_menu.add_command(label="Delete Items", command=delstock)
    stock_menu.add_command(label="Update Items", command=updatestock)
    '''Expiry Check'''
    expiry_menu.add_command(label="Check Expiry", command=expirycheck)
    '''Billing'''
    billing_menu.add_command(label="Billing", command=billingitems)
    billing_menu.add_command(label="Check Today's Income", command=dailyincome)

    '''teller'''
    teller_menu.add_command(label="Add Tellers", command=TellerAccount)
    
    
    menu_bar.add_cascade(label="Stock Maintainance", menu=stock_menu)
    menu_bar.add_cascade(label="Expiry", menu=expiry_menu)
    menu_bar.add_cascade(label="Billing", menu=billing_menu)
    menu_bar.add_cascade(label="teller details",menu=teller_menu)
    menu_bar.add_cascade(label="Logout",command=Back)
    Home.config(menu=menu_bar)

    img2 = PhotoImage(file = "gd.png")
    panel1 = Label(Home,image = img2,width = 750,height=500)
    panel1.place(x=600,y=70)
    panel1.image = img2

    img3 = PhotoImage(file = "gd.png")
    panel1 = Label(Home,image = img3,width = 820,height=500)
    panel1.place(x=0,y=70)
    panel1.image = img3

    frameH = Frame(Home, height=65, width=1377, bg='#3C6739').place(x=0, y=0)
    frameC = Frame(Home, height=95, width=1377, bg='#3C6739').place(x=0, y=500)

    framem = Frame(Home,bg='yellow', width=1500, height=80) 
    framem.place(x=1, y=600)
    footer1 = Label(framem, text="Contact Us On:",  fg='darkblue',bg="yellow", font=('times new roman', 14))
    footer1.place(x=50, y=5)
    footer2 = Label(framem, text="+256 776 468 124", fg='black',bg="yellow", font=('times new roman', 11))
    footer2.place(x=180, y=5)
    footer3 = Label(framem, text="+256 757 254 271", fg='black',bg="yellow", font=('times new roman', 11))
    footer3.place(x=180, y=25)

    footer4 = Label(framem, text="E-mail:",  fg='darkblue',bg="yellow", font=('times new roman', 14))
    footer4.place(x=380, y=5)

    footer5 = Label(framem, text="info@kiramasupmrkt.org.ug",  fg='black',bg="yellow", font=('times new roman', 11))
    footer5.place(x=450, y=5)

    footer6 =Label(framem,text="ptersont@gmail.com",fg='black',bg="yellow",font=('times new roman',11))
    footer6.place(x=450, y=25)

    footer7 = Label(framem, text="Media:",  fg='darkblue',bg="yellow", font=('times new roman', 14))
    footer7.place(x=700, y=5)

    footer8 = Label(framem, text="Facebook Peterson Diaz Junior",  fg='yellow',bg="yellow", font=('times new roman', 11))
    footer8.place(x=780, y=5)
    footer9 = Label(framem, text="YouTube Kirama Super Market",  fg='black',bg="yellow", font=('times new roman', 11))
    footer9.place(x=780, y=25)
    footer10 = Label(framem, text="Twitter  @petersondiazjunior",  fg='black',bg="yellow", font=('times new roman', 11))
    footer10.place(x=880, y=5)
    footer11 = Label(framem, text="Instagram @petersondiazjunior",  fg='black',bg="yellow", font=('times new roman', 11))
    footer11.place(x=880, y=25)

    footer = Label(framem, text="copy;2020 copyright. All rights Reserved",  fg='red',bg="yellow",
                        font=('times new roman', 16))
    footer.place(x=350, y=50)

    Home.mainloop()
       


#==========================================================================================
    

#####==============================================trial==================================================

#window.config(menu=menubar)
    
#=======================================VARIABLES=====================================
USERNAME1 = StringVar()
PASSWORD1 = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()


def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(window)
    LoginFrame.place(x=800,y=50)
    lbl2_title=Label(frame2, text = "TELLER", bg="yellow", font=('times new roman', 15))
    lbl2_title.place(x=900,y=320)
    
    lbl_username = Label(frame2, text = "Username:", bg="yellow", font=('times new roman', 15))
    lbl_username.place(x=700,y=370)

    lbl_password = Label(frame2, text = "Password:", bg="yellow", font=('times new roman', 15))
    lbl_password.place(x=700,y=420)
    
    lbl_result1 = Label(frame2, text="", font=('arial', 18))
    lbl_result1.place(x=700,y=250)
    
    username = ttk.Entry(frame2, textvariable=USERNAME1,width=25 ,font=('times new roman', 15))
    username.place(x=800,y=370)

    password = ttk.Entry(frame2, textvariable=PASSWORD1,width=25, show="*", font=('times new roman', 15))
    password.place(x=800,y=420)
    
    btn_login = Button(frame2, text="Login", font=('arial', 10), command=Login,bg='#3C6739')
    btn_login.place(x=900,y=500)
    
    lbl_register = Label(frame2, text="Register", font=('arial', 12),bg='#3C6739')
    lbl_register.place(x=700,y=500)
    lbl_register.bind('<Button-1>', ToggleToRegister)
 
def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(window)
    RegisterFrame.place(x=700, y=300)
    lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=5, columnspan=2)
    username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME1, width=15)
    username.grid(row=1, column=1)
    password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD1, width=15, show="*")
    password.grid(row=2, column=1)
    firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
    btn_login.grid(row=6, columnspan=2, pady=20)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToggleToLogin)
 
 
#========================================MENUBAR WIDGETS==================================
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
window.config(menu=menubar)

#def Exit():
    #result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    #if result == 'yes':
        #root.destroy()
        #exit()
 
def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()
 
def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()
 
def Register():
    
    if USERNAME1.get == "" or PASSWORD1.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "":
        lbl_result2.config(text="Please complete the required fields!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME1.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)", (str(USERNAME1.get()), str(PASSWORD1.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
            con.commit()
            USERNAME1.set("")
            PASSWORD1.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
            lbl_result2.config(text="Successfully Created!", fg="black")
        #cursor.close()
        #conn.close()
def Login():
    
    global un, pwd
    if USERNAME1.get == "" or PASSWORD1.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?", (USERNAME1.get(), PASSWORD1.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="You Successfully Login", fg="blue")
            HomeWindow1()
            USERNAME1.set("")
            PASSWORD1.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")
LoginForm()

login=sqlite3.connect("grocery.sqlite")
l=login.cursor()
WinStat = ''


def stock():
    
    #Home.destroy()
    
    login.close()
    
    import stockdetails
    a = stockdetails.stock()
    
    HomeWindow1()
def dailyincome():
    
    #Home.destroy()
    
    login.close()
    
    import billingdetails
    a = billingdetails.dailyincome()
    
    HomeWindow1()    
    
def billingitems():
    
    #Home.destroy()
    
    login.close()
    
    import billingdetails
    a = billingdetails.billingitems()
    
    HomeWindow1()
    
def delstock():
    
    #Home.destroy()
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    login.close()
    
    import stockdetails
    a = stockdetails.deletestock()
    
    HomeWindow1()
    
def updatestock():
    
   # Home.destroy()
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    login.close()
    
    import stockdetails
    a = stockdetails.updatestock()
    
    HomeWindow1()
    
def expirycheck():
    
    #Home.destroy()
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    login.close()
    
    import expirycheck
    a = expirycheck.expiry()
    
    HomeWindow1()
def customerAccount():
    
    #Home.destroy()
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    login.close()
    
    import customer
    a = customer.customerAccount()
    
    HomeWindow1()

def HomeWindow1():
    global Home, WinStat
    WinStat='Home'
    window.withdraw()
    Home = Toplevel()
    Home.wm_iconbitmap('favicon.ico')

    acc=0 
    Home.geometry('10000x9500')

    Home.title("KIRAMA SUPERMARKET MANAGEMENT SYSTEM")
    Home.config(bg="turquoise")

#=========================================================================================================
    menu_bar = Menu(Home)
    #stock_menu = Menu(menu_bar,tearoff=0)
    expiry_menu = Menu(menu_bar,tearoff=0)
    billing_menu = Menu(menu_bar,tearoff=0)
    customer_menu = Menu(menu_bar,tearoff=0)
    '''Stock Maintainance'''
    #stock_menu.add_command(label="Add Items", command=stock)
    #stock_menu.add_command(label="Delete Items", command=delstock)
    #stock_menu.add_command(label="Update Items", command=updatestock)
    '''Expiry Check'''
    expiry_menu.add_command(label="Check Expiry", command=expirycheck)
    '''Billing'''
    billing_menu.add_command(label="Billing", command=billingitems)
    #billing_menu.add_command(label="Check Today's Income", command=dailyincome)

    '''customer'''
    customer_menu.add_command(label="Add Customers", command=customerAccount)
    
    
   # menu_bar.add_cascade(label="Stock Maintainance", menu=stock_menu)
    menu_bar.add_cascade(label="Expiry", menu=expiry_menu)
    menu_bar.add_cascade(label="Billing", menu=billing_menu)
    menu_bar.add_cascade(label="customer details",menu=customer_menu)
    menu_bar.add_cascade(label="Logout",command=Back)
    Home.config(menu=menu_bar)

    img2 = PhotoImage(file = "gd.png")
    panel1 = Label(Home,image = img2,width = 750,height=500)
    panel1.place(x=600,y=70)
    panel1.image = img2

    img3 = PhotoImage(file = "gd.png")
    panel1 = Label(Home,image = img3,width = 820,height=500)
    panel1.place(x=0,y=70)
    panel1.image = img3

    frameH = Frame(Home, height=65, width=1377, bg='#3C6739').place(x=0, y=0)
    frameC = Frame(Home, height=95, width=1377, bg='#3C6739').place(x=0, y=500)

    

    framem = Frame(Home,bg='yellow', width=1500, height=80) 
    framem.place(x=1, y=600)
    footer1 = Label(framem, text="Contact Us On:",  fg='darkblue',bg="yellow", font=('times new roman', 14))
    footer1.place(x=50, y=5)
    footer2 = Label(framem, text="+256 776 468 124", fg='black',bg="yellow", font=('times new roman', 11))
    footer2.place(x=180, y=5)
    footer3 = Label(framem, text="+256 757 254 271", fg='black',bg="yellow", font=('times new roman', 11))
    footer3.place(x=180, y=25)

    footer4 = Label(framem, text="E-mail:",  fg='darkblue',bg="yellow", font=('times new roman', 14))
    footer4.place(x=380, y=5)

    footer5 = Label(framem, text="info@kiramasupmrkt.org.ug",  fg='black',bg="yellow", font=('times new roman', 11))
    footer5.place(x=450, y=5)

    footer6 =Label(framem,text="ptersont@gmail.com",fg='black',bg="yellow",font=('times new roman',11))
    footer6.place(x=450, y=25)

    footer7 = Label(framem, text="Media:",  fg='darkblue',bg="yellow", font=('times new roman', 14))
    footer7.place(x=700, y=5)

    footer8 = Label(framem, text="Facebook Peterson Diaz Junior",  fg='yellow',bg="yellow", font=('times new roman', 11))
    footer8.place(x=780, y=5)
    footer9 = Label(framem, text="YouTube Kirama Super Market",  fg='black',bg="yellow", font=('times new roman', 11))
    footer9.place(x=780, y=25)
    footer10 = Label(framem, text="Twitter  @petersondiazjunior",  fg='black',bg="yellow", font=('times new roman', 11))
    footer10.place(x=880, y=5)
    footer11 = Label(framem, text="Instagram @petersondiazjunior",  fg='black',bg="yellow", font=('times new roman', 11))
    footer11.place(x=880, y=25)

    footer = Label(framem, text="copy;2020 copyright. All rights Reserved",  fg='red',bg="yellow",
                        font=('times new roman', 16))
    footer.place(x=350, y=50)

    Home.mainloop()

    

    
    
    
    
#again()


       
def Homeys():
    #Home.destroy()
    #window.deiconify()
    frame4 = Tk()
    frame4.title("KIRAMA SUPERMARKET MANAGEMENT SYSTEM")

def Homey():
    frame3 = Tk()
    frame3.title("KIRAMA SUPERMARKET MANAGEMENT SYSTEM")

def Back():
    Home.destroy()
    window.deiconify()

 


handle(frame5)

window.mainloop()

