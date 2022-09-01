import tkinter as tk
import pickle
import os
import csv
from tkinter import *
from tkinter import messagebox
window=tk.Tk()
window.attributes('-fullscreen',True)
window.title("MRF.com")
window.configure(bg ="Light pink")
l1=Label(window,text="Welcome to Move Run Fly",font=("Arial Bold",45))
l1.configure(fg="Black",bg="Light Pink")
l1.place(relx=0.5, rely=0.12, anchor="center")
photo=tk.PhotoImage(file="project.png")
label=tk.Label(window,image=photo)
label.place(relx = 0.95,rely = 0.01, anchor ='center')
d=[["Railways","Train"],["Roadways","Bus"],["Airways","Flight"]]
adminku=[["Srijith","12f214"],["Devadarshan","12f207"],["Syed","12f242"],["1","1"]]
userlogin=[["Srijith","12f214"],["Devadarshan","12f207"],["Syed","12f242"],["1","1"]]
fromlist=["monday","tuesday","wednesday","thursday","friday"]
vai=[]
for i in range(1,32):
    vai.append(str(i))

def Print():
    print("Useless")

def cav():
    messagebox.showinfo("Note","Go to python module for Cancelling")
    fna=input("Enter which chart")
    fna+=".csv"
    f=open(fna,"r")
    robj=csv.reader(f,delimiter=",")
    r=list(robj)
    x=0
    for a in r:
        if x%2==0:
            a[6]="Cancelled"
        x+=1
    print(r)
    messagebox.showinfo("Success","All Scheduled Vehicles Cancelled")
    f.close()
    f=open(fna,"w")
    wobj=csv.writer(f,delimiter=",")
    m=0
    for b in r:
        if m%2==0:
            print(b)
            wobj.writerow(b)
        m+=1
    f.close()

def update_chart():
    messagebox.showinfo("Note","Go to python module for Updating")
    fna=input("Enter which chart")
    fnab=fna+".csv"
    f=open(fnab,"r")
    s=[]
    robj=csv.reader(f,delimiter=",")
    r=list(robj)
    for m in d:
        if m[0]==fna:
            j=m[1]  
    name=input("Enter name of the "+j+" which you want to update")
    x=0
    for a in r:
        if x%2==0 and a[1]!=name:
            s.append(a)
        elif x%2==0:
            v=[]
            print("Enter details to be updated")
            v.append(input("Enter "+j+" Number"))
            v.append(input("Enter "+j+" name"))
            v.append(input("From"))
            v.append(input("To"))
            v.append(input("Arrival date and Time"))
            v.append(input("Departure date and Time"))
            v.append(input("Enter Status"))
            s.append(v)
        x+=1
    f.close()
    print(s)
    f=open(fnab,"w")
    wobj=csv.writer(f,delimiter=",")
    for b in s:
        wobj.writerow(b)
    f.close()
       
def put_chart():
    messagebox.showinfo("Note","Go to python module for putting the chart ")
    fna=input("Enter which chart")
    fnab=fna+".csv"
    f=open(fnab,"w")
    wobj=csv.writer(f,delimiter=",")
    for m in d:
        if m[0]==fna:
            v=m[1]            
    while True:
        sno=input("Enter "+v+" number")
        name=input("Enter "+v+"name")
        fromu=input("From")
        to=input("To")
        arrival=input("Arrival date and Time")
        departure=input("Departure date and Time")
        status=input("Enter Status")
        wobj.writerow([sno,name,fromu,to,arrival,departure,status])
        f.flush()
        ch=input("Any more data")
        if ch not in "Yy":
            break
    f.close()
    

def show_chart():
    
    class Table: 
      
        def __init__(self,root):
            c=0
          
        # code for creating table 
            for i in range(total_rows):
                if c%2==0:
                    for j in range(total_columns):
                        self.e = Entry(root, width=15, fg='blue', 
                                       font=('Arial',16,'bold'))                   
                        self.e.grid(row=i+1, column=j+1)
                        self.e.insert(END, e[i][j])
                c+=1
  
# take the data


    messagebox.showinfo("Note","Go to python module for seeing the chart")
    fna=input("Enter which chart")
    q=fna+".csv"
    r=fna+"portal"
    f=open(q,"r")
    f.seek(0)
    robj=csv.reader(f,delimiter=",")
    e=list(robj)
   
# find total number of rows and 
# columns in list 
    total_rows = len(e) 
    total_columns = len(e[0])
    f.close()
    root = Tk()
    root.attributes('-fullscreen',True)
    root.title(fna+" chart")
    root.configure(bg ="Light pink")
    l1=Label(root,text=fna+" Chart",font=("Arial Bold",45))
    l1.configure(fg="Black",bg="Light Pink")
    l1.place(relx=0.5, rely=0.2, anchor="center")
    t = Table(root)
    root.mainloop()           


def Admin_creating_about_us_fn():
    f=open("About us.txt","w")
    s=' '
    print("Enter Data for About us option")
    while True:
        robj=input()
        s+=robj
        s+="\n"
        if robj.upper=="Exit":
            break
    f.write(s)

def add_a_Vehicle():
    messagebox.showinfo("note","go to python module for seeing the chart")
    fna=input("Enter which chart")
    q=fna+".csv"
    f=open(q,"a")
    w=0
    wobj=csv.writer(f,delimiter=",")
    for m in d:
        if m[0]==fna:
            v=m[1]  
    while True:
        sno=int(input("Enter "+v+" number"))
        name=input("Enter "+v+" name")
        fromu=input("From")
        to=input("To")
        arrival=input("Arrival date Time")
        departure=input("Departure date Time")
        status=input("Enter Status")
        wobj.writerow([sno,name,fromu,to,arrival,departure,status])
        f.flush()
        ch=input("Any more data")
        if ch not in "Yy":
            break
    f.close()
    
