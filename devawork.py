from tkinter import *
import pickle
import csv
import os
from tkinter import messagebox
window=Tk()
window.attributes('-fullscreen',True)
window.title("MRF.com")
window.configure(bg ="#00ffff")
l1=Label(window,text="Welcome to Move Run Fly",font=("Arial Bold",45))
l1.configure(fg="Black",bg="#00ffff")
l1.place(relx=0.5, rely=0.12, anchor="center")
userlogin=[["Srijith","12f214"],["Devadarshan","12f207"],["Syed","12f242"],["1","1"]]
fromlist=["monday","tuesday","wednesday","thursday","friday"]

def Admin_id():
    print("nothing inside")
def user_login():
    def useridpassword():
        c=0
        num1=username.get()
        num2=password.get()
        for i in range(len(userlogin)):
            if num1 in userlogin[i][0] and num2 in userlogin[i][1]:
                c+=1
        if c==1:
            user_portal()
            userwindow.destroy()
        else: 
            messagebox.showwarning("Attention","Invalid Username or Password!")
            userwindow.destroy()
        
    userwindow=Tk()
    userwindow.title("Admin login")
    userwindow.attributes('-fullscreen',True) 
    userwindow.configure(bg ="light Green")
    lab1=Label(userwindow,text="Enter required credentials to enter the portal",font=("Arial",20))
    lab1.configure(fg="White",bg="light Green")
    lab1.place(relx=0.55,rely=0.2,anchor="center")
    lab2=Label(userwindow,text="Username")
    lab2.place(relx=0.5,rely=0.4,anchor="center")
    username=Entry(userwindow)
    username.place(relx=0.6,rely=0.4,anchor="center")
    lab3=Label(userwindow,text="Password")
    lab3.place(relx=0.5,rely=0.45,anchor="center")
    password=Entry(userwindow,show="*")
    password.place(relx=0.6,rely=0.45,anchor="center")
    bu1=Button(userwindow,text="Submit",fg="Blue",bg="yellow",command=useridpassword)
    bu1.place(relx=0.55,rely=0.5,anchor="center")
    bu2=Button(userwindow,text="Back",fg="Blue",bg="yellow",command=userwindow.destroy)
    bu2.place(relx=0.65,rely=0.5,anchor="center")
def Guest():
    print("nothing")
def Exit():
     messagebox.showinfo("Quit","Thank you")
     window.destroy()
def Help():
    print("i dont need your help")
def ITSHOW():
    print("nothing to show")
def About_us():
    print("basically we are busy")