def cancel_a_Vehicle():
    def c_v_n():
        name=cvname.get()
        c,s=0,[]
        q=fna+".csv"
        f=open(q,"r")
        robj=csv.reader(f,delimiter=",")
        for h in robj:
            if c%2==0 and h[1]!=name:
                s.append(h)
            elif c%2==0:
               messagebox.showinfo("Sucess","Sucessfully cancelled the train")
            c+=1
        f.close()
        cv.destroy()
        j=open(q,"w")
        wobj=csv.writer(j,delimiter=",")
        for h in s:
            wobj.writerow(h)
        j.close()                        
    messagebox.showinfo("Note","Go to python module for Cancellation process")
    fna=input("Enter which chart")
    for m in d:
        if m[0]==fna:
            v=m[1]  
    cv=tk.Tk()
    cv.title("Cancel a "+v+" from "+fna+" Chart")
    cv.geometry('1000x1000+50+50')
    cv.configure(bg ="Red")
    ll=Label(cv,text="Enter the "+v+" Name",font=("Arial Bold",15))
    ll.configure(fg="White",bg="Red")
    ll.place(relx=0.2, rely=0.4, anchor="center")
    cvname=tk.Entry(cv)
    cvname.place(relx=0.5,rely=0.4, anchor="center")
    but1=tk.Button(cv,text="Confirm",fg="yellow",bg="Blue",command=c_v_n)
    but1.place(relx = 0.3, rely = 0.5, anchor = 'c')

def showpaslist():
    messagebox.showinfo("Note","Go to python module for seeing passenger list ")
    fna=input("Enter which chart")
    q=fna+".csv"
    f=open(q,"r")
    c=a=0
    robj=csv.reader(f,delimiter=",")
    for m in d:
        if m[0]==fna:
            v=m[1] 
    ding=input("Enter name of the",v)
    for h in robj:
        if c%2==0 and h[1]==ding:
            n=h[1]+".csv"
            q=open(n,delimiter=",")
            robj1=csv.reader(q,delimiter=",")
            s=0
            a+=1
            for k in robj1:
                if s%2==0:
                    for w in range(len(k)):
                        print(k[w],end=" ")
                s+=1
        c+=1
    if a==0:
         messagebox.showinfo("Kannna","Poda! aandavane enga pakkam irukaan")
        
def deladmin():
    def deladinput():
        g=0
        d=deladname.get()
        for i in range(len(adminku)):
            if d in adminku[i][0]:
                adminku.remove(adminku[i])
                messagebox.showinfo("Sucess","Admin Deleted Sucessfully")
                g+=1
                break
        if g==0:
            messagebox.showinfo("Error","Admin name not found")
    deladmin=tk.Tk()
    deladmin.title("Delete an Admin")
    deladmin.attributes('-fullscreen',True)
    deladmin.configure(bg ="Red")
    ll=Label(deladmin,text="Enter admin name to be deleted",font=("Arial Bold",15))
    ll.configure(fg="White",bg="Red")
    ll.place(relx=0.2, rely=0.4, anchor="center")
    deladname=tk.Entry(deladmin)
    deladname.place(relx=0.5,rely=0.4, anchor="center")
    but1=tk.Button(deladmin,text="Confirm",fg="yellow",bg="Blue",command=deladinput)
    but1.place(relx = 0.3, rely = 0.5, anchor = 'c')
    but2=tk.Button(deladmin,text="Back",fg="yellow",bg="Blue",command=deladmin.destroy)
    but2.place(relx = 0.4 ,rely = 0.5, anchor = 'c')
    
def addadmin():
    def addidpass():
        e1=[]
        user=addadname.get()
        passw=addadnamep.get()
        e1.append(user)
        e1.append(passw)
        adminku.append(e1)
        messagebox.showinfo("Sucess","Admin Added Sucessfully")       
    addadmin=tk.Tk()
    addadmin.title("Add an Admin")
    addadmin.attributes('-fullscreen',True)
    addadmin.configure(bg ="Red")
    l3=Label(addadmin,text="Enter the Required Credentials",font=("Arial Bold",20))
    l3.configure(fg="White",bg="Red")
    l3.place(relx=0.45,rely=0.2, anchor="center")
    ll=Label(addadmin,text="Enter admin name to be added",font=("Arial Bold",15))
    ll.configure(fg="White",bg="Red")
    ll.place(relx=0.2, rely=0.3, anchor="center")
    addadname=tk.Entry(addadmin)
    addadname.place(relx=0.5,rely=0.3, anchor="center")
    l2=Label(addadmin,text="Enter admin password to be added",font=("Arial Bold",15))
    l2.configure(fg="White",bg="Red")
    l2.place(relx=0.2, rely=0.4, anchor="center")
    addadnamep=tk.Entry(addadmin)
    addadnamep.place(relx=0.5,rely=0.4, anchor="center")
    but1=tk.Button(addadmin,text="Confirm",fg="yellow",bg="Blue",command=addidpass)
    but1.place(relx = 0.4 ,rely = 0.5, anchor = 'c')
    but2=tk.Button(addadmin,text="Back",fg="yellow",bg="Blue",command=addadmin.destroy)
    but2.place(relx = 0.5 ,rely = 0.5, anchor = 'c')
   
def Exit():
    messagebox.showinfo("Quit","Thank you")
    window.destroy()
    
def Guest():
    window1=tkinter.Tk()
    window1.title("MRF.com/Guest/choosing mode of transport")
    window1.geometry('100x100')
    window1.configure(bg ="Blue")
    from tkinter import Label
    l1=Label(window1,text="Choose you're mode of transport",font=("Arial Bold",25),anchor='c')
    l1.configure(fg="White",bg="Blue")
    l1.pack()
    gt=tkinter.Button(window1,text="Airways",fg="White",bg="Black",command= Airways)
    gt.place(relx = 0.5, rely = 0.4, anchor = 'c')
    gt1=tkinter.Button(window1,text="Railways",fg="White",bg="Black",command= Railways)
    gt1.place(relx = 0.5, rely = 0.5, anchor = 'c')
    gt2=tkinter.Button(window1,text="Roadways",fg="White",bg="Black",command= Roadways)
    gt2.place(relx = 0.5, rely = 0.6, anchor = 'c')    

def Railways_portal():
    Railwaysportal=tk.Tk()
    Railwaysportal.title("Railways portal")
    Railwaysportal.attributes('-fullscreen',True)
    Railwaysportal.configure(bg ="Sky Blue")
    l1=Label(Railwaysportal,text="Railways Portal",font=("Arial Bold",45))
    l1.configure(fg="White",bg="Sky Blue")
    l1.place(relx=0.5, rely=0.07, anchor="center")   
    bt1=tk.Button(Railwaysportal,text="Show scheduled train chart",fg="yellow",bg="Blue",command=show_chart)
    bt1.place(relx = 0.5, rely = 0.3, anchor = 'c')
    bt2=tk.Button(Railwaysportal,text="Add a train",fg="yellow",bg="Blue",command=add_a_Vehicle)
    bt2.place(relx = 0.5, rely = 0.4, anchor = 'c')
    bt3=tk.Button(Railwaysportal,text="Cancel a train",fg="yellow",bg="Blue",command=cancel_a_Vehicle)
    bt3.place(relx = 0.5, rely = 0.5, anchor = 'c')
    bt4=tk.Button(Railwaysportal,text="Update the chart",fg="yellow",bg="Blue",command=update_chart)
    bt4.place(relx = 0.5, rely = 0.6, anchor = 'c')
    bt5=tk.Button(Railwaysportal,text="Cancel all trains",fg="yellow",bg="Blue",command=cav)
    bt5.place(relx = 0.5, rely = 0.7, anchor = 'c')
    bt6=tk.Button(Railwaysportal, text="Put up the chart",fg="yellow",bg="Blue",command=put_chart)
    bt6.place(relx = 0.5, rely= 0.2 , anchor='c')
    bt7=tk.Button(Railwaysportal,text="Show passenger list",fg="yellow",bg="Blue",command=showpaslist)
    bt7.place(relx=0.5,rely=0.8,anchor="center")  
    bt8=tk.Button(Railwaysportal,text="Back",fg="yellow",bg="Blue",command=Railwaysportal.destroy)
    bt8.place(relx=0.5,rely=0.9,anchor="center")

def Roadways_portal():
    Roadwaysportal=tk.Tk()
    Roadwaysportal.title("Roadways portal")
    Roadwaysportal.attributes('-fullscreen',True)  
    Roadwaysportal.configure(bg ="Sky Blue")
    l1=Label(Roadwaysportal,text="Roadways Portal",font=("Arial Bold",45))
    l1.configure(fg="White",bg="Sky Blue")
    l1.place(relx=0.5, rely=0.07, anchor="center")
    bt1=tk.Button(Roadwaysportal,text="Show scheduled bus chart",fg="yellow",bg="Blue",command=show_chart)
    bt1.place(relx = 0.5, rely = 0.3, anchor = 'c')
    bt2=tk.Button(Roadwaysportal,text="Add a bus",fg="yellow",bg="Blue",command=add_a_Vehicle)
    bt2.place(relx = 0.5, rely = 0.4, anchor = 'c')
    bt3=tk.Button(Roadwaysportal,text="Cancel a bus",fg="yellow",bg="Blue",command=cancel_a_Vehicle)
    bt3.place(relx = 0.5, rely = 0.5, anchor = 'c')
    bt4=tk.Button(Roadwaysportal,text="Update the chart",fg="yellow",bg="Blue",command=update_chart)
    bt4.place(relx = 0.5, rely = 0.6, anchor = 'c')
    bt5=tk.Button(Roadwaysportal,text="Cancel all buses",fg="yellow",bg="Blue",command=cav)
    bt5.place(relx = 0.5, rely = 0.7, anchor = 'c')
    bt6=tk.Button(Roadwaysportal, text="Put up the chart",fg="yellow",bg="Blue",command=put_chart)
    bt6.place(relx = 0.5, rely= 0.2 , anchor='c')
    bt7=tk.Button(Roadwaysportal,text="Show passenger list",fg="yellow",bg="Blue",command=showpaslist)
    bt7.place(relx=0.5,rely=0.8,anchor="center") 
    bt8=tk.Button(Roadwaysportal,text="Back",fg="yellow",bg="Blue",command=Roadwaysportal.destroy)
    bt8.place(relx=0.5,rely=0.9,anchor="center")

def Airways_portal():
    Airwaysportal=tk.Tk()
    Airwaysportal.title("Airways portal")
    Airwaysportal.attributes('-fullscreen',True)
    Airwaysportal.configure(bg ="Sky Blue")
    l1=Label(Airwaysportal,text="Airways Portal",font=("Arial Bold",45))
    l1.configure(fg="White",bg="Sky Blue")
    l1.place(relx=0.5, rely=0.07, anchor="center")
    bt1=tk.Button(Airwaysportal,text="Show scheduled flight chart",fg="yellow",bg="Blue",command=show_chart)
    bt1.place(relx = 0.5, rely = 0.3, anchor = 'c')
    bt2=tk.Button(Airwaysportal,text="Add a flight",fg="yellow",bg="Blue",command=add_a_Vehicle)
    bt2.place(relx = 0.5, rely = 0.4, anchor = 'c')
    bt3=tk.Button(Airwaysportal,text="Cancel a flight",fg="yellow",bg="Blue",command=cancel_a_Vehicle)
    bt3.place(relx = 0.5, rely = 0.5, anchor = 'c')
    bt4=tk.Button(Airwaysportal,text="Update the chart",fg="yellow",bg="Blue",command=update_chart)
    bt4.place(relx = 0.5, rely = 0.6, anchor = 'c')
    bt5=tk.Button(Airwaysportal,text="Cancel all flights",fg="yellow",bg="Blue",command=cav)
    bt5.place(relx = 0.5, rely = 0.7, anchor = 'c')
    bt6=tk.Button(Airwaysportal, text="Put up the chart",fg="yellow",bg="Blue",command=put_chart)
    bt6.place(relx = 0.5, rely= 0.2 , anchor='c')
    bt7=tk.Button(Airwaysportal,text="Show passenger list",fg="yellow",bg="Blue",command=showpaslist)
    bt7.place(relx=0.5,rely=0.8,anchor="center")  
    bt8=tk.Button(Airwaysportal,text="Back",fg="yellow",bg="Blue",command=Airwaysportal.destroy)
    bt8.place(relx=0.5,rely=0.9,anchor="center")
   