def Railways_booking(*args):
    def search_train(*args):
        class Table: 
            def __init__(self,strain):
                c=0
                for i in range(total_rows):
                    if c%2==0:
                        for j in range(total_columns):
                            self.e = Entry(strain, width=20, fg='blue', 
                                       font=('Arial',16,'bold'))                   
                            self.e.grid(row=i+1, column=j+1)
                            self.e.insert(END, slt[i][j])
                    c+=1
                    
        f=open("Railways.csv","r")
        robj=csv.reader(f,delimiter=",")
        slt=list(robj)
        total_rows = len(slt) 
        total_columns = len(slt[0])
        f.close()
        strain=Tk()
        strain.attributes('-fullscreen',True)
        strain.title("search train")
        strain.configure(bg ="light Green")
        s1=Label(strain,text="Available Trains",font=("Arial Bold",30))
        s1.configure(fg="blue",bg="light Green")
        s1.place(relx=0.1, rely=0.07, anchor="center")
        t = Table(strain)
        strain.mainloop()
            
    railbook=Tk()
    railbook.title("rail portal")
    railbook.attributes('-fullscreen',True)  
    railbook.configure(bg ="light Blue")
    l1=Label(railbook,text="railway booking",font=("Arial Bold",45))
    l1.configure(fg="yellow",bg="light Blue")
    l1.place(relx=0.5, rely=0.07, anchor="center")
    From=Label(railbook,text="ORIGIN",fg="Blue",bg="yellow")
    From.place(relx=0.07,rely=0.4,anchor="center")
    vari=StringVar(railbook)
    vari1=StringVar(railbook)
    vari2=StringVar(railbook)
    vari3=StringVar(railbook)
    drop1=OptionMenu(railbook,vari,"monday","tuesday","wednesday","thursday","friday")
    drop1.place(relx=0.20,rely=0.4,anchor="center")
    vari.set("monday")
    To=Label(railbook,text="DESTINATION",fg="Blue",bg="yellow")
    To.place(relx=0.07,rely=0.5,anchor="center")
    drop2=OptionMenu(railbook,vari1,"monday","tuesday","wednesday","thursday","friday")
    drop2.place(relx=0.20,rely=0.5,anchor="center")
    vari1.set("tuesday")
    date=Label(railbook,text="DATE",fg="Blue",bg="yellow")
    date.place(relx=0.07,rely=0.6)
    e1=Entry(railbook,bg="yellow",fg="white")
    e1.place(relx=0.18,rely=0.6)
    nop=Label(railbook,text="NO OF PASSENGERS",fg="Blue",bg="yellow")
    nop.place(relx=0.07,rely=0.7)
    e2=Entry(railbook,bg="yellow",fg="white")
    e2.place(relx=0.18,rely=0.7)
    quo=Label(railbook,text="QUOTA",fg="Blue",bg="yellow")
    quo.place(relx=0.11,rely=0.8)
    drop3=OptionMenu(railbook,vari3,"General","Senior Citizen","divyaang")
    drop3.place(relx=0.20,rely=0.8,anchor="center")         
    bu4=Button(railbook,text="Exit Railway Booking",fg="Blue",bg="yellow",command=railbook.destroy)
    bu4.place(relx=0.1,rely=0.9,anchor="c")
    r1=Label(railbook,text=":",fg="yellow",bg="light blue",font=("Arial Bold",20))
    r1.place(relx=0.15,rely=0.7)
    r2=Label(railbook,text=":",fg="yellow",bg="light blue",font=("Arial Bold",20))
    r2.place(relx=0.15,rely=0.6)
    r3=Label(railbook,text=":",fg="yellow",bg="light blue",font=("Arial Bold",20))
    r3.place(relx=0.15,rely=0.5)
    r4=Label(railbook,text=":",fg="yellow",bg="light blue",font=("Arial Bold",20))
    r4.place(relx=0.15,rely=0.4)
    r5=Label(railbook,text=":",fg="yellow",bg="light blue",font=("Arial Bold",20))
    r5.place(relx=0.15,rely=0.8)
    bu5=Button(railbook,text="Search Train",fg="Blue",bg="yellow",command=search_train)
    bu5.place(relx=0.9,rely=0.9,anchor="c")
def Roadways_booking():
    return
    
def Airways_booking():
    return
    
def user_portal():
    userportal=Tk()
    userportal.title("user portal")
    userportal.attributes('-fullscreen',True)  
    userportal.configure(bg ="light Blue")
    l1=Label(userportal,text="User Portal",font=("Arial Bold",45))
    l1.configure(fg="White",bg="Sky Blue")
    l1.place(relx=0.5, rely=0.07, anchor="center")
    bu1=Button(userportal,text="BOOK A TRAIN",fg="Blue",bg="yellow",command=Railways_booking)
    bu1.place(relx = 0.5, rely = 0.4, anchor = 'c')
    bu2=Button(userportal,text="BOOK A BUS",fg="Blue",bg="yellow",command=Roadways_booking)
    bu2.place(relx = 0.5, rely = 0.55, anchor = 'c')
    bu3=Button(userportal,text="BOOK A FLIGHT",fg="Blue",bg="yellow",command=Airways_booking)
    bu3.place(relx = 0.5, rely = 0.7, anchor = 'c')
    bu4=Button(userportal,text="Exit User Portal",fg="Blue",bg="yellow",command=userportal.destroy)
    bu4.place(relx = 0.5, rely = 0.9, anchor = 'c')

    
bt=Button(window,text="Admin Login",fg="Blue",bg="yellow",command=Admin_id)
bt.place(relx = 0.5, rely = 0.4, anchor = 'c')

bt2=Button(window,text=" User Login",fg="Blue",bg="yellow",command=user_login)
bt2.place(relx = 0.5, rely = 0.5, anchor = 'c')
bt3=Button(window,text="Guest Login",fg="Blue",bg="yellow",command=Guest)
bt3.place(relx = 0.5, rely = 0.6, anchor = 'c')
bt4=Button(window,text="   Exit    ",fg="Blue",bg="yellow",command=Exit)
bt4.place(relx = 0.5, rely = 0.7, anchor = 'c')
bt5=Button(window,text="Help",fg="Blue",bg="yellow",command=Help)
bt5.place(relx=0.1,rely=0.9,anchor="c")
bt6=Button(window,text="Know about Indian Transport",fg="Blue",bg="yellow",command=ITSHOW)
bt6.place(relx=0.5,rely=0.9,anchor="c")
bt7=Button(window,text="About us",fg="Blue",bg="yellow",command=About_us)
bt7.place(relx=0.9,rely=0.9,anchor="c")

window.mainloop()