def Admin_portal():
    adminportal=tk.Tk()
    adminportal.title("Admin portal")
    adminportal.attributes('-fullscreen',True)  
    adminportal.configure(bg ="Sky Blue")
    l1=Label(adminportal,text="Admin Portal",font=("Arial Bold",45))
    l1.configure(fg="White",bg="Sky Blue")
    l1.place(relx=0.5, rely=0.07, anchor="center")
    bu1=tk.Button(adminportal,text="Enter Railways Portal",fg="yellow",bg="Blue",command=Railways_portal)
    bu1.place(relx = 0.5, rely = 0.4, anchor = 'c')
    bu2=tk.Button(adminportal,text="Enter Roadways Portal",fg="yellow",bg="Blue",command=Roadways_portal)
    bu2.place(relx = 0.5, rely = 0.55, anchor = 'c')
    bu3=tk.Button(adminportal,text="Enter Airways Portal",fg="yellow",bg="Blue",command=Airways_portal)
    bu3.place(relx = 0.5, rely = 0.7, anchor = 'c')
    bu4=tk.Button(adminportal,text="Add an Admin",fg="yellow",bg="Blue",command=addadmin)
    bu4.place(relx = 0.1, rely = 0.9, anchor = 'c')
    bu5=tk.Button(adminportal,text="Delete an Admin",fg="yellow",bg="Blue",command=deladmin)
    bu5.place(relx = 0.9, rely = 0.9, anchor = 'c')
    bu6=tk.Button(adminportal,text="Exit Admin Portal",fg="yellow",bg="Blue",command=adminportal.destroy)
    bu6.place(relx = 0.5, rely = 0.9, anchor = 'c')

def Admin_id():
    global photo
    
    def adminidpassword():
        c=0
        num1=username.get()
        num2=password.get()
        for i in range(len(adminku)):
            if num1 in adminku[i][0] and num2 in adminku[i][1]:
                c+=1
        if c==1:
            Admin_portal()
            adminwindow.destroy()
        else: 
            messagebox.showinfo("Attention","Invalid Username or Password!")
        
    adminwindow=tk.Tk()
    adminwindow.title("Admin login")
    adminwindow.attributes('-fullscreen',True) 
    adminwindow.configure(bg ="light Green")
    l4=tk.Label(master=adminwindow,text="Enter required credentials to enter the portal",font=("Arial",20))
    l4.configure(fg="White",bg="light Green")
    l4.place(relx=0.55,rely=0.2,anchor="center")
    l2=tk.Label(master=adminwindow,text="Username")
    l2.place(relx=0.5,rely=0.4,anchor="center")
    username=tk.Entry(master=adminwindow)
    username.place(relx=0.6,rely=0.4,anchor="center")
    l3=tk.Label(master=adminwindow,text="Password")
    l3.place(relx=0.5,rely=0.45,anchor="center")
    password=tk.Entry(master=adminwindow,show="*")
    password.place(relx=0.6,rely=0.45,anchor="center")    
    bt6=tk.Button(adminwindow,text="Submit",fg="yellow",bg="Blue",command=adminidpassword)
    bt6.place(relx=0.55,rely=0.5,anchor="center")
    bt7=tk.Button(adminwindow,text="Back",fg="yellow",bg="Blue",command=adminwindow.destroy)
    bt7.place(relx=0.65,rely=0.5,anchor="center")
      
def About_us():
    f=open("About us.txt","r")
    s=a=' '
    while s:
        s=f.read()
        s=s.strip()
        a+=s
    messagebox.showinfo("About us",a)

def itroadways():  
    f=open("itroadways.txt","r")
    s=a=' '
    while s:
        s=f.read()
        s=s.strip()
        a+=s
    f.close()
    messagebox.showinfo("Know about Roadways",a)
    
def itrailways():
    f=open("itrailways.txt","r")
    s=a=' '
    while s:
        s=f.read()
        s=s.strip()
        a+=s
    f.close()
    messagebox.showinfo("Know about Railways",a)
    
def itairways():
    f=open("itairways.txt","r")
    s=a=' '
    while s:
        s=f.read()
        s=s.strip()
        a+=s
    f.close()
    messagebox.showinfo("Know about Airways",a)
          
def ITSHOW():
    itshow=tk.Tk()
    itshow.title=("Indian Transport")
    itshow.geometry('500x500+50+50')  
    itshow.configure(bg ="green")
    l1=Label(itshow,text="Select an option",font=("Arial Bold",25))
    l1.configure(fg="White",bg="green")
    l1.place(relx=0.4, rely=0.2, anchor="center")
    bt1=tk.Button(itshow,text="Roadways(Bus Services)",fg="yellow",bg="Blue",command=itroadways)
    bt1.place(relx = 0.5, rely = 0.4, anchor = 'c')
    bt2=tk.Button(itshow,text="Railways",fg="yellow",bg="Blue",command=itrailways)
    bt2.place(relx = 0.5, rely = 0.5, anchor = 'c')
    bt3=tk.Button(itshow,text="Airways",fg="yellow",bg="Blue",command=itairways)
    bt3.place(relx = 0.5, rely = 0.6, anchor = 'c')

def help():
    print("Help lam onnum panna maten, poda")


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

def Railways_booking(*args):
    def search_train(*args):
        class Table: 
            def __init__(self,strain):
                c=0
                da=vari.get()
                ma=vari1.get()
                ca=e1.get()
                print(da,ma,ca)
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
    drop1=OptionMenu(railbook,vari,'AGRA FORT(AF)','AHMEDABAD(ADI)','ALLAHABAD(ALD)','AMRITSAR(ASR)',
       'BANGALORE CITY(SBC)','BARAUNI Jn.(BJU)','BHOPAL(BPL)','BHUBANESWAR(BBS)','BIKANER(BKN)','BILASPUR jn.(BSP)',
       'BOKARO STEEL CITY(BKSC)','CHANDIGARH(CDG)','CHENNAI CENTRAL(MAS)','CHENNAI EGMORE(MS)','COIMBATORE Jn.(CBE)',
       'DEHRADUN(DDN)','DELHI(DLI)','DURG(DURG)','ERNAKULAM Jn.(ERS)','FIROZPUR CITY(FZP)','GORAKHPUR(GKP)',
       'GUWAHATI(GHY)','GWALIOR(GWL)','HAJIPUR(HJP)','HUBLI(UBL)','HYDERABAD(HYB)','INDORE(INDB)','JAIPUR(JP)',
       'JAISALMER(JSM)','JHANSI(JHS)','JODHPUR(JU)','KACHEGUDA(KCG)','KANNIYAKUMARI(CAPE)','KANPUR CENTRAL(CNB)',
       'KOLKATA(KOAA)','LUCKNOW(LJN/LKO)','MADGAON(GOA)(MAO)','MANGALORE CENTRAL(MAQ)','MATHURA(MTJ)','METTUPALAYAM(MTP)',
       'MUMBAI CENTRAL(BCT)','MYSORE(MYS)','NAGERCOIL Jn.(NCJ)','NAGPUR(NGP)','NIZAMABAD(NZB)','PATNA(PNBE)','PORBANDAR PBR',
       'PUNE Jn.(PUNE)','RAIPUR(R)','RAMESWARAM(RMM)','RANCHI(RNC)','SECUNDERABAD(SC)','SHIMLA(SML)','THANJAVUR(TJ)',
       'TIRUCHCHIRAPPALLI Jn.(TPJ)','THIRUVANANTHAPURAM(TVC)','TUTICORIN(TN)','UDAIPUR CITY(UDZ)','VADODARA(BRC)','VARANASI(BSB)',
       'VIJAYAWADA(BZA)','VISAKHAPATNAM(VSKP)')
    drop1.place(relx=0.20,rely=0.4,anchor="center")
    To=Label(railbook,text="DESTINATION",fg="Blue",bg="yellow")
    To.place(relx=0.07,rely=0.5,anchor="center")
    drop2=OptionMenu(railbook,vari1,'AGRA FORT(AF)','AHMEDABAD(ADI)','ALLAHABAD(ALD)','AMRITSAR(ASR)',
       'BANGALORE CITY(SBC)','BARAUNI Jn.(BJU)','BHOPAL(BPL)','BHUBANESWAR(BBS)','BIKANER(BKN)','BILASPUR jn.(BSP)',
       'BOKARO STEEL CITY(BKSC)','CHANDIGARH(CDG)','CHENNAI CENTRAL(MAS)','CHENNAI EGMORE(MS)','COIMBATORE Jn.(CBE)',
       'DEHRADUN(DDN)','DELHI(DLI)','DURG(DURG)','ERNAKULAM Jn.(ERS)','FIROZPUR CITY(FZP)','GORAKHPUR(GKP)',
       'GUWAHATI(GHY)','GWALIOR(GWL)','HAJIPUR(HJP)','HUBLI(UBL)','HYDERABAD(HYB)','INDORE(INDB)','JAIPUR(JP)',
       'JAISALMER(JSM)','JHANSI(JHS)','JODHPUR(JU)','KACHEGUDA(KCG)','KANNIYAKUMARI(CAPE)','KANPUR CENTRAL(CNB)',
       'KOLKATA(KOAA)','LUCKNOW(LJN/LKO)','MADGAON(GOA)(MAO)','MANGALORE CENTRAL(MAQ)','MATHURA(MTJ)','METTUPALAYAM(MTP)',
       'MUMBAI CENTRAL(BCT)','MYSORE(MYS)','NAGERCOIL Jn.(NCJ)','NAGPUR(NGP)','NIZAMABAD(NZB)','PATNA(PNBE)','PORBANDAR PBR',
       'PUNE Jn.(PUNE)','RAIPUR(R)','RAMESWARAM(RMM)','RANCHI(RNC)','SECUNDERABAD(SC)','SHIMLA(SML)','THANJAVUR(TJ)',
       'TIRUCHCHIRAPPALLI Jn.(TPJ)','THIRUVANANTHAPURAM(TVC)','TUTICORIN(TN)','UDAIPUR CITY(UDZ)','VADODARA(BRC)','VARANASI(BSB)',
       'VIJAYAWADA(BZA)','VISAKHAPATNAM(VSKP)')
    drop2.place(relx=0.20,rely=0.5,anchor="center")
    date=Label(railbook,text="DATE",fg="Blue",bg="yellow")
    date.place(relx=0.07,rely=0.6)
    e1=Entry(railbook,bg="yellow",fg="black")
    e1.place(relx=0.18,rely=0.6)
    nop=Label(railbook,text="NO OF PASSENGERS",fg="Blue",bg="yellow")
    nop.place(relx=0.07,rely=0.7)
    e2=Entry(railbook,bg="yellow",fg="black")
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
    

def Guest_login():
    window1=tk.Tk()
    window1.title("MRF.com/Guest/choosing mode of transport")
    window1.attributes('-fullscreen',True)
    window1.configure(bg ="blue")
    l1=Label(window1,text="Choose your mode of transport",font=("Arial Bold",45),anchor='c')
    l1.configure(fg="White",bg="blue")
    l1.pack()
    gt=tk.Button(window1,text="Airways",fg="White",bg="Black",command= Guest_Airways)
    gt.place(relx = 0.5, rely = 0.4, anchor = 'c')
    gt1=tk.Button(window1,text="Railways",fg="White",bg="Black",command= Guest_Railways)
    gt1.place(relx = 0.5, rely = 0.5, anchor = 'c')
    gt2=tk.Button(window1,text="Roadways",fg="White",bg="Black",command= Guest_Roadways)
    gt2.place(relx = 0.5, rely = 0.6, anchor = 'c')
    bt=tk.Button(window1,text="Back",fg="White",bg="Black",command=window1.destroy)
    bt.place(relx=0.5,rely=0.7,anchor="c")
    
    
def Guest_Airways():

    def searchpannalama():
        of=airportsfrom.get()
        ot=airportsto.get()
        dateo=day.get()+" "+month.get()+" "+year.get()
        print(of,ot,dateo)
        f=open("Airways.csv",'r')
        lab=tom=0
        robj=csv.reader(f,delimiter=",")
        for a in robj:
            if tom%2==0:
                if a[2]==of and a[3]==ot and dateo==a[4]:
                    print(a[0],a[1],a[2],a[3],a[4],a[5],a[6])
                    lab+=1
                    break
            tom+=1
        if lab==0:
            print("No flight found")
    
    windowA=tk.Tk()
    windowA.title("MRF.com/Guest/choosing mode of transport/Airways")
    windowA.attributes('-fullscreen',True)
    windowA.configure(bg ="Blue")
    lc=Label(windowA,text='Enter the required details',font=("Arial Bold",25))
    lc.place(relx = 0.4, rely = 0.14)
    lc.configure(fg="White",bg="Blue")
    l1=Label(windowA,text='From:',font=("Arial Bold",10))
    l1.place(relx = 0.25, rely = 0.35)
    l1.configure(fg="White",bg="Blue")
    from tkinter import ttk
    airportsfrom=ttk.Combobox(windowA,values=['Rajiv Gandhi International Airport(Hyderabad, Telangana)',
       'Sri Guru Ram Dass Jee International Airport(Amritsar, Punjab)',
       'Indira Gandhi International Airport(New Delhi, Delhi)',
       'Sardar Vallabhbhai Patel International Airport(Ahmedabad, Gujarat)',
       'Kempegowda International Airport(Bengaluru, Karnataka)',
       'Cochin International Airport(Kochi, Kerala)',
       'Calicut International Airport(Kozhikode, Kerala)'
       'Chhatrapati Shivaji International Airport(Mumbai, Maharashtra)',
       'Pune Airport(Pune, Maharashtra)',
       'Jaipur International Airport(Jaipur, Rajasthan)',
       'Chennai International Airport(Chennai, Tamil Nadu)',
       'Civil Aerodrome(Coimbatore, Tamil Nadu)',
       'Chandigarh Airport(Chandigarh)',
       'Dabolim Airport(Goa)'])
    airportsfrom.place(relx = 0.3, rely = 0.4, anchor = 'c')
    airportsfrom.current()
    l2=Label(windowA,text='To:',font=("Arial Bold",10))
    l2.place(relx = 0.25, rely = 0.55)
    l2.configure(fg="White",bg="Blue")
    airportsto=ttk.Combobox(windowA,values=['Rajiv Gandhi International Airport(Hyderabad, Telangana)',
       'Sri Guru Ram Dass Jee International Airport(Amritsar, Punjab)',
       'Indira Gandhi International Airport(New Delhi, Delhi)',
       'Sardar Vallabhbhai Patel International Airport(Ahmedabad, Gujarat)',
       'Kempegowda International Airport(Bengaluru, Karnataka)',
       'Cochin International Airport(Kochi, Kerala)',
       'Calicut International Airport(Kozhikode, Kerala)'
       'Chhatrapati Shivaji International Airport(Mumbai, Maharashtra)',
       'Pune Airport(Pune, Maharashtra)',
       'Jaipur International Airport(Jaipur, Rajasthan)',
       'Chennai International Airport(Chennai, Tamil Nadu)',
       'Civil Aerodrome(Coimbatore, Tamil Nadu)',
       'Chandigarh Airport(Chandigarh)',
       'Dabolim Airport(Goa)'])
    airportsto.place(relx = 0.3, rely = 0.6, anchor = 'c')
    airportsto.current()
    ld=Label(windowA,text='Day:',font=("Arial Bold",10))
    ld.place(relx = 0.45, rely = 0.35)
    ld.configure(fg="White",bg="Blue")
    day=ttk.Combobox(windowA,values=vai)
    day.place(relx = 0.45, rely = 0.4, anchor = 'c')
    day.current()
    
    l3=Label(windowA,text='Month:',font=("Arial Bold",10))
    l3.place(relx = 0.6, rely = 0.35)
    l3.configure(fg="White",bg="Blue")
    month=ttk.Combobox(windowA,values=['January','February','March',
                                       'April','May','June','July',
                                       'August','September','October',
                                       'November','December'])
    month.place(relx = 0.6, rely = 0.4, anchor = 'c')
    month.current()
    l4=Label(windowA,text='Year:',font=("Arial Bold",10))
    l4.place(relx = 0.75, rely = 0.35)
    l4.configure(fg="White",bg="Blue")
    year=ttk.Combobox(windowA,values=['2020','2021','2022'])
    year.place(relx = 0.8, rely = 0.4, anchor = 'c')
    year.current()
    adult=ttk.Combobox(windowA,values=['1','2','3','4','5','6','7','8','9'])
    adult.place(relx = 0.7, rely = 0.6, anchor = 'c')
    l5=Label(windowA,text='Adults:',font=("Arial Bold",10))
    l5.place(relx = 0.65, rely = 0.55)
    l5.configure(fg="White",bg="Blue")
    children=ttk.Combobox(windowA,values=['1','2','3','4','5','6','7','8','9'])
    children.place(relx = 0.8, rely = 0.6, anchor = 'c')
    l6=Label(windowA,text='Children(2-11yrs):',font=("Arial Bold",10))
    l6.place(relx = 0.75, rely =0.55)
    l6.configure(fg="White",bg="Blue")
    infants=ttk.Combobox(windowA,values=['0','1'])
    infants.place(relx = 0.7, rely = 0.7, anchor='c')
    l7=Label(windowA,text='Infants(below 2yrs):',font=("Arial Bold",10))
    l7.place(relx = 0.65, rely = 0.65)
    l7.configure(fg="White",bg="Blue")
    bt=ttk.Button(windowA,text="Back",command=windowA.destroy)
    bt.place(relx=0.7,rely=0.9,anchor="c")
    bt2=ttk.Button(windowA,text="Search",command=searchpannalama)
    bt2.place(relx=0.5,rely=0.9,anchor="c") 
                                       
def Guest_Railways():
    windowR=tk.Tk()
    windowR.title("MRF.com/Guest/choosing mode of transport/Airways")
    windowR.attributes('-fullscreen',True)
    windowR.configure(bg ="Blue")
    lc=Label(windowR,text='Enter the required details',font=("Arial Bold",25))
    lc.place(relx = 0.4, rely = 0.14)
    lc.configure(fg="White",bg="Blue")
    l1=Label(windowR,text='From:',font=("Arial Bold",10))
    l1.place(relx = 0.25, rely = 0.35)
    l1.configure(fg="White",bg="Blue")
    from tkinter import ttk
    railwaysfrom=ttk.Combobox(windowR,values=['AGRA FORT(AF)','AHMEDABAD(ADI)','ALLAHABAD(ALD)','AMRITSAR(ASR)',
       'BANGALORE CITY(SBC)','BARAUNI Jn.(BJU)','BHOPAL(BPL)','BHUBANESWAR(BBS)','BIKANER(BKN)','BILASPUR jn.(BSP)',
       'BOKARO STEEL CITY(BKSC)','CHANDIGARH(CDG)','CHENNAI CENTRAL(MAS)','CHENNAI EGMORE(MS)','COIMBATORE Jn.(CBE)',
       'DEHRADUN(DDN)','DELHI(DLI)','DURG(DURG)','ERNAKULAM Jn.(ERS)','FIROZPUR CITY(FZP)','GORAKHPUR(GKP)',
       'GUWAHATI(GHY)','GWALIOR(GWL)','HAJIPUR(HJP)','HUBLI(UBL)','HYDERABAD(HYB)','INDORE(INDB)','JAIPUR(JP)',
       'JAISALMER(JSM)','JHANSI(JHS)','JODHPUR(JU)','KACHEGUDA(KCG)','KANNIYAKUMARI(CAPE)','KANPUR CENTRAL(CNB)',
       'KOLKATA(KOAA)','LUCKNOW(LJN/LKO)','MADGAON(GOA)(MAO)','MANGALORE CENTRAL(MAQ)','MATHURA(MTJ)','METTUPALAYAM(MTP)',
       'MUMBAI CENTRAL(BCT)','MYSORE(MYS)','NAGERCOIL Jn.(NCJ)','NAGPUR(NGP)','NIZAMABAD(NZB)','PATNA(PNBE)','PORBANDAR PBR',
       'PUNE Jn.(PUNE)','RAIPUR(R)','RAMESWARAM(RMM)','RANCHI(RNC)','SECUNDERABAD(SC)','SHIMLA(SML)','THANJAVUR(TJ)',
       'TIRUCHCHIRAPPALLI Jn.(TPJ)','THIRUVANANTHAPURAM(TVC)','TUTICORIN(TN)','UDAIPUR CITY(UDZ)','VADODARA(BRC)','VARANASI(BSB)',
       'VIJAYAWADA(BZA)','VISAKHAPATNAM(VSKP)'])
    railwaysfrom.place(relx = 0.3, rely = 0.4, anchor = 'c')
    railwaysfrom.current()
    l2=Label(windowR,text='To:',font=("Arial Bold",10))
    l2.place(relx = 0.25, rely = 0.55)
    l2.configure(fg="White",bg="Blue")
    railwaysto=ttk.Combobox(windowR,values=['AGRA FORT(AF)','AHMEDABAD(ADI)','ALLAHABAD(ALD)','AMRITSAR(ASR)',
       'BANGALORE CITY(SBC)','BARAUNI Jn.(BJU)','BHOPAL(BPL)','BHUBANESWAR(BBS)','BIKANER(BKN)','BILASPUR jn.(BSP)',
       'BOKARO STEEL CITY(BKSC)','CHANDIGARH(CDG)','CHENNAI CENTRAL(MAS)','CHENNAI EGMORE(MS)','COIMBATORE Jn.(CBE)',
       'DEHRADUN(DDN)','DELHI(DLI)','DURG(DURG)','ERNAKULAM Jn.(ERS)','FIROZPUR CITY(FZP)','GORAKHPUR(GKP)',
       'GUWAHATI(GHY)','GWALIOR(GWL)','HAJIPUR(HJP)','HUBLI(UBL)','HYDERABAD(HYB)','INDORE(INDB)','JAIPUR(JP)',
       'JAISALMER(JSM)','JHANSI(JHS)','JODHPUR(JU)','KACHEGUDA(KCG)','KANNIYAKUMARI(CAPE)','KANPUR CENTRAL(CNB)',
       'KOLKATA(KOAA)','LUCKNOW(LJN/LKO)','MADGAON(GOA)(MAO)','MANGALORE CENTRAL(MAQ)','MATHURA(MTJ)','METTUPALAYAM(MTP)',
       'MUMBAI CENTRAL(BCT)','MYSORE(MYS)','NAGERCOIL Jn.(NCJ)','NAGPUR(NGP)','NIZAMABAD(NZB)','PATNA(PNBE)','PORBANDAR PBR',
       'PUNE Jn.(PUNE)','RAIPUR(R)','RAMESWARAM(RMM)','RANCHI(RNC)','SECUNDERABAD(SC)','SHIMLA(SML)','THANJAVUR(TJ)',
       'TIRUCHCHIRAPPALLI Jn.(TPJ)','THIRUVANANTHAPURAM(TVC)','TUTICORIN(TN)','UDAIPUR CITY(UDZ)','VADODARA(BRC)','VARANASI(BSB)',
       'VIJAYAWADA(BZA)','VISAKHAPATNAM(VSKP)'])
    railwaysto.place(relx = 0.3, rely = 0.6, anchor = 'c')
    railwaysto.current()
    ld=Label(windowR,text='Day:',font=("Arial Bold",10))
    ld.place(relx = 0.45, rely = 0.35)
    ld.configure(fg="White",bg="Blue")
    day=ttk.Combobox(windowR,values=vai)
    day.place(relx = 0.45, rely = 0.4, anchor = 'c')
    day.current()
    l3=Label(windowR,text='Month:',font=("Arial Bold",10))
    l3.place(relx = 0.6, rely = 0.35)
    l3.configure(fg="White",bg="Blue")
    month=ttk.Combobox(windowR,values=['January','February','March',
                                       'April','May','June','July',
                                       'August','September','October',
                                       'November','December'])
    month.place(relx = 0.6, rely = 0.4, anchor = 'c')
    month.current()
    l4=Label(windowR,text='Year:',font=("Arial Bold",10))
    l4.place(relx = 0.75, rely = 0.35)
    l4.configure(fg="White",bg="Blue")
    year=ttk.Combobox(windowR,values=['2020','2021','2022'])
    year.place(relx = 0.8, rely = 0.4, anchor = 'c')
    year.current()
    adult=ttk.Combobox(windowR,values=['1','2','3','4','5','6'])
    adult.place(relx = 0.7, rely = 0.6, anchor = 'c')
    l5=Label(windowR,text='Adults(12-60yrs):',font=("Arial Bold",10))
    l5.place(relx = 0.65, rely = 0.55)
    l5.configure(fg="White",bg="Blue")
    children=ttk.Combobox(windowR,values=['1','2','3','4','5','6'])
    children.place(relx = 0.8, rely = 0.6, anchor = 'c')
    l6=Label(windowR,text='Children(5-11yrs):',font=("Arial Bold",10))
    l6.place(relx = 0.75, rely =0.55)
    l6.configure(fg="White",bg="Blue")
    seniormen=ttk.Combobox(windowR,values=['1','2','3','4','5','6'])
    seniormen.place(relx = 0.7, rely = 0.7, anchor='c')
    l7=Label(windowR,text='Senior Men(60+yrs):',font=("Arial Bold",10))
    l7.place(relx = 0.65, rely = 0.65)
    l7.configure(fg="White",bg="Blue")
    seniorwomen=ttk.Combobox(windowR,values=['1','2','3','4','5','6'])
    seniorwomen.place(relx = 0.8, rely = 0.7, anchor='c')
    l8=Label(windowR,text='Senior Men(58+yrs):',font=("Arial Bold",10))
    l8.place(relx = 0.75, rely = 0.65)
    l8.configure(fg="White",bg="Blue")
    bt=ttk.Button(windowR,text="Back",command=windowR.destroy)
    bt.place(relx=0.7,rely=0.9,anchor="c")
    bt2=ttk.Button(windowR,text="Search")
    bt2.place(relx=0.5,rely=0.9,anchor="c")
        

def Guest_Roadways():

    windowr=tk.Tk()
    windowr.title("MRF.com/Guest/choosing mode of transport/Airways")
    windowr.attributes('-fullscreen',True)
    windowr.configure(bg ="Blue")
    lc=Label(windowr,text='Enter the required details',font=("Arial Bold",25))
    lc.place(relx = 0.4, rely = 0.14)
    lc.configure(fg="White",bg="Blue") 
    l1=Label(windowr,text='From:',font=("Arial Bold",10))
    l1.place(relx = 0.25, rely = 0.35)
    l1.configure(fg="White",bg="Blue")
    from tkinter import ttk
    roadwaysfrom=ttk.Combobox(windowr,values=['Mumbai','Delhi','Bangalore','Hyderabad','Ahmedabad','Chennai','Kolkata','Surat','Pune','Jaipur',
                                              'Lucknow','Kanpur','Nagpur','Indore','Bhopal','Visakhapatnam','Patna','Agra','Varanasi','Amritsar',
                                              'Ranchi','Coimbatore','Gwalior','Vijayawada','Jodhpur','Madurai','Raipur','Kota','Chandigarh','Hubli',
                                              'Mysore','Gurgaon','Tiruchirappalli','Salem','Thiruvananthapuram','Amravati','Noida','Firozabad',
                                              'Kochi','Dehradun','Ujjain','Jhansi','Nellore','Mangalore','Tirunelveli','Udaipur'])
    roadwaysfrom.place(relx = 0.3, rely = 0.4, anchor = 'c')
    roadwaysfrom.current()
    l2=Label(windowr,text='To:',font=("Arial Bold",10))
    l2.place(relx = 0.25, rely = 0.55)
    l2.configure(fg="White",bg="Blue")
    roadwaysto=ttk.Combobox(windowr,values=['Mumbai','Delhi','Bangalore','Hyderabad','Ahmedabad','Chennai','Kolkata','Surat','Pune','Jaipur',
                                            'Lucknow','Kanpur','Nagpur','Indore','Bhopal','Visakhapatnam','Patna','Agra','Varanasi','Amritsar',
                                            'Ranchi','Coimbatore','Gwalior','Vijayawada','Jodhpur','Madurai','Raipur','Kota','Chandigarh','Hubli',
                                            'Mysore','Gurgaon','Tiruchirappalli','Salem','Thiruvananthapuram','Amravati','Noida','Firozabad',
                                            'Kochi','Dehradun','Ujjain','Jhansi','Nellore','Mangalore','Tirunelveli','Udaipur'])
    roadwaysto.place(relx = 0.3, rely = 0.6, anchor = 'c')
    roadwaysto.current()
    ld=Label(windowr,text='Day:',font=("Arial Bold",10))
    ld.place(relx = 0.45, rely = 0.35)
    ld.configure(fg="White",bg="Blue")
    day=ttk.Combobox(windowr,values=vai)
    day.place(relx = 0.45, rely = 0.4, anchor = 'c')
    day.current()
    l3=Label(windowr,text='Month:',font=("Arial Bold",10))
    l3.place(relx = 0.6, rely = 0.35)
    l3.configure(fg="White",bg="Blue")
    month=ttk.Combobox(windowr,values=['January','February','March',
                                       'April','May','June','July',
                                       'August','September','October',
                                       'November','December'])
    month.place(relx = 0.6, rely = 0.4, anchor = 'c')
    month.current()
    l4=Label(windowr,text='Year:',font=("Arial Bold",10))
    l4.place(relx = 0.75, rely = 0.35)
    l4.configure(fg="White",bg="Blue")
    year=ttk.Combobox(windowr,values=['2020','2021','2022'])
    year.place(relx = 0.8, rely = 0.4, anchor = 'c')
    year.current()
    bt=ttk.Button(windowr,text="Back",command=windowr.destroy)
    bt.place(relx=0.7,rely=0.9,anchor="c")
    bt2=ttk.Button(windowr,text="Search")
    bt2.place(relx=0.5,rely=0.9,anchor="c") 
       
bt=tk.Button(window,text="Admin Login",fg="yellow",bg="Blue",command=Admin_id)
bt.place(relx = 0.5, rely = 0.4, anchor = 'c')
bt2=tk.Button(window,text=" User Login",fg="yellow",bg="Blue",command=user_login)
bt2.place(relx = 0.5, rely = 0.5, anchor = 'c')
bt3=tk.Button(window,text="Guest Login",fg="yellow",bg="Blue",command=Guest_login)
bt3.place(relx = 0.5, rely = 0.6, anchor = 'c')
bt4=tk.Button(window,text="   Exit    ",fg="yellow",bg="Blue",command=Exit)
bt4.place(relx = 0.5, rely = 0.7, anchor = 'c')
bt5=tk.Button(window,text="Help",fg="yellow",bg="blue",command=help)
bt5.place(relx=0.1,rely=0.9,anchor="c")
bt6=tk.Button(window,text="Know about Indian Transport",fg="Yellow",bg="blue",command=ITSHOW)
bt6.place(relx=0.5,rely=0.9,anchor="c")
bt7=tk.Button(window,text="About us",fg="yellow",bg="blue",command=About_us)
bt7.place(relx=0.9,rely=0.9,anchor="c")
window.mainloop()



'''Sri Guru Ram Dass Jee International Airport(Amritsar, Punjab)   
Rajiv Gandhi International Airport(Hyderabad, Telangana)

How to get the name which have been inputed 'inform'
User ID Password of user how to create
Tabular column label mela varanum
Bill'''

