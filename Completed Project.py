from tkinter import *
from tkinter import ttk
import pickle
import os
import csv
from tkinter import messagebox
import tkinter.font as font
import datetime  
import random    
current_time = datetime.datetime.now()      
def start():
    global window
    try:
        adminwindow.destroy()           
    except:
        try:
            userwindow.destroy()
        except:
            try:
                window1.destroy()
            except:
                try:
                    userportal.destroy()
                except:
                    try:
                        adminportal.destroy()
                    except:
                        try:
                            reg.destroy()
                        except:
                            print()                                                                                    
                                                                                            
    window=Tk()
    window.attributes('-fullscreen',True)
    window.title("MRF.com")    
    myFont = font.Font(size=25)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(window,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack   
    photo=PhotoImage(file="project.png")
    label=Label(window,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image =photo
    label.pack 
    l1=Label(window,text="Welcome to Move Run Fly", font=("Arial Bold",45))
    l1.configure(fg="white",bg='black')
    l1.pack()
    bt=Button(window,text="Admin Login",fg="White",bg="Black",command=Admin_id)
    bt['font'] = myFont
    bt.place(relx = 0.5, rely = 0.25, anchor = 'c')
    bt2=Button(window,text=" User Login",fg="White",bg="Black",command=user_login)
    bt2['font'] = myFont
    bt2.place(relx = 0.5, rely = 0.42, anchor = 'c')
    bt3=Button(window,text="Guest Login",fg="White",bg="Black",command=Guest_login)
    bt3['font'] = myFont
    bt3.place(relx = 0.5, rely = 0.59, anchor = 'c')
    bt4=Button(window,text="   Exit    ",fg="White",bg="Black",command=Exit)
    bt4['font'] = myFont
    bt4.place(relx = 0.5, rely = 0.76, anchor = 'c')
    bt5=Button(window,text="Help",fg="White",bg="Black",command=Help)
    bt5['font'] = myFont
    bt5.place(relx=0.1,rely=0.9,anchor="c")
    bt6=Button(window,text="Know about Indian Transport",fg="White",bg="Black",command=ITSHOW)
    bt6['font'] = myFont
    bt6.place(relx=0.5,rely=0.9,anchor="c")
    bt7=Button(window,text="About us",fg="White",bg="Black",command=About_us)
    bt7['font'] = myFont
    bt7.place(relx=0.9,rely=0.9,anchor="c")
    
def start1():
    
    try:
        bankin.destroy()
    except:
        try:
            windowA.destroy()
            Guest_login()
        except:
            try:
                windowh.destroy()
                start()
            except:
                try:
                    itshow.destroy()
                    start()
                except:
                    try:
                        windowR.destroy()
                        Guest_login()
                    except:
                        try:
                            windowr.destroy()
                            Guest_login()
                        except:
                            try:
                                Roadwaysportal.destroy()
                                Admin_portal()
                            except:
                                try:
                                    Airwaysportal.destroy()                                    
                                    Admin_portal()
                                except:
                                    try:
                                        Railwaysportal.destroy()
                                        Admin_portal()
                                    except:
                                        try:
                                            cav.destroy()
                                            Admin_portal()
                                        except:
                                            try:
                                                windowAa.destroy()
                                                user_portal()
                                            except:
                                                try:
                                                    windowRa.destroy()
                                                    user_portal()
                                                except:
                                                    try:
                                                        windowra.destroy()
                                                        user_portal()
                                                    except:
                                                        try:
                                                            addadmin.destroy()
                                                            Admin_portal()
                                                        except:
                                                            try:
                                                                deladmin.destroy()
                                                                Admin_portal()
                                                            except:
                                                                try:
                                                                    aav.destroy()
                                                                    Admin_portal()
                                                                except:
                                                                    try:
                                                                        bil.destroy()
                                                                        start()
                                                                    except:
                                                                        print()

def start2():
    try:
        the.destroy()
        Admin_portal()
    except:
        try:
            ct.destroy()
            user_portal()
        except:
            try:
                paslist.destroy()
                Admin_portal()
            except:
                try:
                    cv.destroy()
                    Admin_portal()
                except:
                    try:
                        ca1v.destroy()
                        Admin_portal()
                    except:
                        print()
                                                                                                                                                                                                                                                                                                               
d=[["Railways","Train"],["Roadways","Bus"],["Airways","Flight"]]
adminku=[["Srijith","12f214"],["Devadarshan","12f207"],["Syed","12f242"],["1","1"]]
userlogin=[["Srijith","12f214"],["Devadarshan","12f207"],["Syed","12f242"],["1","1"]]
banklogin=[["Srijith","12f214"],["Devadarshan","12f207"],["Syed","12f242"],["1","1"]]
vai=ne=[]
banks=[("ICICI","ICICI"),("SBI","SBI"),('HDFC','HDFC')]
Railwayspassenger=[]
Airwayspassenger=[]
Roadwayspassenger=[]
Railwaysdestination=['AGRA FORT(AF)','BANGALORE CITY(SBC)','CHENNAI CENTRAL(MAS)','COIMBATORE Jn.(CBE)','DELHI(DLI)','HYDERABAD(HYB)','KOLKATA(KOAA)','MUMBAI CENTRAL(BCT)','PUNE Jn.(PUNE)','TIRUPATI(TPTY)']
Airports=['Rajiv Gandhi International Airport(Hyderabad, Telangana)',
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
       'Dabolim Airport(Goa)']

Airwaysdestination=['Hyderabad','Amritsar','New Delhi','Ahmedabad','Bengaluru','Kochi','Kozhikode','Mumbai', 'Pune ','Jaipur','Chennai','Coimbatore','Chandigarh','Goa']

Roadwaysdestination=['Mumbai','Delhi','Bangalore','Hyderabad','Ahmedabad','Chennai','Kolkata','Surat','Pune','Jaipur',
                                        'Lucknow','Kanpur','Nagpur','Indore','Bhopal','Visakhapatnam','Patna','Agra','Varanasi','Amritsar',
                                        'Ranchi','Coimbatore','Gwalior','Vijayawada','Jodhpur','Madurai','Raipur','Kota','Chandigarh','Hubli',
                                        'Mysore','Gurgaon','Tiruchirappalli','Salem','Thiruvananthapuram','Amravati','Noida','Firozabad',
                                        'Kochi','Dehradun','Ujjain','Jhansi','Nellore','Mangalore','Tirunelveli','Udaipur']

Flightseat=[]
busseat=[]
for i in range(1,32):
    vai.append(str(i))

for j in range (1,31):
    Flightseat.append(str(j))

for k in range (1,31):
    busseat.append(str(k))    
teach=[]
e=[]
w12=[]
debit=['33','48','73','27','89','32','25','99']
available=[]
pnr=[]
    
def cav():
    def cancelloop():
        fna=cavc.get()
        fna+=".csv"
        f=open(fna,"r")
        robj=csv.reader(f,delimiter=",")
        r=list(robj)
        x=0
        for a in r:
            if x%2==0:
                a[6]="Cancelled"
            x+=1
        messagebox.showinfo("Success","All Scheduled Vehicles Cancelled")
        f.close()
        f=open(fna,"w")
        wobj=csv.writer(f,delimiter=",")
        m=0
        for b in r:
            if m%2==0:
                wobj.writerow(b)
            m+=1
        f.close()

    try:
        Roadwaysportal.destroy()
    except:
        try:
            Airwaysportal.destroy()
        except:
            try:
                Railwaysportal.destroy()
            except:
                print()
        
    global cav    
    cav=Tk()
    cav.attributes('-fullscreen',True)
    cav.title("Cancel all vehicles")
    myFont = font.Font(size=25) 
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(cav,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(cav,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l1=Label(cav,text="Cancelling all vehicles",font=("Arial Bold",45))
    l1.configure(fg="white",bg="black")
    l1.place(relx=0.5, rely=0.04, anchor="center")
    l2=Label(cav,text="Enter the chart",font=("Arial Bold",25))
    l2.configure(fg="white",bg="black")
    l2.place(relx=0.3, rely=0.5, anchor="center")
    cavc=Entry(cav,width=25,font=('Arial Bold',20))
    cavc.place(relx=0.6,rely=0.5, anchor="center")
    but1=Button(cav,text="Confirm",fg="white",bg="black",command=cancelloop)
    but1.place(relx = 0.35, rely = 0.6, anchor = 'c')
    but1['font']=myFont
    but2=Button(cav,text="Back",fg="white",bg="black",command=start1)
    but2.place(relx = 0.55, rely = 0.6, anchor = 'c')
    but2['font']=myFont       

def update_chart():
           
    def check():       

        def stillcheck():            
            
            def appendit():
                q=fna+".csv"
                king=open(q,"a")
                w=0
                wobj=csv.writer(king,delimiter=",")
                wobj.writerow([numberu.get(),name.get(),From.get(),To.get(),Dept.get(),Arr.get(),Status.get()])
                messagebox.showinfo("Sucess","Sucessfully updated the chart")
                king.flush()
                king.close()

            q=fna+".csv"
            f=open(q,"r")
            aq=[]
            robj=csv.reader(f,delimiter=",")
            w=0
            roeo=list(robj)
            abc=0
            for a in roeo :
                if w%2==0:                    
                    if checkname.get()==a[1]:                                                                               
                        ther=Tk()
                        ther.attributes('-fullscreen',True)
                        ther.title("Updating the Chart")
                        ther.configure(bg="Light Blue")
                        myFont = font.Font(size=25) 
                        l=Label(ther,text="Enter the Details ",font=("Arial Bold",45))
                        l.configure(fg="white",bg="black")
                        l.place(relx=0.5, rely=0.1, anchor="center")
                        l1=Label(ther,text="Enter "+v+" number",font=("Arial Bold",25))
                        l1.configure(fg="white",bg="black")
                        l1.place(relx=0.4, rely=0.2, anchor="center")
                        numberu=Entry(ther,width=25,font=('Arial Bold',20))
                        numberu.place(relx=0.65,rely=0.2, anchor="center")
                        l2=Label(ther,text="Enter "+v+" name",font=("Arial Bold",25))
                        l2.configure(fg="white",bg="black")
                        l2.place(relx=0.4, rely=0.3, anchor="center")
                        name=Entry(ther,width=25,font=('Arial Bold',20))
                        name.place(relx=0.65,rely=0.3, anchor="center")
                        l3=Label(ther,text="From",font=("Arial Bold",25))
                        l3.configure(fg="white",bg="black")
                        l3.place(relx=0.4, rely=0.4, anchor="center")
                        From=Entry(ther,width=25,font=('Arial Bold',20))
                        From.place(relx=0.65,rely=0.4, anchor="center")
                        l4=Label(ther,text="To",font=("Arial Bold",25))
                        l4.configure(fg="white",bg="black")
                        l4.place(relx=0.4, rely=0.5, anchor="center")
                        To=Entry(ther,width=25,font=('Arial Bold',20))
                        To.place(relx=0.65,rely=0.5, anchor="center")
                        l5=Label(ther,text="Departure Date",font=("Arial Bold",25))
                        l5.configure(fg="white",bg="black")
                        l5.place(relx=0.4, rely=0.6, anchor="center")
                        Dept=Entry(ther,width=25,font=('Arial Bold',20))
                        Dept.place(relx=0.65,rely=0.6, anchor="center")
                        l6=Label(ther,text="Arrival Date",font=("Arial Bold",25))
                        l6.configure(fg="white",bg="black")
                        l6.place(relx=0.4, rely=0.7, anchor="center")
                        Arr=Entry(ther,width=25,font=('Arial Bold',20))
                        Arr.place(relx=0.65,rely=0.7, anchor="center")
                        l7=Label(ther,text="Status",font=("Arial Bold",25))
                        l7.configure(fg="white",bg="black")
                        l7.place(relx=0.4, rely=0.8, anchor="center")
                        Status=Entry(ther,width=25,font=('Arial Bold',20))
                        Status.place(relx=0.65,rely=0.8, anchor="center")
                        but1=Button(ther,text="Confirm",fg="white",bg="black",command=appendit)
                        but1.place(relx = 0.35, rely = 0.9, anchor = 'c')
                        but1['font'] = myFont
                        but2=Button(ther,text="Back",fg="white",bg="black",command=ther.destroy)
                        but2.place(relx = 0.55, rely = 0.9, anchor = 'c')
                        but2['font'] = myFont
                        abc+=1
                    else:
                        aq.append(a)                        
                w+=1                    
            if abc==0:
                messagebox.showinfo("Oops!","None of the "+v+" names match to given name")
            u=open(q,"w")
            wobj=csv.writer(u,delimiter=",")
            for b in aq:
                wobj.writerow(b)
            u.close()

        cc=aavc.get()
        w12.append(cc)                    
        fna=w12[0]
        abcd=0
        for m in d:
            if m[0]==fna:
                v=m[1]
                abcd+=1
        if abcd==0:
                messagebox.showinfo("Oops!","None of the chart names match to given name")
                w12.pop()
        else:
            try:
                adminportal.destroy()      
            except:
                try:
                    cav.destroy()
                except:
                    print()
                    
            global the
            aav.destroy() 
            the=Tk()
            the.attributes('-fullscreen',True)
            the.title("Updating the Chart")
            myFont = font.Font(size=25)
            Coverphoto=PhotoImage(file="Coverphoto1.png")
            label2=Label(the,image=Coverphoto)
            label2.place(relx = 0.5,rely = 0.5, anchor ='center')
            label2.image = Coverphoto
            label2.pack
            photo=PhotoImage(file="project.png")
            label=Label(the,image=photo)
            label.place(relx = 0.94,rely = 0.1, anchor ='center')
            label.image = photo
            label.pack
            lt=Label(the,text="Updating the Chart",font=("Arial Bold",45))
            lt.configure(fg="white",bg="black")
            lt.place(relx=0.5, rely=0.04, anchor="center")
            l=Label(the,text="Enter the name of the Vehicle ",font=("Arial Bold",25))
            l.configure(fg="white",bg="black")
            l.place(relx=0.4, rely=0.5, anchor="center")
            checkname=Entry(the,width=25,font=('Arial Bold',20))
            checkname.place(relx=0.7,rely=0.5, anchor="center")
            cn=checkname.get()
            but1=Button(the,text="Confirm",fg="white",bg="black",command=stillcheck)
            but1.place(relx = 0.35, rely = 0.6, anchor = 'c')
            but1['font'] = myFont
            but2=Button(the,text="Back",fg="white",bg="black",command=start2)
            but2.place(relx = 0.55, rely = 0.6, anchor = 'c')
            but2['font'] = myFont
                       
    try:
        Railwaysportal.destroy()
    except:
        try:
            Roadwaysportal.destroy()
        except:
            try:
                Airwaysportal.destroy()
            except:
                print()

    global aav               
    aav=Tk()
    aav.attributes('-fullscreen',True)
    aav.title("Updating the Chart")
    myFont = font.Font(size=25) 
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(aav,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack    
    photo=PhotoImage(file="project.png")
    label=Label(aav,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l1=Label(aav,text="Updating the Chart",font=("Arial Bold",45))
    l1.configure(fg="white",bg="black")
    l1.place(relx=0.5, rely=0.04, anchor="center")
    l2=Label(aav,text="Enter the Chart",font=("Arial Bold",25))
    l2.configure(fg="white",bg="black")
    l2.place(relx=0.4, rely=0.5, anchor="center")
    aavc=Entry(aav,width=25,font=('Arial Bold',20))
    aavc.place(relx=0.6,rely=0.5, anchor="center")
    but1=Button(aav,text="Confirm",fg="white",bg="black",command=check)
    but1.place(relx = 0.35, rely = 0.6, anchor = 'c')
    but1['font'] = myFont
    but2=Button(aav,text="Back",fg="white",bg="black",command=start1)
    but2.place(relx = 0.55, rely = 0.6, anchor = 'c')
    but2['font'] = myFont
                                                                          
def put_chart():
    ott=[]
    def puttingchart():
        
        def appendit():
            
            def morea():
                if ch.get()=="Yes":
                    ther.destroy()
                    puttingchart()
                else:
                    q=fna+".csv"
                    f=open(q,"w")
                    w=0
                    wobj=csv.writer(f,delimiter=",")
                    for i in range(len(ott)):
                        if w%2==0:          
                            wobj.writerow(ott[i])
                        w+=1
                    f.flush()
                    f.close()
                    messagebox.showinfo("Sucess","You just finished putting the "+fna+" Chart")
                    ther.destroy()
                    aav.destroy()
                    
            ott.append([numberu.get(),name.get(),From.get(),To.get(),Dept.get(),Arr.get(),Status.get()])
            l1=Label(ther,text="Do you want to add more "+v+" ?Give Yes or No",font=("Arial Bold",25))
            l1.configure(fg="Black",bg="Light Pink")
            l1.place(relx=0.4, rely=0.1, anchor="center")
            ch=Entry(ther,width=25,font=('Arial Bold',20))
            ch.place(relx=0.78,rely=0.1, anchor="center")
            but1=Button(ther,text="Confirm",fg="yellow",bg="Blue",command=morea)
            but1.place(relx = 0.95, rely = 0.1, anchor = 'c')
            but1['font']=myFont
            
        fna= aavc.get()
        abc=0           
        for m in d:
            if m[0]==fna:
                v=m[1]
                abc+=1
        print(abc)
        if abc==0:
                messagebox.showinfo("Oops!","None of the chart names match to given name")
        else:                
            ther=Tk()
            ther.attributes('-fullscreen',True)
            ther.title("Putting the Chart")
            ther.configure(bg ="Light Blue")
            l=Label(ther,text="Enter the Details",font=("Arial Bold",45))
            l.configure(fg="white",bg="black")
            l.place(relx=0.45, rely=0.05, anchor="center")        
            l1=Label(ther,text="Enter "+v+" number",font=("Arial Bold",25))
            l1.configure(fg="white",bg="black")
            l1.place(relx=0.4, rely=0.2, anchor="center")
            numberu=Entry(ther,width=25,font=('Arial Bold',20))
            numberu.place(relx=0.65,rely=0.2, anchor="center")
            l2=Label(ther,text="Enter "+v+" name",font=("Arial Bold",25))
            l2.configure(fg="white",bg="black")
            l2.place(relx=0.4, rely=0.3, anchor="center")
            name=Entry(ther,width=25,font=('Arial Bold',20))
            name.place(relx=0.65,rely=0.3, anchor="center")
            l3=Label(ther,text="From",font=("Arial Bold",25))
            l3.configure(fg="white",bg="black")
            l3.place(relx=0.4, rely=0.4, anchor="center")
            From=Entry(ther,width=25,font=('Arial Bold',20))
            From.place(relx=0.65,rely=0.4, anchor="center")
            l4=Label(ther,text="To",font=("Arial Bold",25))
            l4.configure(fg="white",bg="black")
            l4.place(relx=0.4, rely=0.5, anchor="center")
            To=Entry(ther,width=25,font=('Arial Bold',20))
            To.place(relx=0.65,rely=0.5, anchor="center")
            l5=Label(ther,text="Departure Date",font=("Arial Bold",25))
            l5.configure(fg="white",bg="black")
            l5.place(relx=0.4, rely=0.6, anchor="center")
            Dept=Entry(ther,width=25,font=('Arial Bold',20))
            Dept.place(relx=0.65,rely=0.6, anchor="center")
            l6=Label(ther,text="Arrival Date",font=("Arial Bold",25))
            l6.configure(fg="white",bg="black")
            l6.place(relx=0.4, rely=0.7, anchor="center")
            Arr=Entry(ther,width=25,font=('Arial Bold',20))
            Arr.place(relx=0.65,rely=0.7, anchor="center")
            l7=Label(ther,text="Status",font=("Arial Bold",25))
            l7.configure(fg="white",bg="black")
            l7.place(relx=0.4, rely=0.8, anchor="center")
            Status=Entry(ther,width=25,font=('Arial Bold',20))
            Status.place(relx=0.65,rely=0.8, anchor="center")
            but1=Button(ther,text="Confirm",fg="white",bg="black",command=appendit)
            but1.place(relx = 0.35, rely = 0.9, anchor = 'c')
            but1['font']=myFont
            but2=Button(ther,text="Back",fg="white",bg="black",command=ther.destroy)
            but2.place(relx = 0.55, rely = 0.9, anchor = 'c')
            but2['font']=myFont
    try:
        Railwaysportal.destroy()
    except:
        try:
            Roadwaysportal.destroy()
        except:
            try:
                Airwaysportal.destroy()
            except:
                print()
                
    global aav
    aav=Tk()
    aav.attributes('-fullscreen',True)
    aav.title("Putting the Chart")
    aav.configure(bg ="Light pink")
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(aav,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack    
    photo=PhotoImage(file="project.png")
    label=Label(aav,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l1=Label(aav,text="Putting the Chart",font=("Arial Bold",45))
    l1.configure(fg="white",bg="black")
    l1.place(relx=0.5, rely=0.04, anchor="center")
    l2=Label(aav,text="Enter the Chart",font=("Arial Bold",25))
    l2.configure(fg="white",bg="black")
    l2.place(relx=0.4, rely=0.5, anchor="center")
    aavc=Entry(aav,width=25,font=('Arial Bold',20))
    aavc.place(relx=0.6,rely=0.5, anchor="center")
    but1=Button(aav,text="Confirm",fg="white",bg="black",command=puttingchart)
    but1.place(relx = 0.35, rely = 0.6, anchor = 'c')
    but1['font']=myFont
    but2=Button(aav,text="Back",fg="white",bg="black",command=start1)
    but2.place(relx = 0.55, rely = 0.6, anchor = 'c')
    but2['font']=myFont
    
def add_a_Vehicle():

    def addingvehicle():
        
        def addda():
            q=fna+".csv"
            f=open(q,"a")
            w=0
            wobj=csv.writer(f,delimiter=",")
            wobj.writerow([numberu.get(),name.get(),From.get(),To.get(),Dept.get(),Arr.get(),Status.get()])
            f.flush()
            f.close()
            messagebox.showinfo("Sucess","The "+v+" Was added to the chart")

        abc=0            
        fna= aavc.get()
        for m in d:
            if m[0]==fna:
                v=m[1]
                abc+=1
        if abc==0:
            messagebox.showinfo("Oops!","None of the chart names match to given name")            
        else:                
            ther=Tk()
            ther.attributes('-fullscreen',True)
            ther.title("Add a "+v)
            ther.configure(bg ="Light Blue")
            l=Label(ther,text="Enter the Details",font=("Arial Bold",45))
            l.configure(fg="white",bg="black")
            l.place(relx=0.5, rely=0.05, anchor="center")        
            l1=Label(ther,text="Enter "+v+" number",font=("Arial Bold",25))
            l1.configure(fg="white",bg="black")
            l1.place(relx=0.4, rely=0.2, anchor="center")
            numberu=Entry(ther,width=25,font=('Arial Bold',20))
            numberu.place(relx=0.65,rely=0.2, anchor="center")
            l2=Label(ther,text="Enter "+v+" name",font=("Arial Bold",25))
            l2.configure(fg="white",bg="black")
            l2.place(relx=0.4, rely=0.3, anchor="center")
            name=Entry(ther,width=25,font=('Arial Bold',20))
            name.place(relx=0.65,rely=0.3, anchor="center")
            l3=Label(ther,text="From",font=("Arial Bold",25))
            l3.configure(fg="white",bg="black")
            l3.place(relx=0.4, rely=0.4, anchor="center")
            From=Entry(ther,width=25,font=('Arial Bold',20))
            From.place(relx=0.65,rely=0.4, anchor="center")
            l4=Label(ther,text="To",font=("Arial Bold",25))
            l4.configure(fg="white",bg="black")
            l4.place(relx=0.4, rely=0.5, anchor="center")
            To=Entry(ther,width=25,font=('Arial Bold',20))
            To.place(relx=0.65,rely=0.5, anchor="center")
            l5=Label(ther,text="Departure Date",font=("Arial Bold",25))
            l5.configure(fg="white",bg="black")
            l5.place(relx=0.4, rely=0.6, anchor="center")
            Dept=Entry(ther,width=25,font=('Arial Bold',20))
            Dept.place(relx=0.65,rely=0.6, anchor="center")
            l6=Label(ther,text="Arrival Date",font=("Arial Bold",25))
            l6.configure(fg="white",bg="black")
            l6.place(relx=0.4, rely=0.7, anchor="center")
            Arr=Entry(ther,width=25,font=('Arial Bold',20))
            Arr.place(relx=0.65,rely=0.7, anchor="center")
            l7=Label(ther,text="Status",font=("Arial Bold",25))
            l7.configure(fg="white",bg="black")
            l7.place(relx=0.4, rely=0.8, anchor="center")
            Status=Entry(ther,width=25,font=('Arial Bold',20))
            Status.place(relx=0.65,rely=0.8, anchor="center")
            but1=Button(ther,text="Confirm",fg="white",bg="black",command=addda)
            but1.place(relx = 0.35, rely = 0.9, anchor = 'c')
            but1['font']=myFont
            but2=Button(ther,text="Back",fg="white",bg="black",command=ther.destroy)
            but2.place(relx = 0.55, rely = 0.9, anchor = 'c')
            but2['font']=myFont
            
    try:
        Railwaysportal.destroy()
    except:
        try:
            Roadwaysportal.destroy()
        except:
            try:
                Airwaysportal.destroy()
            except:
                print()
        
    global aav           
    aav=Tk()
    aav.attributes('-fullscreen',True)
    aav.title("Add a vehicle")
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(aav,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack    
    photo=PhotoImage(file="project.png")
    label=Label(aav,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l1=Label(aav,text="Adding a vehicle",font=("Arial Bold",45))
    l1.configure(fg="white",bg="black")
    l1.place(relx=0.5, rely=0.04, anchor="center")
    l2=Label(aav,text="Enter the Chart",font=("Arial Bold",25))
    l2.configure(fg="white",bg="black")
    l2.place(relx=0.4, rely=0.5, anchor="center")
    aavc=Entry(aav,width=25,font=('Arial Bold',20))
    aavc.place(relx=0.6,rely=0.5, anchor="center")
    but1=Button(aav,text="Confirm",fg="white",bg="black",command=addingvehicle)
    but1.place(relx = 0.35, rely = 0.6, anchor = 'c')
    but1['font']=myFont
    but2=Button(aav,text="Back",fg="white",bg="black",command=start1)
    but2.place(relx = 0.55, rely = 0.6, anchor = 'c')
    but2['font']=myFont 
       
def cancel_a_Vehicle():

    def cancelvehicle():

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
                   messagebox.showinfo("Sucess","Sucessfully cancelled the "+v)
                c+=1
            f.close()
            
            j=open(q,"w")
            wobj=csv.writer(j,delimiter=",")
            for h in s:
                wobj.writerow(h)
            j.close()
            
        abc=0        
        fna=aavc.get() 
        for m in d:
            if m[0]==fna:
                v=m[1]
                abc+=1
        if abc==0:
            messagebox.showinfo("Oops!","None of the chart names match to given name")
        else:
            ca1v.destroy()
            cv=Tk()
            cv.title("Cancel a "+v+" from "+fna+" Chart")
            cv.attributes('-fullscreen',True)
            myFont = font.Font(size=20)
            Coverphoto=PhotoImage(file="Coverphoto1.png")
            label2=Label(cv,image=Coverphoto)
            label2.place(relx = 0.5,rely = 0.5, anchor ='center')
            label2.image = Coverphoto
            label2.pack    
            photo=PhotoImage(file="project.png")
            label=Label(cv,image=photo)
            label.place(relx = 0.94,rely = 0.1, anchor ='center')
            label.image = photo
            label.pack
            l=Label(cv,text="Cancelling a "+v,font=("Arial Bold",45))
            l.configure(fg="white",bg="black")
            l.place(relx=0.45, rely=0.05, anchor="center")        
            ll=Label(cv,text="Enter the "+v+" Name",font=("Arial Bold",25))
            ll.configure(fg="white",bg="black")
            ll.place(relx=0.2, rely=0.4, anchor="center")
            cvname=Entry(cv,width=25,font=('Arial Bold',25))
            cvname.place(relx=0.5,rely=0.4, anchor="center")
            but1=Button(cv,text="Confirm",fg="white",bg="black",command=c_v_n)
            but1.place(relx = 0.3, rely = 0.5, anchor = 'c')
            but1['font']=myFont
            but2=Button(cv,text="Back",fg="white",bg="black",command=start2)
            but2.place(relx = 0.5, rely = 0.5, anchor = 'c')
            but2['font']=myFont

    try:
        Railwaysportal.destroy()
    except:
        try:
            Roadwaysportal.destroy()
        except:
            try:
                Airwaysportal.destroy()
            except:
                print()
        
    global ca1v                 
    ca1v=Tk()
    ca1v.attributes('-fullscreen',True)
    ca1v.title("Cancel a vehicle")
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(ca1v,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack    
    photo=PhotoImage(file="project.png")
    label=Label(ca1v,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l1=Label(ca1v,text="Cancelling a vehicle",font=("Arial Bold",45))
    l1.configure(fg="white",bg="black")
    l1.place(relx=0.5, rely=0.04, anchor="center")
    l2=Label(ca1v,text="Enter the Chart",font=("Arial Bold",25))
    l2.configure(fg="white",bg="black")
    l2.place(relx=0.4, rely=0.5, anchor="center")
    aavc=Entry(ca1v,width=25,font=('Arial Bold',20))
    aavc.place(relx=0.6,rely=0.5, anchor="center")
    but1=Button(ca1v,text="Confirm",fg="white",bg="black",command=cancelvehicle)
    but1.place(relx = 0.35, rely = 0.6, anchor = 'c')
    but1['font']=myFont
    but2=Button(ca1v,text="Back",fg="white",bg="black",command=start2)
    but2.place(relx = 0.55, rely = 0.6, anchor = 'c')
    but2['font']=myFont
        
def showpaslist():
    
    def show_chart():
        
        class Table:
            
            def __init__(self,root):
                c=0         
                for i in range(10,total_rows+10):
                    if c%2==0:
                        for j in range(10,total_columns+10):
                            self.e = Entry(root, width=17, fg='blue', 
                                            font=('Arial',16,'bold'))                   
                            self.e.grid(row=i+1,column=j+1)
                            self.e.insert(END, e[i-10][j-10])
                    c+=1

        fna=vname.get()
        q=fna+".csv"
        r=fna+"Chart"
        f=open(q,"r")
        f.seek(0)
        robj=csv.reader(f,delimiter=",")
        e=list(robj)
        print(e)
        total_rows = len(e) 
        total_columns = len(e[0])
        f.close()
        for m in d:
            if m[0]==fna:
                j=m[1]            
        root = Tk()
        root.attributes('-fullscreen',True)
        root.title(fna+" chart")
        myFont = font.Font(size=20)               
        root.configure(bg ="Light Blue")
        l1=Label(root,text=fna+" Chart",font=("Arial Bold",45))
        l1.configure(fg="Black",bg="Light Blue")
        l1.place(relx=0.5, rely=0.04, anchor="center")            
        goq='Name  \t Age\t\tGender\t\tClass\t  Seat Number'
        l2=Label(root,text=goq,font=("Arial Bold",20))
        l2.configure(fg="Black",bg="Light Blue")
        l2.place(relx=0.33, rely=0.15, anchor="center")
        for r in range(9):
            bi=Label(root,text="   ",bg="Light Blue")
            bi.grid(row=r,column=0)
        but1=Button(root,text="Back",fg="White",bg="Black",command=root.destroy)
        but1.place(relx = 0.5, rely = 0.8, anchor = 'c',)
        but1['font'] = myFont
        t = Table(root)
        root.mainloop()

    try:
        Railwaysportal.destroy()
    except:
        try:
            Roadwaysportal.destroy()
        except:
            try:
                Airwaysportal.destroy()
            except:
                print()
        
    global paslist       
    paslist=Tk()
    paslist.attributes('-fullscreen',True)
    paslist.title("Cancel a vehicle")               
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(paslist,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack    
    photo=PhotoImage(file="project.png")
    label=Label(paslist,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l1=Label(paslist,text="Passenger List",font=("Arial Bold",45))
    l1.configure(fg="White",bg="Black")
    l1.place(relx=0.5, rely=0.04, anchor="center")
    l2=Label(paslist,text="Enter the vehicle's name",font=("Arial Bold",25))
    l2.configure(fg="White",bg="Black")
    l2.place(relx=0.25, rely=0.5, anchor="center")
    vname=Entry(paslist,width=25,font=('Arial Bold',20))
    vname.place(relx=0.6,rely=0.5, anchor="center")
    but1=Button(paslist,text="Back",fg="White",bg="Black",command=start2)
    but1.place(relx = 0.6, rely = 0.6, anchor = 'c',)
    but1['font'] = myFont
    but2=Button(paslist,text="Submit",fg="White",bg="Black",command=show_chart)
    but2.place(relx = 0.4, rely = 0.6, anchor = 'c',)
    but2['font'] = myFont
            
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

    try:
        adminportal.destroy()
    except:
        try:
            cav.destroy()
        except:
            print()
        
    global deladmin    
    deladmin=Tk()
    deladmin.title("Delete an Admin")
    deladmin.attributes('-fullscreen',True)
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(deladmin,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack    
    photo=PhotoImage(file="project.png")
    label=Label(deladmin,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l=Label(deladmin,text="Deleting an Admin",font=("Arial Bold",45))
    l.configure(fg="white",bg="black")
    l.place(relx=0.5, rely=0.1, anchor="center")
    ll=Label(deladmin,text="Enter admin name to be deleted",font=("Arial Bold",25))
    ll.configure(fg="white",bg="black")
    ll.place(relx=0.2, rely=0.4, anchor="center")
    deladname=Entry(deladmin,width=25,font=('Arial Bold',20))
    deladname.place(relx=0.6,rely=0.4, anchor="center")
    but1=Button(deladmin,text="Confirm",fg="white",bg="black",command=deladinput)
    but1.place(relx = 0.3, rely = 0.5, anchor = 'c')
    but1['font'] = myFont 
    but2=Button(deladmin,text="Back",fg="white",bg="black",command=start1)
    but2.place(relx = 0.4 ,rely = 0.5, anchor = 'c')
    but2['font'] = myFont
    
def addadmin():
    
    def addidpass():
        e1=[]
        user=addadname.get()
        passw=addadnamep.get()
        e1.append(user)
        e1.append(passw)
        adminku.append(e1)
        messagebox.showinfo("Sucess","Admin Added Sucessfully")

    try:
        adminportal.destroy()      
    except:
        try:
            cav.destroy()
        except:
            print()
        
    global addadmin
    addadmin=Tk()
    addadmin.title("Add an Admin")
    addadmin.attributes('-fullscreen',True)
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(addadmin,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack    
    photo=PhotoImage(file="project.png")
    label=Label(addadmin,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l=Label(addadmin,text="Adding an Admin",font=("Arial Bold",45))
    l.configure(fg="white",bg="black")
    l.place(relx=0.5,rely=0.1, anchor="center")        
    l3=Label(addadmin,text="Enter the Required Credentials",font=("Arial Bold",30))###
    l3.configure(fg="white",bg="black")
    l3.place(relx=0.5,rely=0.2, anchor="center")
    ll=Label(addadmin,text="Enter admin name to be added",font=("Arial Bold",25))
    ll.configure(fg="white",bg="black")
    ll.place(relx=0.3, rely=0.4, anchor="center")
    addadname=Entry(addadmin,width=25,font=('Arial Bold',20))
    addadname.place(relx=0.6,rely=0.4, anchor="center")
    l2=Label(addadmin,text="Enter admin password to be added",font=("Arial Bold",25))
    l2.configure(fg="white",bg="black")
    l2.place(relx=0.3, rely=0.6, anchor="center")
    addadnamep=Entry(addadmin,width=25,font=('Arial Bold',20))
    addadnamep.place(relx=0.6,rely=0.6, anchor="center")
    but1=Button(addadmin,text="Confirm",fg="white",bg="black",command=addidpass)
    but1.place(relx = 0.4 ,rely = 0.7, anchor = 'c')
    but1['font'] = myFont 
    but2=Button(addadmin,text="Back",fg="white",bg="black",command=start1)
    but2.place(relx = 0.5 ,rely = 0.7, anchor = 'c')
    but2['font'] = myFont       
   
def Admin_portal():
        
    def Airways_portal():

        def show_chart():
            
            class Table:
                
                def __init__(self,root):
                    c=0        
                    for i in range(10,total_rows+10):
                        if c%2==0:
                            for j in range(10,total_columns+10):
                                self.e = Entry(root, width=17, fg='blue', 
                                               font=('Arial',16,'bold'))                   
                                self.e.grid(row=i+1,column=j+1)
                                self.e.insert(END, e[i-10][j-10])
                        c+=1

            fna='Airways'
            q=fna+".csv"
            r=fna+"portal"
            f=open(q,"r")
            f.seek(0)
            robj=csv.reader(f,delimiter=",")
            e=list(robj)
            total_rows = len(e) 
            total_columns = len(e[0])
            f.close()
            for m in d:
                if m[0]==fna:
                    j=m[1]            
            root = Tk()
            root.attributes('-fullscreen',True)
            root.title(fna+" chart")
            myFont = font.Font(size=20)               
            root.configure(bg ="Light blue")
            l1=Label(root,text="Available "+j+"s",font=("Arial Bold",40))
            l1.configure(fg="Black",bg="Light Blue")
            l1.place(relx=0.5, rely=0.04, anchor="center")            
            goq='Flight No.  \t  Flight Name\t  Origin\t\tDestination\t  Departure\t    Arrival\t\tStatus'
            l2=Label(root,text=goq,font=("Arial Bold",20))
            l2.configure(fg="Black",bg="Light Blue")
            l2.place(relx=0.43, rely=0.15, anchor="center")
            for r in range(9):
                bi=Label(root,text="   ",bg="Light blue")
                bi.grid(row=r,column=0)
            but1=Button(root,text="Back",fg="White",bg="Black",command=root.destroy)
            but1.place(relx = 0.5, rely = 0.8, anchor = 'c',)
            but1['font'] = myFont
            t = Table(root)
            root.mainloop()

        try:
            adminportal.destroy()      
        except:
            try:
                cav.destroy()
            except:
                print()
        
        global Airwaysportal                                           
        Airwaysportal=Tk()
        Airwaysportal.title("Airways portal")
        Airwaysportal.attributes('-fullscreen',True)
        myFont = font.Font(size=20)
        Coverphoto=PhotoImage(file="1307258.png")
        label2=Label(Airwaysportal,image=Coverphoto)
        label2.place(relx = 0.5,rely = 0.5, anchor ='center')
        label2.image = Coverphoto
        label2.pack    
        photo=PhotoImage(file="project.png")
        label=Label(Airwaysportal,image=photo)
        label.place(relx = 0.94,rely = 0.1, anchor ='center')
        label.image = photo
        label.pack    
        l1=Label(Airwaysportal,text="Airways Portal",font=("Arial Bold",45))
        l1.configure(fg="White",bg="Black")
        l1.place(relx=0.5, rely=0.07, anchor="center")
        bt1=Button(Airwaysportal,text="Show scheduled flight chart",fg="white",bg="black",command=show_chart)
        bt1.place(relx = 0.5, rely = 0.3, anchor = 'c')
        bt1['font'] = myFont 
        bt2=Button(Airwaysportal,text="Add a flight",fg="white",bg="black",command=add_a_Vehicle)
        bt2.place(relx = 0.5, rely = 0.4, anchor = 'c')
        bt2['font'] = myFont 
        bt3=Button(Airwaysportal,text="Cancel a flight",fg="white",bg="black",command=cancel_a_Vehicle)
        bt3.place(relx = 0.5, rely = 0.5, anchor = 'c')
        bt3['font'] = myFont  
        bt4=Button(Airwaysportal,text="Update the chart",fg="white",bg="black",command=update_chart)
        bt4.place(relx = 0.5, rely = 0.6, anchor = 'c')
        bt4['font'] = myFont 
        bt5=Button(Airwaysportal,text="Cancel all flights",fg="white",bg="black",command=cav)
        bt5.place(relx = 0.5, rely = 0.7, anchor = 'c')
        bt5['font'] = myFont 
        bt6=Button(Airwaysportal, text="Put up the chart",fg="white",bg="black",command=put_chart)
        bt6.place(relx = 0.5, rely= 0.2 , anchor='c')
        bt6['font'] = myFont      
        bt7=Button(Airwaysportal,text="Show passenger list",fg="white",bg="black",command=showpaslist)
        bt7.place(relx=0.5,rely=0.8,anchor="center")
        bt7['font'] = myFont         
        bt8=Button(Airwaysportal,text="Back",fg="white",bg="black",command=start1)
        bt8.place(relx=0.5,rely=0.9,anchor="center")
        bt8['font'] = myFont 

    def Roadways_portal():

        def show_chart():
            
            class Table:
                
                def __init__(self,root):
                    c=0        
                    for i in range(10,total_rows+10):
                        if c%2==0:
                            for j in range(10,total_columns+10):
                                self.e = Entry(root, width=17, fg='blue', 
                                               font=('Arial',16,'bold'))                   
                                self.e.grid(row=i+1,column=j+1)
                                self.e.insert(END, e[i-10][j-10])
                        c+=1

            fna='Roadways'
            q=fna+".csv"
            r=fna+"portal"
            f=open(q,"r")
            f.seek(0)
            robj=csv.reader(f,delimiter=",")
            e=list(robj) 
            total_rows = len(e) 
            total_columns = len(e[0])
            f.close()
            for m in d:
                if m[0]==fna:
                    j=m[1]
            goq='Bus No.  \t  Bus Name\t  Origin\t\tDestination\t  Departure\t    Arrival\t\tStatus'
            root = Tk()
            root.attributes('-fullscreen',True)
            root.title(fna+" chart")
            root.configure(bg ="Light Blue")
            myFont = font.Font(size=20)               
            l1=Label(root,text=fna+" Chart",font=("Arial Bold",45))
            l1.configure(fg="Black",bg="Light Blue")
            l1.place(relx=0.5, rely=0.04, anchor="center")
            l2=Label(root,text=goq,font=("Arial Bold",17))
            l2.configure(fg="Black",bg="Light Blue")
            l2.place(relx=0.43, rely=0.15, anchor="center")
            for r in range(9):
                bi=Label(root,text="   ",bg="Light Blue")
                bi.grid(row=r,column=0)
            but1=Button(root,text="Back",fg="White",bg="Black",command=root.destroy)
            but1.place(relx = 0.5, rely = 0.8, anchor = 'c')
            but1['font'] = myFont
            t = Table(root)
            root.mainloop()

        try:
            adminportal.destroy()      
        except:
            try:
                cav.destroy()
            except:
                print()
        
        global Roadwaysportal                                                       
        Roadwaysportal=Tk()
        Roadwaysportal.title("Roadways portal")
        Roadwaysportal.attributes('-fullscreen',True)  
        myFont = font.Font(size=20)
        Coverphoto=PhotoImage(file="Roadw.png")
        label2=Label(Roadwaysportal,image=Coverphoto)
        label2.place(relx = 0.5,rely = 0.5, anchor ='center')
        label2.image = Coverphoto
        label2.pack    
        photo=PhotoImage(file="project.png")
        label=Label(Roadwaysportal,image=photo)
        label.place(relx = 0.94,rely = 0.1, anchor ='center')
        label.image = photo
        label.pack 
        l1=Label(Roadwaysportal,text="Roadways Portal",font=("Arial Bold",45))
        l1.configure(fg="White",bg="Black")
        l1.place(relx=0.5, rely=0.07, anchor="center")
        bt1=Button(Roadwaysportal,text="Show scheduled bus chart",fg="white",bg="black",command=show_chart)
        bt1.place(relx = 0.5, rely = 0.3, anchor = 'c')
        bt1['font'] = myFont 
        bt2=Button(Roadwaysportal,text="Add a bus",fg="white",bg="black",command=add_a_Vehicle)
        bt2.place(relx = 0.5, rely = 0.4, anchor = 'c')
        bt2['font'] = myFont 
        bt3=Button(Roadwaysportal,text="Cancel a bus",fg="white",bg="black",command=cancel_a_Vehicle)
        bt3.place(relx = 0.5, rely = 0.5, anchor = 'c')
        bt3['font'] = myFont 
        bt4=Button(Roadwaysportal,text="Update the chart",fg="white",bg="black",command=update_chart)
        bt4.place(relx = 0.5, rely = 0.6, anchor = 'c')
        bt4['font'] = myFont         
        bt5=Button(Roadwaysportal,text="Cancel all buses",fg="white",bg="black",command=cav)
        bt5.place(relx = 0.5, rely = 0.7, anchor = 'c')
        bt5['font'] = myFont         
        bt6=Button(Roadwaysportal, text="Put up the chart",fg="white",bg="black",command=put_chart)
        bt6.place(relx = 0.5, rely= 0.2 , anchor='c')
        bt6['font'] = myFont         
        bt7=Button(Roadwaysportal,text="Show passenger list",fg="white",bg="black",command=showpaslist)
        bt7.place(relx=0.5,rely=0.8,anchor="center")
        bt7['font'] = myFont         
        bt8=Button(Roadwaysportal,text="Back",fg="white",bg="black",command=start1)
        bt8.place(relx=0.5,rely=0.9,anchor="center")
        bt8['font'] = myFont 

    def Railways_portal():

        def show_chart():
            
            class Table:
                
                def __init__(self,root):
                    c=0        
                    for i in range(10,total_rows+10):
                        if c%2==0:
                            for j in range(10,total_columns+10):
                                self.e = Entry(root, width=17, fg='blue', 
                                              font=('Arial',16,'bold'))                   
                                self.e.grid(row=i+1,column=j+1)
                                self.e.insert(END, e[i-10][j-10])
                        c+=1

            fna='Railways'
            q=fna+".csv"
            r=fna+"portal"
            f=open(q,"r")
            f.seek(0)
            robj=csv.reader(f,delimiter=",")
            e=list(robj)   
            total_rows = len(e) 
            total_columns = len(e[0])
            f.close()
            for m in d:
                if m[0]==fna:
                    j=m[1]
            goq='Train No.  \t  Train Name\t  Origin\t\tDestination\t  Departure\t    Arrival\t\tStatus'
            root = Tk()
            root.attributes('-fullscreen',True)
            root.title(fna+" chart")
            root.configure(bg ="Light blue")
            myFont = font.Font(size=20)
            l1=Label(root,text=fna+" Chart",font=("Arial Bold",45))
            l1.configure(fg="Black",bg="Light blue")
            l1.place(relx=0.5, rely=0.04, anchor="center")
            l2=Label(root,text=goq,font=("Arial Bold",17))
            l2.configure(fg="Black",bg="Light Blue")
            l2.place(relx=0.43, rely=0.15, anchor="center")
            for r in range(9):
                bi=Label(root,text="   ",bg="Light blue")
                bi.grid(row=r,column=0)
            but1=Button(root,text="Back",fg="White",bg="black",command=root.destroy)
            but1.place(relx = 0.5, rely = 0.8, anchor = 'c')
            but1['font'] = myFont
            t = Table(root)
            root.mainloop()

        try:
            adminportal.destroy()      
        except:
            try:
                cav.destroy()
            except:
                print()
        
        global Railwaysportal                                                               
        Railwaysportal=Tk()
        Railwaysportal.title("Railways portal")
        Railwaysportal.attributes('-fullscreen',True)
        myFont = font.Font(size=20)
        Coverphoto=PhotoImage(file="Coverphoto1.png")
        label2=Label(Railwaysportal,image=Coverphoto)
        label2.place(relx = 0.5,rely = 0.5, anchor ='center')
        label2.image = Coverphoto
        label2.pack    
        photo=PhotoImage(file="project.png")
        label=Label(Railwaysportal,image=photo)
        label.place(relx = 0.94,rely = 0.1, anchor ='center')
        label.image = photo
        label.pack 
        l1=Label(Railwaysportal,text="Railways Portal",font=("Arial Bold",45))
        l1.configure(fg="white",bg="black")
        l1.place(relx=0.5, rely=0.07, anchor="center")   
        bt1=Button(Railwaysportal,text="Show scheduled train chart",fg="white",bg="black",command=show_chart)
        bt1.place(relx = 0.5, rely = 0.3, anchor = 'c')
        bt1['font'] = myFont 
        bt2=Button(Railwaysportal,text="Add a train",fg="white",bg="black",command=add_a_Vehicle)
        bt2.place(relx = 0.5, rely = 0.4, anchor = 'c')
        bt2['font'] = myFont
        bt3=Button(Railwaysportal,text="Cancel a train",fg="white",bg="black",command=cancel_a_Vehicle)
        bt3.place(relx = 0.5, rely = 0.5, anchor = 'c')
        bt3['font'] = myFont
        bt4=Button(Railwaysportal,text="Update the chart",fg="white",bg="black",command=update_chart)
        bt4.place(relx = 0.5, rely = 0.6, anchor = 'c')
        bt4['font'] = myFont 
        bt5=Button(Railwaysportal,text="Cancel all trains",fg="white",bg="black",command=cav)
        bt5.place(relx = 0.5, rely = 0.7, anchor = 'c')
        bt5['font'] = myFont
        bt6=Button(Railwaysportal, text="Put up the chart",fg="white",bg="black",command=put_chart)
        bt6.place(relx = 0.5, rely= 0.2 , anchor='c')
        bt6['font'] = myFont
        bt7=Button(Railwaysportal,text="Show passenger list",fg="white",bg="black",command=showpaslist)
        bt7.place(relx=0.5,rely=0.8,anchor="center")
        bt7['font'] = myFont
        bt8=Button(Railwaysportal,text="Back",fg="white",bg="black",command=start1)
        bt8.place(relx=0.5,rely=0.9,anchor="center")
        bt8['font'] = myFont

    try:
        adminwindow.destroy()
    except:
        try:
            window1.destroy()
        except:
            print()
        
    global adminportal    
    adminportal=Tk()
    adminportal.title("Admin portal")
    adminportal.attributes('-fullscreen',True)
    myFont = font.Font(size=25) 
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(adminportal,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(adminportal,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l1=Label(adminportal,text="Admin Portal",font=("Arial Bold",45))
    l1.configure(fg="white",bg="black")
    l1.place(relx=0.5, rely=0.07, anchor="center")
    bu1=Button(adminportal,text="Enter Railways Portal",fg="white",bg="black",command=Railways_portal)
    bu1.place(relx = 0.5, rely = 0.4, anchor = 'c')
    bu1['font'] = myFont 
    bu2=Button(adminportal,text="Enter Roadways Portal",fg="white",bg="black",command=Roadways_portal)
    bu2.place(relx = 0.5, rely = 0.55, anchor = 'c')
    bu2['font'] = myFont  
    bu3=Button(adminportal,text="Enter Airways Portal",fg="white",bg="black",command=Airways_portal)
    bu3.place(relx = 0.5, rely = 0.7, anchor = 'c')
    bu3['font'] = myFont 
    bu4=Button(adminportal,text="Add an Admin",fg="white",bg="black",command=addadmin)
    bu4.place(relx = 0.1, rely = 0.9, anchor = 'c')
    bu4['font'] = myFont 
    bu5=Button(adminportal,text="Delete an Admin",fg="white",bg="black",command=deladmin)
    bu5.place(relx = 0.9, rely = 0.9, anchor = 'c')
    bu5['font'] = myFont 
    bu6=Button(adminportal,text="Exit Admin Portal",fg="white",bg="black",command=start)
    bu6.place(relx = 0.5, rely = 0.9, anchor = 'c')
    bu6['font'] = myFont 

def Admin_id():
        
    def adminidpassword():
        c=0
        num1=username.get()
        num2=password.get()
        for i in range(len(adminku)):
            if num1 in adminku[i][0] and num2 in adminku[i][1]:
                c+=1
        if c==1:
            Admin_portal()
        else: 
            messagebox.showinfo("Attention","Invalid Username or Password!")
            
    try:
        window.destroy()
    except:
        try:
            cav.destroy()
        except:
            print()
        
    global adminwindow  
    adminwindow=Tk()
    adminwindow.title("Admin login")
    adminwindow.attributes('-fullscreen',True)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    myFont = font.Font(size=25)
    label2=Label(adminwindow,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack   
    photo=PhotoImage(file="project.png")
    label=Label(adminwindow,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l4=Label(adminwindow,text="Enter required credentials to enter the portal",font=("Arial",30))
    l4.configure(fg="white",bg="black")
    l4.place(relx=0.55,rely=0.2,anchor="center")
    l2=Label(adminwindow,text="Username",font=("Arial Bold",25))
    l2.place(relx=0.4,rely=0.4,anchor="center")
    l2.configure(fg="white",bg="black")
    username=Entry(adminwindow,width=25,font=('Arial Bold',20))
    username.place(relx=0.6,rely=0.4,anchor="center")
    l3=Label(adminwindow,text="Password",font=("Arial Bold",25))
    l3.configure(fg="white",bg="black")
    l3.place(relx=0.4,rely=0.45,anchor="center")
    password=Entry(adminwindow,show="*",width=25,font=('Arial Bold',20))
    password.place(relx=0.6,rely=0.45,anchor="center")    
    bt6=Button(adminwindow,text="Submit",fg="white",bg="black",command=adminidpassword)
    bt6.place(relx=0.55,rely=0.6,anchor="center")
    bt6['font'] = myFont 
    bt7=Button(adminwindow,text="Back",fg="white",bg="black",command=start)
    bt7.place(relx=0.65,rely=0.6,anchor="center")
    bt7['font'] = myFont
      
def About_us():
    
    def destroy_text():        
        T.destroy()
        button.destroy()
    a="""MRF stands for Move Run Fly, matching to the modes of transport; the Railways,Roadways and the Airways.
We,here, provide booking platform for researving your tickets for your breathtaking journey round the world, at
mindblowing discounted rates.
MRF was found by Mr.K.Rakesh, who was suceeded by his son, Mr.R Suresh,the current CEO of MRF.
Your complaints and queries are most welcomed and  can be addressed to us.
Contact us @ mrfbkssd@gmail.com or Phone 3535024024
A project by- K.Devadarshan
                      K.Srijith
                      Syed Ameen
                      12 F2"""            
    myFont = font.Font(size=20)
    T = Text(window, height=10, width=100)
    T.pack()
    T.insert(END, a)
    T['font']=myFont     
    button = Button(window, text='Close',fg="White",bg="Black",command=destroy_text)
    button.place(relx=0.9,rely=0.4,anchor="center")
    button['font'] = myFont
          
def ITSHOW():

    def itroadways():
        def destroy_text():
            T.destroy()
            button.destroy()
        a="""A bus (contracted from omnibus, with variants multibus, motorbus, autobus, etc.) is a road vehicle designed to carry many passengers.
* Buses can have a capacity as high as 300 passengers.[2] The most common type is the single-deck rigid bus, with larger loads carried by double-decker and articulated buses, and smaller loads carried by midibuses and minibuses while coaches are used for longer-distance services.
* Many types of buses, such as city transit buses and inter-city coaches, charge a fare. Other types, such as elementary or secondary school buses or shuttle buses within a post-secondary education campus do not charge a fare. In many jurisdictions, bus drivers require a special licence above and beyond a regular drivers licence.Buses may be used for scheduled bus transport, scheduled coach transport, school transport, private hire, or tourism;
promotional buses may be used for political campaigns and others are privately operated for a wide range of purposes, including rock and pop band tour vehicles. """
        myFont = font.Font(size=20)
        T = Text(itshow, height=10, width=100)
        T.pack()
        T.insert(END, a)
        T['font']=myFont    
        button = Button(itshow, text='Close',fg="White",bg="Black", command=destroy_text)
        button.place(relx=0.9,rely=0.4,anchor="center")
        button['font'] = myFont
        
    def itrailways():
        def destroy_text():
            T.destroy()
            button.destroy()
        a="""Indian Railways (IR) is Indias national railway system operated by the Ministry of Railways.
* It is run by the government as a public good and manages the fourth largest railway network in the world by size, with a route length of 68,155 km (42,350 mi) as of March 2019. 39,866 km (24,772 mi) or 58.49% of all the routes are electrified with 25 kV 50 Hz AC electric traction as of 1 April 2020.
* In the fiscal year ending March 2019, IR carried 844 crore (8.44 billion) passengers and transported 123 crore (1.23 billion) tonnes of freight.
* IR runs 13,523 passenger trains daily, on both long-distance and suburban routes, covering 7,321 stations across India.
* Mail or Express trains, the most common types, run at an average speed of 50.6 km/h (31.4 mph).
* Suburban EMUs run at an average speed of 37.5 km/h (23.3 mph).
* Ordinary Passenger Trains (incl. mixed) run at an average speed of 33.5 km/h (20.8 mph).
* Maximum speed of passenger trains varies with the Vande Bharat Express running at the peak speed of 180 km/h (110 mph).
* In the freight segment, IR runs more than 9,146 trains daily.
* The average speed of freight trains is around 24 km/h (15 mph). Maximum speed of freight trains varies from 60 to 75 km/h (37 to 47 mph) depending on their axle load with "container special" trains running at a peak speed of 100 km/h (62 mph).
* As of March 2019, Indian Railways rolling stock consisted of 289,185 freight wagons, 74,003 passenger coaches and 12,147 locomotives.
* IR owns locomotive and coach-production facilities at several locations in India.
* Being the worlds eighth-largest employer, it had 1.227 million employees as of March 2019.
* The government has committed to electrify its entire rail network by 2023-24, and become a "net-zero railway" by 2030"""
        myFont = font.Font(size=20)
        T = Text(itshow, height=10, width=100)
        T.pack()
        T.insert(END, a)
        T['font']=myFont
        button = Button(itshow, text='Close',fg="White",bg="Black", command=destroy_text)
        button.place(relx=0.9,rely=0.4,anchor="center")
        button['font'] = myFont    
    
    def itairways():
        
        def destroy_text():
            T.destroy()
            button.destroy()            

        a="""Indian Airlines, later Indian, was a major Indian airline based in Delhi and focused primarily on domestic routes, along with several international services to neighbouring countries in Asia.
* It was state-owned after merger of eight pre-Independence domestic airlines and was administered by the Ministry of Civil Aviation.
* Indian was one of the two flag carriers of India, the other being Air India.On 7 December 2005, the airline was rebranded as Indian for advertising purposes as a part of a program to revamp its image in preparation for an initial public offering (IPO).
* The airline operated closely with Air India, Indias national overseas carrier. Alliance Air was a fully owned subsidiary of Indian.
* In 2007, the Government of India announced that Indian would be merged into Air India.
* As part of the merger process, a new company called the National Aviation Company of India Limited (now called Air India Limited) was established, into which both Air India (along with Air India Express) and Indian (along with Alliance Air) would be merged.
* Once the merger was completed, the airline – called Air India – would continue to be headquartered in Mumbai and would have a fleet of over 130 aircraft."""            
        myFont = font.Font(size=20)
        T = Text(itshow, height=10, width=100)
        T.pack()
        T.insert(END, a)
        T['font']=myFont
        button = Button(itshow, text='Close',fg="White",bg="Black", command=destroy_text)
        button.place(relx=0.9,rely=0.4,anchor="center")
        button['font'] = myFont
        
    try:
        window.destroy()      
    except:
        try:
            cav.destroy()
        except:
            print()       
 
    global itshow    
    itshow=Tk()
    itshow.title=("Indian Transport")
    itshow.attributes('-fullscreen',True)
    Coverphoto=PhotoImage(file="123.png")
    label2=Label(itshow,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(itshow,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    myFont = font.Font(size=20)
    l1=Label(itshow,text="Select an option",font=("Arial Bold",45))
    l1.configure(fg="White",bg="Black")
    l1.place(relx=0.5, rely=0.2, anchor="center")
    bt1=Button(itshow,text="Roadways(Bus Services)",fg="Black",bg="White",command=itroadways)
    bt1.place(relx = 0.5, rely = 0.4, anchor = 'c')
    bt1['font']=myFont
    bt2=Button(itshow,text="Railways",fg="Black",bg="White",command=itrailways)
    bt2.place(relx = 0.5, rely = 0.5, anchor = 'c')
    bt2['font']=myFont
    bt3=Button(itshow,text="Airways",fg="Black",bg="White",command=itairways)
    bt3.place(relx = 0.5, rely = 0.6, anchor = 'c')
    bt3['font']=myFont
    bt4=Button(itshow,text="Back",fg="Black",bg="White",command=start1)
    bt4.place(relx = 0.5, rely = 0.7, anchor = 'c')
    bt4['font']=myFont    

def Help():

    try:
        window.destroy()      
    except:
        try:
            cav.destroy()
        except:
            print()

    global windowh
    windowh=Tk()
    windowh.title("MRF.com/Help")
    windowh.attributes('-fullscreen',True) 
    myFont = font.Font(size=15)
    Coverphoto=PhotoImage(file="help.png")
    label2=Label(windowh,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(windowh,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l0=Label(windowh,text='Help',font=("Arial Bold",45))
    l0.place(relx = 0.46, rely = 0.0)
    l0.configure(fg="White",bg="Black")
    l=Label(windowh,text='How to search for different modes of transport?',font=("Arial Bold",30))
    l.place(relx = 0.2, rely = 0.1)
    l.configure(fg="Orange",bg="Black")
    l1=Label(windowh,text='Our search is designed on the principle of easy access',font=("Arial Bold",20))
    l1.place(relx = 0.2, rely = 0.15)
    l1.configure(fg="White",bg="Black")
    l2=Label(windowh,text='*Choose mode of transport in the Guest/User window',font=("Arial Bold",20))
    l2.place(relx = 0.3, rely = 0.2)
    l2.configure(fg="White",bg="Black")
    l3=Label(windowh,text='*Enter from and to city/airport',font=("Arial Bold",20))
    l3.place(relx =0.3, rely = 0.25)
    l3.configure(fg="White",bg="Black")
    l4=Label(windowh,text='*Select the date of travel',font=("Arial Bold",20))
    l4.place(relx = 0.3, rely = 0.3)
    l4.configure(fg="White",bg="Black")
    l5=Label(windowh,text='*Choose the number of travellers ',font=("Arial Bold",20))
    l5.place(relx = 0.3, rely = 0.35)
    l5.configure(fg="White",bg="Black")
    l6=Label(windowh,text='(OR) Directly choose mode of transport here:',font=("Arial Bold",20))
    l6.place(relx = 0.3, rely = 0.4)
    l6.configure(fg="White",bg="Black")
    gt=Button(windowh,text="Airways",fg="Black",bg="White",command= Airways_booking)
    gt.place(relx = 0.4, rely = 0.45)
    gt['font']=myFont
    gt1=Button(windowh,text="Railways",fg="Black",bg="White",command= Railways_booking)
    gt1.place(relx = 0.5, rely = 0.45)
    gt1['font']=myFont
    gt2=Button(windowh,text="Roadways",fg="Black",bg="White",command= Roadways_booking)
    gt2.place(relx = 0.6, rely = 0.45)
    gt2['font']=myFont
    l7=Label(windowh,text='How to create an account?',font=("Arial Bold",30))
    l7.place(relx = 0.2, rely = 0.5)
    l7.configure(fg="Orange",bg="Black")
    l8=Label(windowh,text='*Go to user login in the Welcome to move run fly window',font=("Arial Bold",20))
    l8.place(relx = 0.3, rely = 0.55)
    l8.configure(fg="White",bg="Black")
    l9=Label(windowh,text='*Click on Register button',font=("Arial Bold",20))
    l9.place(relx = 0.3, rely = 0.6)
    l9.configure(fg="White",bg="Black")
    l11=Label(windowh,text='*Fill in all required credentials and click on Submit',font=("Arial Bold",20))
    l11.place(relx = 0.3, rely = 0.65)
    l11.configure(fg="White",bg="Black")
    l10=Label(windowh,text='(OR) Directly Register from here:',font=("Arial Bold",20))
    l10.place(relx = 0.3, rely = 0.7)
    l10.configure(fg="White",bg="Black")
    gt3=Button(windowh,text="Register",fg="Black",bg="White",command= Registration)
    gt3.place(relx = 0.45, rely = 0.75)
    gt3['font']=myFont
    l12=Label(windowh,text='For further details:',font=("Arial Bold",30))
    l12.place(relx = 0.2, rely = 0.8)
    l12.configure(fg="Orange",bg="Black")
    l13=Label(windowh,text='*Contact 1000 1000',font=("Arial Bold",20))
    l13.place(relx = 0.3, rely = 0.85)
    l13.configure(fg="White",bg="Black")
    l14=Label(windowh,text='*Mail:mrf@gmail.com',font=("Arial Bold",20))
    l14.place(relx = 0.3, rely = 0.9)
    l14.configure(fg="White",bg="Black")
    g2=Button(windowh,text="BACK",fg="white",bg="black",command=start1)
    g2.place(relx=0.1,rely=0.88)
    g2['font']=myFont
        
def Exit():
    messagebox.showinfo("Quit","Thank you")
    window.destroy()

def cantic():

    def can():
        print(pnr)
        awe=pnrr.get()
        if awe in pnr:
            messagebox.showinfo("Sucess","Your ticket has been cancelled with 50% deduction")
        else:
            messagebox.showinfo("Error","PNR Number does not exist")    
    try:
        userwindow.destroy()
    except:
        try:
            userportal.destroy()
        except:
            print()

    global ct 
    ct=Tk()
    ct.title("Cancel Ticket")
    ct.attributes('-fullscreen',True)  
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(ct,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(ct,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l1=Label(ct,text="Deleting Ticket",font=("Arial Bold",40))
    l1.configure(fg="White",bg="Black")
    lab1=Label(ct,text="Enter Credentials ",font=("Arial",45))
    lab1.configure(fg="White",bg="Black")
    lab1.place(relx=0.5,rely=0.2,anchor="center")
    lab2=Label(ct,text="Enter PNR number",font=("Arial Bold",25))
    lab2.configure(fg="White",bg="Black")
    lab2.place(relx=0.4,rely=0.4,anchor="center")
    pnrr=Entry(ct,width=25,font=('Arial Bold',20))
    pnrr.place(relx=0.65,rely=0.4,anchor="center")
    bu5=Button(ct,text="Cancel Ticket",fg="White",bg="Black",command=can)
    bu5.place(relx = 0.4, rely = 0.75, anchor = 'c')
    bu5['font']=myFont
    bu6=Button(ct,text="Back",fg="White",bg="Black",command=start2)
    bu6.place(relx = 0.6, rely = 0.75, anchor = 'c')
    bu6['font']=myFont                

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
        else: 
            messagebox.showwarning("Attention","Invalid Username or Password!")

    try:
        window.destroy()
    except:
        try:
            windowA.destroy()
        except:
            try:
                windowR.destroy()
            except:
                try:
                    windowr.destroy()

                except:
                    print()
                    
    global userwindow
    userwindow=Tk()
    userwindow.title("User login")
    userwindow.attributes('-fullscreen',True)
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="1307258.png")
    label2=Label(userwindow,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(userwindow,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    lab1=Label(userwindow,text="Enter Credentials ",font=("Arial",45))
    lab1.configure(fg="White",bg="Black")
    lab1.place(relx=0.5,rely=0.2,anchor="center")
    lab2=Label(userwindow,text="Username",font=("Arial Bold",25))
    lab2.configure(fg="White",bg="Black")
    lab2.place(relx=0.35,rely=0.4,anchor="center")
    lab3=Label(userwindow,text="New user? Click to Register",font=("Arial Bold",25))
    lab3.configure(fg="White",bg="Black")
    lab3.place(relx=0.35,rely=0.6,anchor="center")
    bu3=Button(userwindow,text="Register",fg="White",bg="Black",command=Registration)
    bu3.place(relx=0.6,rely=0.6,anchor="center")
    bu3['font']=myFont
    username=Entry(userwindow,width=25,font=('Arial Bold',20))
    username.place(relx=0.6,rely=0.4,anchor="center")
    lab3=Label(userwindow,text="Password",font=("Arial Bold",25))
    lab3.configure(fg="White",bg="Black")
    lab3.place(relx=0.35,rely=0.45,anchor="center")
    password=Entry(userwindow,show="*",width=25,font=('Arial Bold',20))
    password.place(relx=0.6,rely=0.45,anchor="center")
    bu1=Button(userwindow,text="Submit",fg="White",bg="Black",command=useridpassword)
    bu1.place(relx=0.55,rely=0.53,anchor="center")
    bu1['font']=myFont
    bu2=Button(userwindow,text="Back",fg="White",bg="Black",command=start)
    bu2.place(relx=0.65,rely=0.53,anchor="center")
    bu2['font']=myFont

def user_portal():
    try:
        userwindow.destroy()
    except:
        try:
            cav.destroy()
        except:
            print()

    global userportal 
    userportal=Tk()
    userportal.title("user portal")
    userportal.attributes('-fullscreen',True)  
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(userportal,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(userportal,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l1=Label(userportal,text="User Portal",font=("Arial Bold",40))
    l1.configure(fg="White",bg="Black")
    l1.place(relx=0.5, rely=0.15, anchor="center")
    bu1=Button(userportal,text="Book a Train",fg="White",bg="Black",command=Railways_booking)
    bu1.place(relx = 0.5, rely = 0.3, anchor = 'c')
    bu1['font']=myFont
    bu2=Button(userportal,text="Book a Bus",fg="White",bg="Black",command=Roadways_booking)
    bu2.place(relx = 0.5, rely = 0.45, anchor = 'c')
    bu2['font']=myFont
    bu3=Button(userportal,text="Book a Flight",fg="White",bg="Black",command=Airways_booking)
    bu3.place(relx = 0.5, rely = 0.6, anchor = 'c')
    bu3['font']=myFont
    bu5=Button(userportal,text="Cancel Ticket",fg="White",bg="Black",command=cantic)
    bu5.place(relx = 0.5, rely = 0.75, anchor = 'c')
    bu5['font']=myFont    
    bu4=Button(userportal,text="Exit User Portal",fg="White",bg="Black",command=start)
    bu4.place(relx = 0.5, rely = 0.9, anchor = 'c')
    bu4['font']=myFont

def Railways_booking():    
        
    def banking():

        def bill():
            thisis=[]
            ohm=[]
            ay=[]
            global bil
            bil=Tk()        
            bil.attributes('-fullscreen',True)
            bil.title("bill")
            bil.configure(bg ="light blue")
            beu1=Button(bil,text="Back",fg="White",bg="Black",command=start1)
            beu1.place(relx=0.5,rely=0.9)            
            beu1['font']=myFont            
            dr=Label(bil,text="Ticket Conformation",font=("arial bold",30),bg="light blue",fg="black")
            dr.place(relx=0.01,rely=0.01)
            rr=Label(bil,text="Congratulations!! Thank you for using MRF's online  Rail reservation facility.",font=("arial bold",20),bg="light blue",fg="black")
            tt=Label(bil,text="Your Booking Details are Indicated Below:",font=("arial bold",20),bg="light blue",fg="black")
            rr.place(relx=0.01,rely=0.08)
            tt.place(relx=0.01,rely=0.15)
            j123=Label(bil,text="PNR Number:",font=("arial bold",19),bg="light blue",fg="black")
            j123.place(relx=0.75,rely=0.01)
            pnrr=random.randint(1000000000,9999999999)
            pnr.append(str(pnrr))
            k123=Label(bil,text=pnrr,font=("arial bold",19),bg="light blue",fg="black")
            k123.place(relx=0.85,rely=0.01)              
            j=Label(bil,text="Train No:",font=("arial bold",19),bg="light blue",fg="black")
            j.place(relx=0.01,rely=0.20)
            k=Label(bil,text=available[0][0],font=("arial bold",19),bg="light blue",fg="black")
            k.place(relx=0.16,rely=0.20)        
            current_time = datetime.datetime.now()                 
            j2=Label(bil,text="Date and Time of booking:",font=("arial bold",19),bg="light blue",fg="black")
            j2.place(relx=0.3,rely=0.20)
            konga=Label(bil,text=current_time,font=("arial bold",19),bg="light blue",fg="black")
            konga.place(relx=0.6,rely=0.20)
            y1=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
            y1.place(relx=0.01,rely=0.25)
            j3=Label(bil,text="From:",font=("arial bold",19),bg="light blue",fg="black")
            j3.place(relx=0.01,rely=0.30)
            k3=Label(bil,text=available[0][2],font=("arial bold",19),bg="light blue",fg="black")
            k3.place(relx=0.1,rely=0.30)
            j4=Label(bil,text="Departure:",font=("arial bold",19),bg="light blue",fg="black")
            j4.place(relx=0.3,rely=0.30)
            k4=Label(bil,text=available[0][4],font=("arial bold",19),bg="light blue",fg="black")
            k4.place(relx=0.4,rely=0.30)        
            j5=Label(bil,text="To:",font=("arial bold",19),bg="light blue",fg="black")
            j5.place(relx=0.6,rely=0.30)
            k5=Label(bil,text=available[0][3],font=("arial bold",19),bg="light blue",fg="black")
            k5.place(relx=0.7,rely=0.30)        
            y2=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
            y2.place(relx=0.01,rely=0.35)       
            j6=Label(bil,text="Arrival:",font=("arial bold",19),bg="light blue",fg="black")
            j6.place(relx=0.01,rely=0.40)
            k6=Label(bil,text=available[0][4],font=("arial bold",19),bg="light blue",fg="black")
            k6.place(relx=0.1,rely=0.40)            
            j7=Label(bil,text="Class:",font=("arial bold",19),bg="light blue",fg="black")
            j7.place(relx=0.3,rely=0.40)
            k1=Label(bil,text=clas,font=("arial bold",19),bg="light blue",fg="black")
            k1.place(relx=0.37,rely=0.40)            
            j8=Label(bil,text="Adult:",font=("arial bold",19),bg="light blue",fg="black")
            j8.place(relx=0.60,rely=0.40)
            k8=Label(bil,text=ad,font=("arial bold",19),bg="light blue",fg="black")
            k8.place(relx=0.67,rely=0.40)            
            j9=Label(bil,text="Child:",font=("arial bold",19),bg="light blue",fg="black")
            j9.place(relx=0.75,rely=0.40)
            k9=Label(bil,text=ch,font=("arial bold",19),bg="light blue",fg="black")
            k9.place(relx=0.8,rely=0.40)           
            y3=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
            y3.place(relx=0.01,rely=0.44)
            j10=Label(bil,text="Passenger details:",font=("arial bold",30),bg="light blue",fg="black")
            j10.place(relx=0.01,rely=0.50)
            j11=Label(bil,text="S.I",font=("arial bold",19),bg="light blue",fg="black")
            j11.place(relx=0.01,rely=0.57)
            for i in range(s):
                k11=Label(bil,text=(i+1),font=("arial bold",15),bg="light blue",fg="black")
                k11.place(relx=0.01,rely=0.60+(i/30))            
            j12=Label(bil,text="Name",font=("arial bold",19),bg="light blue",fg="black")
            j12.place(relx=0.1,rely=0.57)
            for i in range(s):
                k12=Label(bil,text=go[i],font=("arial bold",15),bg="light blue",fg="black")
                k12.place(relx=0.1,rely=0.60+(i/30))                    
            j13=Label(bil,text="Age",font=("arial bold",19),bg="light blue",fg="black")
            j13.place(relx=0.25,rely=0.57)
            for i in range(s):
                k13=Label(bil,text=re[i],font=("arial bold",15),bg="light blue",fg="black")
                k13.place(relx=0.25,rely=0.60+(i/30))            
            j14=Label(bil,text="Gender",font=("arial bold",19),bg="light blue",fg="black")
            j14.place(relx=0.35,rely=0.57)
            for i in range(s):
                k14=Label(bil,text=bo[i],font=("arial bold",15),bg="light blue",fg="black")
                k14.place(relx=0.35,rely=0.60+(i/30))                        
            j15=Label(bil,text="Coach",font=("arial bold",19),bg="light blue",fg="black")
            j15.place(relx=0.45,rely=0.57)
            if clas=="First A.C":
                rand=random.randint(1,2)
                rand1=random.randint(1,29)
                coach="F"+str(rand)
                for i in range(s):                
                    k15=Label(bil,text=coach,font=("arial bold",15),bg="light blue",fg="black")
                    k15.place(relx=0.45,rely=0.60+(i/30))
                for i in range(s):                
                    k16=Label(bil,text=rand1+i,font=("arial bold",15),bg="light blue",fg="black")
                    k16.place(relx=0.55,rely=0.61+(i/30))                    
            elif clas=="Second A.C":            
                rand=random.randint(1,3)
                rand1=random.randint(1,51)
                coach="A"+str(rand)
                for i in range(s):                                
                    k15=Label(bil,text=coach,font=("arial bold",15),bg="light blue",fg="black")
                    k15.place(relx=0.45,rely=0.60+(i/30))
                for i in range(s):                              
                    k16=Label(bil,text=rand1+i,font=("arial bold",15),bg="light blue",fg="black")
                    k16.place(relx=0.55,rely=0.61+(i/30))                
            elif clas=="Third A.C":            
                rand=random.randint(1,3)
                rand1=random.randint(1,69)
                coach="B"+str(rand)
                for i in range(s):                
                    k15=Label(bil,text=coach,font=("arial bold",15),bg="light blue",fg="black")
                    k15.place(relx=0.45,rely=0.61+(i/30))
                for i in range(s):                                                                
                   k16=Label(bil,text=rand1+i,font=("arial bold",15),bg="light blue",fg="black")
                   k16.place(relx=0.55,rely=0.60+(i/30))
            elif  clas=="Sleeper":            
                rand=random.randint(1,11)
                rand1=random.randint(1,72)
                coach="S"+str(rand)
                for i in range(s):
                     k15=Label(bil,text=coach,font=("arial bold",15),bg="light blue",fg="black")
                     k15.place(relx=0.45,rely=0.60+(i/30))
                for i in range(s):                                               
                    k16=Label(bil,text=rand1+i,font=("arial bold",15),bg="light blue",fg="black")
                    k16.place(relx=0.55,rely=0.60+(i/30))                        
            j16=Label(bil,text="Seat",font=("arial bold",19),bg="light blue",fg="black")
            j16.place(relx=0.55,rely=0.57)            
            y4=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
            y4.place(relx=0.01,rely=0.74)            
            j17=Label(bil,text="Fare Details:",font=("arial bold",30),bg="light blue",fg="black")
            j17.place(relx=0.01,rely=0.77)            
            j18=Label(bil,text="Ticket Fee",font=("arial bold",19),bg="light blue",fg="black")
            j18.place(relx=0.01,rely=0.84)
            k18=Label(bil,text=c,font=("arial bold",25),bg="light blue",fg="black")
            k18.place(relx=0.01,rely=0.87)            
            j19=Label(bil,text="Convenience Fee",font=("arial bold",19),bg="light blue",fg="black")
            j19.place(relx=0.2,rely=0.84)
            k19=Label(bil,text=s*15,font=("arial bold",25),bg="light blue",fg="black")
            k19.place(relx=0.2,rely=0.87)            
            j20=Label(bil,text="Total Fee",font=("arial bold",19),bg="light blue",fg="black")
            j20.place(relx=0.4,rely=0.84)
            k20=Label(bil,text=c+(s*15),font=("arial bold",25),bg="light blue",fg="black")
            k20.place(relx=0.4,rely=0.87)
            thisis.append(go)
            thisis.append(re)
            thisis.append(bo)
            for i in range(s):
                ohm.append(clas)
            for i in range(s):
                ay.append(coach)
            thisis.append(ohm)                    
            thisis.append(ay)
            print(thisis)
            okq=available[0][1]+'.csv'
            fq=open(okq,'a')
            wobj=csv.writer(fq,delimiter=',')
            for i in range(0,s):
                wobj.writerow([thisis[0][i],thisis[1][i],thisis[2][i],thisis[3][i],thisis[4][i]])   
            fq.close()
            teach.pop()

        def payment_mode():

            def debit_card():
            
                def debit_check():
                    num1=cardno.get()
                    num2=pinno.get()
                    if num1 in debit and num2 in debit:
                        print("oho")
                        bill()
                        debitwindow.destroy()
                    else: 
                        messagebox.showwarning("Attention","Numbers do not match")
                        debitwindow.destroy()
                        
                paymentwindow.destroy()
                debitwindow=Tk()
                debitwindow.title("payment mode")
                debitwindow.attributes('-fullscreen',True) 
                debitwindow.configure(bg ="light Blue")
                deb1=Label(debitwindow,text="Enter required credentials to enter the portal",font=("Arial Bold",25))
                deb1.configure(fg="Black",bg="light Blue")
                deb1.place(relx=0.55,rely=0.2,anchor="center")
                lb0=Label(debitwindow,text="Amount:",font=("Arial Bold",25))
                lb0.configure(fg="black",bg="light blue")
                lb0.place(relx=0.45,rely=0.1)
                lbb0=Label(debitwindow,text=c+(s*15),font=("Arial Bold",25))
                lbb0.configure(fg="Red",bg="light blue")
                lbb0.place(relx=0.65,rely=0.1) 
                deb2=Label(debitwindow,text="Enter number in D",font=("Arial",20))
                deb2.place(relx=0.4,rely=0.4,anchor="center")
                deb2.configure(fg="Black",bg="Light Blue")
                cardno=Entry(debitwindow,show="*",width=10,font=('Arial Bold',15))
                cardno.place(relx=0.65,rely=0.4,anchor="center")
                deb3=Label(debitwindow,text="Enter number in M",font=("Arial",20))
                deb3.place(relx=0.4,rely=0.45,anchor="center")
                deb3.configure(fg="Black",bg="Light Blue")
                pinno=Entry(debitwindow,show="*",width=10,font=('Arial Bold',15))
                pinno.place(relx=0.65,rely=0.45,anchor="center")
                du1=Button(debitwindow,text="Submit",fg="White",bg="Black",command=debit_check)
                du1.place(relx=0.55,rely=0.5,anchor="center")
                du1['font']=myFont      
                du2=Button(debitwindow,text="Back",fg="White",bg="Black",command=debitwindow.destroy)
                du2.place(relx=0.65,rely=0.5,anchor="center")
                du2['font']=myFont  

            def bank_login():
                    
                def bankidpassword():
                    c=0
                    num1=usename.get()
                    num2=password1.get()
                    for i in range(len(banklogin)):
                        if num1 in banklogin[i][0] and num2 in banklogin[i][1]:
                            c+=1
                    if c==1:
                        bill()
                        banklog.destroy()
                    else: 
                        messagebox.showwarning("Attention","Invalid Username or Password!")
                        banklog.destroy()
                        
                paymentwindow.destroy()
                banklog=Tk()       
                banklog.attributes('-fullscreen',True)
                banklog.title("bank login")
                banklog.configure(bg ="light blue")
                lb0=Label(banklog,text="Amount:",font=("Arial Bold",25))
                lb0.configure(fg="black",bg="light blue")
                lb0.place(relx=0.45,rely=0.1)
                lbb0=Label(banklog,text=c+(s*15),font=("Arial Bold",25))
                lbb0.configure(fg="Red",bg="Light Blue")
                lbb0.place(relx=0.65,rely=0.1)        
                lb1=Label(banklog,text="Enter required  bank credentials for payment",font=("Arial",25))
                lb1.configure(fg="Black",bg="Light Blue")
                lb1.place(relx=0.55,rely=0.2,anchor="center")
                lb2=Label(banklog,text="Username",font=("Arial",20))
                lb2.place(relx=0.5,rely=0.4,anchor="center")
                lb2.configure(fg="Black",bg="Light Blue")
                usename=Entry(banklog,width=10,font=('Arial Bold',15))
                usename.place(relx=0.6,rely=0.4,anchor="center")
                lb3=Label(banklog,text="Password",font=("Arial",20))
                lb3.place(relx=0.5,rely=0.45,anchor="center")
                lb3.configure(fg="Black",bg="Light Blue")
                password1=Entry(banklog,show="*",width=10,font=('Arial Bold',15))
                password1.place(relx=0.6,rely=0.45,anchor="center")
                bue1=Button(banklog,text="Submit",fg="White",bg="Black",command=bankidpassword)
                bue1.place(relx=0.55,rely=0.5,anchor="center")
                bue1['font']=myFont
                bue2=Button(banklog,text="Back",fg="White",bg="Black",command=banklog.destroy)
                bue2.place(relx=0.65,rely=0.5,anchor="center")
                bue2['font']=myFont             
                
            paymentwindow=Tk()
            paymentwindow.title("payment mode")
            paymentwindow.attributes('-fullscreen',True) 
            paymentwindow.configure(bg ="Light Blue")
            pa1=Button(paymentwindow,text="Net banking",fg="White",bg="Black",command=bank_login)
            pa1.place(relx=0.5,rely=0.4,anchor="center")
            pa1['font']=myFont
            pa2=Button(paymentwindow,text="Debit card",fg="White",bg="Black",command=debit_card)
            pa2.place(relx=0.5,rely=0.66,anchor="center")
            pa2['font']=myFont 
            p1=Label(paymentwindow,text="Payment Mode",font=("Arial Bold",45))
            p1.configure(fg="Black",bg="Light Blue")
            p1.place(relx=0.5, rely=0.12, anchor="center")
            p2=Button(paymentwindow,text="Back",fg="White",bg="Black",command=paymentwindow.destroy)
            p2.place(relx=0.05,rely=0.9,anchor="center")
            p2['font']=myFont 
                        
        try:
             userportal.destroy()      
        except:
            try:
                cav.destroy()
            except:
                print()
        
        global ad
        global ch
        global c
        c=0
        ad=0
        ch=0            
        clas=teach[0].get()
        global s
        s=e[0]
        print(s)
        re=[]
        go=[]
        bo=[]
        for i in range (s):
            go.append(Railwayspassenger[i][0].get())
            bo.append(Railwayspassenger[i][2].get())
          
        for i in range(s):
            gh=0
            gh+=int(Railwayspassenger[i][1].get())
            re.append(gh)    
        print(re)        
        for i in range(s):        
            op=0
            if re[i]<=13  or  re[i]>=60 :
                if clas=="First A.C":
                    op+=1000
                    c+=op
                    print(c)
                elif clas=="Second A.C":
                    op+=750
                    c+=op
                elif clas=="Third A.C":
                    op+=500
                    c+=op
                elif  clas=="Sleeper":
                    op+=250
                    c+=op                                            
            else:
                
                if clas=="First A.C":
                    op+=2000
                    c+=op                
                elif clas=="Second A.C":
                    op+=1500
                    c+=op
                elif clas=="Third A.C":
                    op+=1000
                    c+=op
                elif  clas=="Sleeper":
                    op+=500
                    c+=op
                    
        for i in range(s):
            if re[i]>=13:
                ad+=1
            else:
                ch+=1
        print(c)
        inform.destroy()
        global bankin        
        bankin=Tk()
        bankin.attributes('-fullscreen',True)
        bankin.title("banking")
        C=PhotoImage(file="money.png")
        label2=Label(bankin,image=C)
        label2.place(relx = 0.5,rely = 0.5, anchor ='center')
        label2.image =C
        label2.pack
        Title=Label(bankin,text="PAYMENT",font=("arial bold",45),bg="Black",fg="White")
        Title.place(relx=0.4,rely=0.05)
        df=Label(bankin,text="AMOUNT TO BE PAYED",font=("arial bold",25),bg="Black",fg="White")
        df.place(relx=0.1,rely=0.2)
        rf=Label(bankin,text="Rs"+str(c),font=("arial bold",25),bg="Black",fg="red")
        rf.place(relx=0.4,rely=0.19)
        be1=Button(bankin,text="Back",fg="White",bg="Black",command=start1)
        be1.place(relx=0.1,rely=0.9)
        be1['font']=myFont
        ef=Label(bankin,text="CHOOSE A BANK",font=("arial bold",25),bg="Black",fg="White")
        ef.place(relx=0.1,rely=0.3)
        t=StringVar()
        io=Radiobutton(bankin,text="ICICI",variable=t,value="ICICI",bg="Black",fg="White",font=("arial bold",20))
        io.place(relx=0.1,rely=0.4)
        io1=Radiobutton(bankin,text="SBI",variable=t,value="SBI",bg="Black",fg="White",font=("arial bold",20))
        io1.place(relx=0.1,rely=0.5)
        io2=Radiobutton(bankin,text="HDFC",variable=t,value="HDFC",bg="Black",fg="White",font=("arial bold",20))
        io2.place(relx=0.1,rely=0.6)
        br=Button(bankin,text="Continue",fg="White",bg="Black",command=payment_mode)
        br.place(relx=0.9,rely=0.9)
        br['font']=myFont
       
    def input_information(): 
        
        try:
            userportal.destroy()      
        except:
            try:
                cav.destroy()
            except:
                print()
                
        global inform
        e2=int(adult.get())+int(children.get())+int(seniormen.get())+int(seniorwomen.get())
        e.append(e2)
        windowRa.destroy()
        inform=Tk()
        inform.attributes('-fullscreen',True)
        inform.title("input information")
        inform.configure(bg="Light pink")
        photo=PhotoImage(file="project.png")
        label=Label(inform,image=photo)
        label.place(relx = 0.94,rely = 0.1, anchor ='center')
        label.image = photo
        label.pack
        l1=Label(inform,text="Enter the Details",font=("Arial Bold",45))
        l1.configure(fg="White",bg="Black")
        l1.place(relx=0.5,rely=0.1,anchor='center')
        for j in range (11):
            if e2==j:
                for i in range(j):
                    ne=[]                       
                    o1=Label(inform,text="Name",font=("Arial Bold",15))
                    o1.place(relx=0.11,rely=0.3+(i/10))
                    o1.configure(fg="Black",bg="Light Pink")
                    o2=Entry(inform,width=10,font=('Arial Bold',15))
                    o2.place(relx=0.15,rely=0.3+(i/10))
                    age=Label(inform,text="Age",font=("Arial Bold",15))
                    age.place(relx=0.25,rely=0.3+(i/10))
                    age.configure(fg="Black",bg="Light Pink")
                    age1=Entry(inform,width=10,font=('Arial Bold',15))
                    age1.place(relx=0.3,rely=0.3+(i/10))
                    ge=Label(inform,text="Gender",font=("Arial Bold",15))
                    ge.place(relx=0.4,rely=0.3+(i/10))
                    ge.configure(fg="Black",bg="Light Pink")
                    ge1=ttk.Combobox(inform,values=["Male","Female","Transgender"])
                    ge1.place(relx=0.45,rely=0.3+(i/10))
                    quo=Label(inform,text="Class",fg="Blue",bg="yellow",font=("Arial Bold",15))
                    quo.place(relx=0.55,rely=0.3+(i/10))
                    quo.configure(fg="Black",bg="Light Pink")
                    drop3=ttk.Combobox(inform,values=["First A.C","Second A.C","Third A.C","Sleeper"])
                    drop3.place(relx=0.64,rely=0.31+(i/10),anchor="center")
                    teach.append(drop3)
                    pre=Label(inform,text="Preference",font=("Arial Bold",15))
                    pre.place(relx=0.7,rely=0.3+(i/10))
                    pre.configure(fg="Black",bg="Light Pink")
                    pre1=ttk.Combobox(inform,values=["No Preferences","Lower","Middle","Upper"])
                    pre1.place(relx=0.78,rely=0.3+(i/10))
                    pre1.current()
                    bu1=Button(inform,text="Back",fg="White",bg="Black",command=inform.destroy)
                    bu1.place(relx=0.4,rely=0.8,anchor="center")
                    bu1['font']=myFont
                    bu2=Button(inform,text="Proceed",fg="White",bg="Black",command=banking)
                    bu2.place(relx=0.6,rely=0.8,anchor="center")
                    bu2['font']=myFont
                    ne.append(o2)
                    ne.append(age1)
                    ne.append(ge1)
                    ne.append(pre1)
                    Railwayspassenger.append(ne)                    
                            
    def comsearchit():
        
        def namecheck():
            qwe=d1.get()
            iru=0
            for i in range(len(m)):
                if qwe==m[i][1]:
                    input_information()
                    root.destroy()
                    iru+=1
            if iru ==0:
                messagebox.showinfo("Oops!","Give a Train name which is the chart")
                root.destroy()

        global available                
        m=[]
        of=userfrom.get()
        ot=userto.get()
        dateo=day.get()+' '+month.get()+' '+year.get()
        f=open("Railways.csv",'r')
        lab=tom=0
        robj=csv.reader(f,delimiter=",")
        for a in robj:
            if tom%2==0:
                if a[2]==of and a[3]==ot and dateo==a[4]:
                    m.append(a)
                    lab+=1
            tom+=1
        available=m
        print(available)
        if lab==0:
            messagebox.showinfo("Oops!","No Train found")
    
        class Table:       
            def __init__(self,root):
                for i in range(10,total_rows+10):
                    for j in range(10,total_columns+10):
                        self.e = Entry(root, width=17, fg='blue', 
                                        font=('Arial',15,'bold'))                   
                        self.e.grid(row=i+1, column=j+1)
                        self.e.insert(END, m[i-10][j-10])
  
        total_rows = len(m) 
        total_columns = len(m[0])
        fna='Railways'
        root = Tk()
        root.attributes('-fullscreen',True)
        root.title("Available Trains")
        myFont = font.Font(size=20)
        root.configure(bg ="Light blue")
        l1=Label(root,text="Available Trains",font=("Arial Bold",40))
        l1.configure(fg="Black",bg="Light Blue")
        l1.place(relx=0.5, rely=0.05, anchor="center")
        goq='Train No.  \t  Train Name\t  Origin\t\tDestination\t  Departure\t    Arrival\t\tStatus'     
        l2=Label(root,text=goq,font=("Arial Bold",17))
        l2.configure(fg="Black",bg="Light Blue")
        l2.place(relx=0.43, rely=0.15, anchor="center")
        for r in range(9):
            bi=Label(root,text="   ",bg="Light Blue")
            bi.grid(row=r,column=0) 
        g1=Button(root,text="BOOK",fg="White",bg="Black",command=namecheck)
        g1.place(relx=0.9,rely=0.9)
        g1['font']=myFont
        g2=Button(root,text="BACK",fg="White",bg="Black",command=root.destroy)
        g2.place(relx=0.1,rely=0.9)
        g2['font']=myFont
        bi2=Label(root,text="Enter the name of the Train you want to book",font=("Arial Bold",20))        
        bi2.place(relx=0.1,rely=0.6)
        bi2.configure(fg="Black",bg="Light Blue")
        d1=Entry(root,fg="Blue",bg="White",width=25,font=('Arial Bold',20))
        d1.place(relx=0.5,rely=0.6)
        t = Table(root)
        root.mainloop()

    try:
        userportal.destroy()      
    except:
        try:
            cav.destroy()
        except:
            print()

    global windowRa    
    windowRa=Tk()
    windowRa.title("MRF.com/Guest/choosing mode of transport/Railays")
    windowRa.attributes('-fullscreen',True)
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(windowRa,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(windowRa,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    lc=Label(windowRa,text='Enter the required details',font=("Arial Bold",45))
    lc.place(relx = 0.3, rely = 0.14)
    lc.configure(fg="White",bg="Black")
    l1=Label(windowRa,text='From:',font=("Arial Bold",20))
    l1.place(relx = 0.25, rely = 0.35)
    l1.configure(fg="White",bg="Black")   
    userfrom=ttk.Combobox(windowRa,values=Railwaysdestination)
    userfrom.place(relx = 0.295, rely = 0.4, anchor = 'c')
    userfrom.current()
    l2=Label(windowRa,text='To:',font=("Arial Bold",20))
    l2.place(relx = 0.25, rely = 0.55)
    l2.configure(fg="White",bg="Black")
    userto=ttk.Combobox(windowRa,values=Railwaysdestination)
    userto.place(relx = 0.295, rely = 0.6, anchor = 'c')
    userto.current()
    ld=Label(windowRa,text='Day:',font=("Arial Bold",20))
    ld.place(relx = 0.55, rely = 0.35)
    ld.configure(fg="White",bg="Black")
    day=ttk.Combobox(windowRa,values=vai)
    day.place(relx = 0.595, rely = 0.4, anchor = 'c')
    day.current()
    l3=Label(windowRa,text='Month:',font=("Arial Bold",20))
    l3.place(relx = 0.65, rely = 0.35)
    l3.configure(fg="White",bg="Black")
    month=ttk.Combobox(windowRa,values=['January','February','March',
                                       'April','May','June','July',
                                       'August','September','October',
                                       'November','December'])
    month.place(relx = 0.695, rely = 0.4, anchor = 'c')
    month.current()
    l4=Label(windowRa,text='Year:',font=("Arial Bold",20))
    l4.place(relx = 0.75, rely = 0.35)
    l4.configure(fg="White",bg="Black")
    year=ttk.Combobox(windowRa,values=['2020','2021','2022'])
    year.place(relx = 0.795, rely = 0.4, anchor = 'c')
    year.current()
    adult=ttk.Combobox(windowRa,values=['0','1','2','3','4','5','6'])
    adult.place(relx = 0.595, rely = 0.605, anchor = 'c')
    l5=Label(windowRa,text='Adults(12-60yrs):',font=("Arial Bold",20))
    l5.place(relx = 0.55, rely = 0.55)
    l5.configure(fg="White",bg="Black")
    children=ttk.Combobox(windowRa,values=['0','1','2','3','4','5','6'])
    children.place(relx = 0.795, rely = 0.605, anchor = 'c')
    l6=Label(windowRa,text='Children(5-11yrs):',font=("Arial Bold",20))
    l6.place(relx = 0.75, rely =0.55)
    l6.configure(fg="White",bg="Black")
    seniormen=ttk.Combobox(windowRa,values=['0','1','2','3','4','5','6'])
    seniormen.place(relx = 0.595, rely = 0.7055, anchor='c')
    l7=Label(windowRa,text='Senior Men(60+yrs):',font=("Arial Bold",20))
    l7.place(relx = 0.55, rely = 0.65)
    l7.configure(fg="White",bg="Black")
    seniorwomen=ttk.Combobox(windowRa,values=['0','1','2','3','4','5','6'])
    seniorwomen.place(relx = 0.795, rely = 0.7055, anchor='c')
    l8=Label(windowRa,text='Senior Women(58+yrs):',font=("Arial Bold",20))
    l8.place(relx = 0.75, rely = 0.65)
    l8.configure(fg="White",bg="Black")
    bt=Button(windowRa,text="Back",fg="White",bg="Black",command=start1)
    bt.place(relx=0.1,rely=0.88)
    bt['font']=myFont
    bt2=Button(windowRa,text="Search",fg="White",bg="Black",command=comsearchit)
    bt2.place(relx=0.5,rely=0.9,anchor="c")
    bt2['font']=myFont                    

def Airways_booking():
    
    def banking():

        def bill():
            thisis=[]
            ohm=[]
            ay=[]
            global bil
            bil=Tk()
            bil.attributes('-fullscreen',True)
            bil.title("bill")
            bil.configure(bg ="light blue")
            beu1=Button(bil,text="Back",fg="White",bg="Black",command=start1)
            beu1.place(relx=0.5,rely=0.9)
            beu1['font']=myFont
            dr=Label(bil,text="Ticket Conformation",font=("arial bold",30),bg="light blue",fg="black")
            dr.place(relx=0.01,rely=0.01)
            rr=Label(bil,text="Congratulations!! Thank you for using MRF's online  Airline reservation facility.",font=("arial bold",20),bg="light blue",fg="black")
            tt=Label(bil,text="Your Booking Details are Indicated Below:",font=("arial bold",20),bg="light blue",fg="black")
            rr.place(relx=0.01,rely=0.08)
            tt.place(relx=0.01,rely=0.15)
            j123=Label(bil,text="PNR Number:",font=("arial bold",19),bg="light blue",fg="black")
            j123.place(relx=0.75,rely=0.01)
            pnrr=random.randint(1000000000,9999999999)
            pnr.append(str(pnrr))
            k123=Label(bil,text=pnrr,font=("arial bold",19),bg="light blue",fg="black")
            k123.place(relx=0.85,rely=0.01)
            j=Label(bil,text="Airline No:",font=("arial bold",19),bg="light blue",fg="black")
            j.place(relx=0.01,rely=0.20)
            k=Label(bil,text=available[0][0],font=("arial bold",19),bg="light blue",fg="black")
            k.place(relx=0.16,rely=0.20)
            current_time = datetime.datetime.now()    
            j2=Label(bil,text="Date and Time of booking:",font=("arial bold",19),bg="light blue",fg="black")
            j2.place(relx=0.4,rely=0.20)
            konga=Label(bil,text=current_time,font=("arial bold",19),bg="light blue",fg="black")
            konga.place(relx=0.6,rely=0.20)            
            y1=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
            y1.place(relx=0.01,rely=0.25)
            j3=Label(bil,text="From:",font=("arial bold",19),bg="light blue",fg="black")
            j3.place(relx=0.01,rely=0.30)
            k3=Label(bil,text=available[0][2],font=("arial bold",19),bg="light blue",fg="black")
            k3.place(relx=0.1,rely=0.30)        
            j4=Label(bil,text="Departure:",font=("arial bold",19),bg="light blue",fg="black")
            j4.place(relx=0.3,rely=0.30)
            k4=Label(bil,text=available[0][4],font=("arial bold",19),bg="light blue",fg="black")
            k4.place(relx=0.4,rely=0.30)        
            j5=Label(bil,text="To:",font=("arial bold",19),bg="light blue",fg="black")
            j5.place(relx=0.6,rely=0.30)
            k5=Label(bil,text=available[0][3],font=("arial bold",19),bg="light blue",fg="black")
            k5.place(relx=0.7,rely=0.30)        
            y2=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
            y2.place(relx=0.01,rely=0.35)        
            j6=Label(bil,text="Arrival:",font=("arial bold",19),bg="light blue",fg="black")
            j6.place(relx=0.01,rely=0.40)
            k6=Label(bil,text=available[0][4],font=("arial bold",19),bg="light blue",fg="black")
            k6.place(relx=0.1,rely=0.40)       
            j7=Label(bil,text="Arrival Terminal:",font=("arial bold",19),bg="light blue",fg="black")
            j7.place(relx=0.3,rely=0.40)
            rand2=random.randint(1,10)
            k7=Label(bil,text=rand2,font=("arial bold",23),bg="light blue",fg="black")
            k7.place(relx=0.45,rely=0.40)            
            j8=Label(bil,text="Adult:",font=("arial bold",19),bg="light blue",fg="black")
            j8.place(relx=0.60,rely=0.40)
            k8=Label(bil,text=ad,font=("arial bold",19),bg="light blue",fg="black")
            k8.place(relx=0.67,rely=0.40)        
            j9=Label(bil,text="Child:",font=("arial bold",19),bg="light blue",fg="black")
            j9.place(relx=0.75,rely=0.40)
            k9=Label(bil,text=ch,font=("arial bold",19),bg="light blue",fg="black")
            k9.place(relx=0.8,rely=0.40)        
            y3=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
            y3.place(relx=0.01,rely=0.44)
            j10=Label(bil,text="Traveller's details:",font=("arial bold",30),bg="light blue",fg="black")
            j10.place(relx=0.01,rely=0.50)
            j11=Label(bil,text="S.I",font=("arial bold",19),bg="light blue",fg="black")
            j11.place(relx=0.01,rely=0.57)            
            for i in range(s):                
                k11=Label(bil,text=(i+1),font=("arial bold",15),bg="light blue",fg="black")
                k11.place(relx=0.01,rely=0.60+(i/30))                
            j12=Label(bil,text="Name",font=("arial bold",19),bg="light blue",fg="black")
            j12.place(relx=0.1,rely=0.57)
            for i in range(s):
                kola=Airwayspassenger[i][0]
                print(kola)             
                k12=Label(bil,text=go[i],font=("arial bold",15),bg="light blue",fg="black")
                k12.place(relx=0.1,rely=0.60+(i/30))                
            j13=Label(bil,text="Age",font=("arial bold",19),bg="light blue",fg="black")
            j13.place(relx=0.25,rely=0.57)
            for i in range(s):
                k13=Label(bil,text=re[i],font=("arial bold",15),bg="light blue",fg="black")
                k13.place(relx=0.25,rely=0.60+(i/30))
            j14=Label(bil,text="Gender",font=("arial bold",19),bg="light blue",fg="black")
            j14.place(relx=0.35,rely=0.57)
            for i in range(s):
                k14=Label(bil,text=bo[i],font=("arial bold",15),bg="light blue",fg="black")
                k14.place(relx=0.35,rely=0.60+(i/30))
            j15=Label(bil,text="Class",font=("arial bold",19),bg="light blue",fg="black")
            j15.place(relx=0.45,rely=0.57)
            for i in range(s):
                k13=Label(bil,text=co[i],font=("arial bold",15),bg="light blue",fg="black")
                k13.place(relx=0.45,rely=0.60+(i/30))                                                    
            j16=Label(bil,text="Seat",font=("arial bold",19),bg="light blue",fg="black")
            j16.place(relx=0.55,rely=0.57)
            for i in range(s):
                k13=Label(bil,text=se[i],font=("arial bold",15),bg="light blue",fg="black")
                k13.place(relx=0.55,rely=0.60+(i/30))         
            y4=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
            y4.place(relx=0.01,rely=0.74)
            j17=Label(bil,text="Payment Details:",font=("arial bold",30),bg="light blue",fg="black")
            j17.place(relx=0.01,rely=0.77)
            j18=Label(bil,text="Basic Fare",font=("arial bold",19),bg="light blue",fg="black")
            j18.place(relx=0.01,rely=0.84)
            k18=Label(bil,text=c,font=("arial bold",25),bg="light blue",fg="black")
            k18.place(relx=0.01,rely=0.87)            
            j19=Label(bil,text="Tax",font=("arial bold",19),bg="light blue",fg="black")
            j19.place(relx=0.2,rely=0.84)
            k19=Label(bil,text=0.23*c,font=("arial bold",25),bg="light blue",fg="black")#calculate tax by taking 23% of each ticket
            k19.place(relx=0.2,rely=0.87)        
            j20=Label(bil,text="Gross Amount",font=("arial bold",19),bg="light blue",fg="black")
            j20.place(relx=0.4,rely=0.84)
            k20=Label(bil,text=c+(0.23*c),font=("arial bold",25),bg="light blue",fg="black")
            k20.place(relx=0.4,rely=0.87)
            thisis.append(go)
            thisis.append(re)
            thisis.append(bo)  
            thisis.append(co)                    
            thisis.append(se)
            print(thisis)
            okq=available[0][1]+'.csv'
            fq=open(okq,'a')
            wobj=csv.writer(fq,delimiter=',')
            for i in range(0,s):
                wobj.writerow([thisis[0][i],thisis[1][i],thisis[2][i],thisis[3][i],thisis[4][i]])   
            fq.close()
            teach.pop()

        def payment_mode():

            def debit_card():
            
                def debit_check():
                    num1=cardno.get()
                    num2=pinno.get()
                    if num1 in debit and num2 in debit:
                        bill()
                        debitwindow.destroy()
                    else: 
                        messagebox.showwarning("Attention","Numbers do not match")
                        debitwindow.destroy()
                        
                paymentwindow.destroy() 
                debitwindow=Tk()
                debitwindow.title("payment mode")
                debitwindow.attributes('-fullscreen',True) 
                debitwindow.configure(bg ="light Blue")
                deb1=Label(debitwindow,text="Enter required credentials to enter the portal",font=("Arial Bold",25))
                deb1.configure(fg="Black",bg="light Blue")
                lb0=Label(debitwindow,text="Amount:",font=("Arial Bold",25))
                lb0.configure(fg="black",bg="light blue")
                lb0.place(relx=0.45,rely=0.1)
                lbb0=Label(debitwindow,text=c+(s*15),font=("Arial Bold",25))
                lbb0.configure(fg="Red",bg="light blue")
                lbb0.place(relx=0.65,rely=0.1) 
                deb1.place(relx=0.55,rely=0.2,anchor="center")
                deb2=Label(debitwindow,text="Enter number in D",font=("Arial",20))
                deb2.place(relx=0.4,rely=0.4,anchor="center")
                deb2.configure(fg="Black",bg="light Blue")
                cardno=Entry(debitwindow,show="*",width=10,font=('Arial Bold',15))
                cardno.place(relx=0.65,rely=0.4,anchor="center")
                deb3=Label(debitwindow,text="Enter number in M",font=("Arial",20))
                deb3.place(relx=0.4,rely=0.45,anchor="center")
                deb3.configure(fg="Black",bg="light Blue")
                pinno=Entry(debitwindow,show="*",width=10,font=('Arial Bold',15))
                pinno.place(relx=0.65,rely=0.45,anchor="center")
                du1=Button(debitwindow,text="Submit",fg="White",bg="Black",command=debit_check)
                du1.place(relx=0.55,rely=0.5,anchor="center")
                du1['font']=myFont      
                du2=Button(debitwindow,text="Back",fg="White",bg="Black",command=debitwindow.destroy)
                du2.place(relx=0.65,rely=0.5,anchor="center")
                du2['font']=myFont  

            def bank_login():
                    
                def bankidpassword():
                    c=0
                    num1=usename.get()
                    num2=password1.get()
                    for i in range(len(banklogin)):
                        if num1 in banklogin[i][0] and num2 in banklogin[i][1]:
                            c+=1
                    if c==1:
                        bill()
                        banklog.destroy()
                    else: 
                        messagebox.showwarning("Attention","Invalid Username or Password!")
                        banklog.destroy()
                        
                paymentwindow.destroy()       
                banklog=Tk()       
                banklog.attributes('-fullscreen',True)
                banklog.title("bank login")
                banklog.configure(bg ="light blue")
                lb0=Label(banklog,text="Amount:",font=("Arial Bold",25))
                lb0.configure(fg="black",bg="light blue")
                lb0.place(relx=0.45,rely=0.1)
                lbb0=Label(banklog,text=c+(s*15),font=("Arial Bold",25))
                lbb0.configure(fg="Red",bg="light blue")
                lbb0.place(relx=0.65,rely=0.1)        
                lb1=Label(banklog,text="Enter required  bank credentials for payment",font=("Arial",25))
                lb1.configure(fg="black",bg="light blue")
                lb1.place(relx=0.55,rely=0.2,anchor="center")
                lb2=Label(banklog,text="Username",font=("Arial",20))
                lb2.place(relx=0.5,rely=0.4,anchor="center")
                lb2.configure(fg="black",bg="light blue")
                usename=Entry(banklog,width=10,font=('Arial Bold',15))
                usename.place(relx=0.6,rely=0.4,anchor="center")
                lb3=Label(banklog,text="Password",font=("Arial",20))
                lb3.place(relx=0.5,rely=0.45,anchor="center")
                lb3.configure(fg="black",bg="light blue")
                password1=Entry(banklog,show="*",width=10,font=('Arial Bold',15))
                password1.place(relx=0.6,rely=0.45,anchor="center")
                bue1=Button(banklog,text="Submit",fg="White",bg="Black",command=bankidpassword)
                bue1.place(relx=0.55,rely=0.5,anchor="center")
                bue1['font']=myFont
                bue2=Button(banklog,text="Back",fg="White",bg="Black",command=banklog.destroy)
                bue2.place(relx=0.65,rely=0.5,anchor="center")
                bue2['font']=myFont             
                
            paymentwindow=Tk()
            paymentwindow.title("payment mode")
            paymentwindow.attributes('-fullscreen',True) 
            paymentwindow.configure(bg ="light Blue")
            pa1=Button(paymentwindow,text="Net banking",fg="White",bg="Black",command=bank_login)
            pa1.place(relx=0.5,rely=0.4,anchor="center")
            pa1['font']=myFont
            pa2=Button(paymentwindow,text="Debit card",fg="White",bg="Black",command=debit_card)
            pa2.place(relx=0.5,rely=0.66,anchor="center")
            pa2['font']=myFont 
            p1=Label(paymentwindow,text="Payment Mode",font=("Arial Bold",45))
            p1.configure(fg="Black",bg="light Blue")
            p1.place(relx=0.5, rely=0.12, anchor="center")
            p2=Button(paymentwindow,text="Back",fg="White",bg="Black",command=paymentwindow.destroy)
            p2.place(relx=0.05,rely=0.9,anchor="center")
            p2['font']=myFont
                    
        try:
             userportal.destroy()      
        except:
            try:
                cav.destroy()
            except:
                print()

        global ad
        global ch
        global c
        c=0
        ad=0
        ch=0            
        clas=teach[0].get()
        global s
        s=e[0]
        re=[]
        go=[]
        bo=[]
        se=[]
        co=[]
        for i in range (s):
            go.append(Airwayspassenger[i][0].get())
            bo.append(Airwayspassenger[i][2].get())
            co.append(Airwayspassenger[i][3].get())
            se.append(Airwayspassenger[i][4].get()) 
        for i in range(s):
            gh=0
            gh+=int(Airwayspassenger[i][1].get())
            re.append(gh)    
        print(re)        
        for i in range(s):        
            op=0
            if clas=="Business":
                op+=8400
                c+=op
            elif clas=="Economy":
                op+=5300
                c+=op                                          
        for i in range(s):
            if re[i]>=13:
                ad+=1
            else:
                ch+=1
                
        print(c)
        inform.destroy()
        global bankin        
        bankin=Tk()
        bankin.attributes('-fullscreen',True)
        bankin.title("banking")
        C=PhotoImage(file="money.png")
        label2=Label(bankin,image=C)
        label2.place(relx = 0.5,rely = 0.5, anchor ='center')
        label2.image =C
        label2.pack
        Title=Label(bankin,text="PAYMENT",font=("arial bold",45),bg="Black",fg="White")
        Title.place(relx=0.4,rely=0.05)
        df=Label(bankin,text="AMOUNT TO BE PAYED",font=("arial bold",25),bg="Black",fg="White")
        df.place(relx=0.1,rely=0.2)
        rf=Label(bankin,text="Rs"+str(c),font=("arial bold",25),bg="Black",fg="red")
        rf.place(relx=0.4,rely=0.19)
        be1=Button(bankin,text="Back",fg="White",bg="Black",command=start1)
        be1.place(relx=0.1,rely=0.9)
        be1['font']=myFont
        ef=Label(bankin,text="CHOOSE A BANK",font=("arial bold",25),bg="Black",fg="White")
        ef.place(relx=0.1,rely=0.3)
        t=StringVar()
        io=Radiobutton(bankin,text="ICICI",variable=t,value="ICICI",bg="Black",fg="White",font=("arial bold",20))
        io.place(relx=0.1,rely=0.4)
        io1=Radiobutton(bankin,text="SBI",variable=t,value="SBI",bg="Black",fg="White",font=("arial bold",20))
        io1.place(relx=0.1,rely=0.5)
        io2=Radiobutton(bankin,text="HDFC",variable=t,value="HDFC",bg="Black",fg="White",font=("arial bold",20))
        io2.place(relx=0.1,rely=0.6)
        br=Button(bankin,text="Continue",fg="White",bg="Black",command=payment_mode)
        br.place(relx=0.9,rely=0.9)
        br['font']=myFont
               
    def input_information():
        try:
            userportal.destroy()      
        except:
            try:
                cav.destroy()
            except:
                print()

        global inform
        e2=int(children.get())+int(adult.get())+int(infants.get())
        e.append(e2)
        windowAa.destroy()
        inform=Tk()
        inform.attributes('-fullscreen',True)
        inform.title("Input Information")
        inform.configure(bg="Light Pink")
        photo=PhotoImage(file="project.png")
        label=Label(inform,image=photo)
        label.place(relx = 0.94,rely = 0.1, anchor ='center')
        label.image = photo
        label.pack
        b=Label(inform,text="Enter the Details",fg="White",bg="Black",font=("Arial Bold",45))
        b.place(relx=0.5,rely=0.1,anchor='center')           
        for j in range (11):          
            if e2==j:
                for i in range(j):
                    ne=[]
                    o1=Label(inform,text="Name",font=("Arial Bold",15))
                    o1.place(relx=0.11,rely=0.3+(i/10))
                    o1.configure(fg="Black",bg="Light Pink")
                    o2=Entry(inform,width=15,font=('Arial Bold',15))
                    o2.place(relx=0.15,rely=0.3+(i/10))
                    age=Label(inform,text="Age",font=("Arial Bold",15))
                    age.place(relx=0.27,rely=0.3+(i/10))
                    age.configure(fg="Black",bg="Light Pink")
                    age1=Entry(inform,width=15,font=('Arial Bold',15))
                    age1.place(relx=0.3,rely=0.3+(i/10))               
                    ge=Label(inform,text="Gender",font=("Arial Bold",15))
                    ge.place(relx=0.4,rely=0.3+(i/10))
                    ge.configure(fg="Black",bg="Light Pink")
                    ge1=ttk.Combobox(inform,values=["Male","Female","Transgender"])
                    ge1.place(relx=0.45,rely=0.3+(i/10))
                    Class=Label(inform,text="Select Class",font=("Arial Bold",15))
                    Class.place(relx=0.55,rely=0.3+(i/10))
                    Class.configure(fg="Black",bg="Light Pink")
                    Class1=ttk.Combobox(inform,values=['Business','Economy'])
                    Class1.place(relx=0.64,rely=0.3+(i/10))
                    Class1.current()
                    teach.append(Class1)
                    pre=Label(inform,text="Select your seat",font=("Arial Bold",15))
                    pre.place(relx=0.74,rely=0.3+(i/10))
                    pre.configure(fg="Black",bg="Light Pink")
                    pre1=ttk.Combobox(inform,values=Flightseat)
                    pre1.place(relx=0.86,rely=0.3+(i/10))
                    pre1.current()
                    bu1=Button(inform,text="Back",fg="White",bg="Black",command=inform.destroy)
                    bu1.place(relx=0.4,rely=0.8,anchor="center")
                    bu1['font']=myFont
                    bu2=Button(inform,text="Proceed",fg="White",bg="Black",command=banking)
                    bu2.place(relx=0.6,rely=0.8,anchor="center")
                    bu2['font']=myFont
                    ne.append(o2)
                    ne.append(age1)
                    ne.append(ge1)
                    ne.append(Class1)
                    ne.append(pre1)
                    Airwayspassenger.append(ne)
                                  
    def comsearchit():
        
        def namecheck():
            qwe=d1.get()
            iru=0
            for i in range(len(m)):
                if qwe==m[i][1]:
                    input_information()
                    root.destroy()
                    iru+=1
            if iru ==0:
                messagebox.showinfo("Oops!","Give a Flight name which is the chart")
                root.destroy()

        global available        
        m=[]
        of=userfrom.get()
        ot=userto.get()
        dateo=day.get()+" "+month.get()+" "+year.get()
        f=open("Airways.csv",'r')
        lab=tom=0
        robj=csv.reader(f,delimiter=",")
        for a in robj:
            if tom%2==0:
                if a[2]==of and a[3]==ot and dateo==a[4]:
                    m.append(a)
                    lab+=1
            tom+=1

        if lab==0:
            messagebox.showinfo("Oops!","No Flight found")
    
        class Table:       
            def __init__(self,root):
                for i in range(10,total_rows+10):
                    for j in range(10,total_columns+10):
                        self.e = Entry(root, width=17, fg='blue', 
                                        font=('Arial',15,'bold'))                   
                        self.e.grid(row=i+1, column=j+1)
                        self.e.insert(END, m[i-10][j-10])  

        total_rows = len(m) 
        total_columns = len(m[0])
        root = Tk()
        root.attributes('-fullscreen',True)
        root.title("Airways chart")
        root.configure(bg ="Light blue")
        l1=Label(root,text="Available Flights",font=("Arial Bold",45))
        l1.configure(fg="Black",bg="Light blue")
        l1.place(relx=0.5, rely=0.05, anchor="center")
        goq='Flight No.  \t  Flight Name\t  Origin\t\tDestination\t  Departure\t    Arrival\t\tStatus'        
        l2=Label(root,text=goq,font=("Arial Bold",17))
        l2.configure(fg="Black",bg="Light Blue")
        l2.place(relx=0.43, rely=0.15, anchor="center")
        for r in range(9):
            bi=Label(root,text="   ",bg="Light blue")
            bi.grid(row=r,column=0)
        bi2=Label(root,text="Enter the name of the Flight you want to book",font=("Arial Bold",20))        
        bi2.place(relx=0.1,rely=0.6)
        bi2.configure(fg="Black",bg="Light Blue")
        d1=Entry(root,bg="white",fg="blue",width=25,font=('Arial Bold',20))
        d1.place(relx=0.5,rely=0.6)
        bt=Button(root,text="Book",fg="White",bg="Black",command=namecheck)
        bt.place(relx=0.3,rely=0.8,anchor="c")
        bt['font']=myFont 
        bt2=Button(root,text="Back",fg="White",bg="Black",command=root.destroy)
        bt2.place(relx=0.7,rely=0.8,anchor="c")
        bt2['font']=myFont
        t = Table(root)
        available=m
        root.mainloop()           

    try:
        userportal.destroy()      
    except:
        try:
            cav.destroy()
        except:
            print()

    global windowAa             
    windowAa=Tk()
    windowAa.title("MRF.com/Guest/choosing mode of transport/Airways")
    windowAa.attributes('-fullscreen',True)
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="1307258.png")
    label2=Label(windowAa,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(windowAa,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    lc=Label(windowAa,text='Enter the required details',font=("Arial Bold",45))
    lc.place(relx = 0.3, rely = 0.1)
    lc.configure(fg="White",bg="Black")
    l1=Label(windowAa,text='From:',font=("Arial Bold",20))
    l1.place(relx = 0.25, rely = 0.35)
    l1.configure(fg="White",bg="Black")
    userfrom=ttk.Combobox(windowAa,values=Airwaysdestination)
    userfrom.place(relx = 0.295, rely = 0.4, anchor = 'c')
    userfrom.current()
    l2=Label(windowAa,text='To:',font=("Arial Bold",20))
    l2.place(relx = 0.25, rely = 0.55)
    l2.configure(fg="White",bg="Black")
    userto=ttk.Combobox(windowAa,values=Airwaysdestination)
    userto.place(relx = 0.295, rely = 0.6, anchor = 'c')
    userto.current()
    ld=Label(windowAa,text='Day:',font=("Arial Bold",20))
    ld.place(relx = 0.65, rely = 0.35)
    ld.configure(fg="White",bg="Black")
    day=ttk.Combobox(windowAa,values=vai)
    day.place(relx = 0.695, rely = 0.4, anchor = 'c')
    day.current()
    l3=Label(windowAa,text='Month:',font=("Arial Bold",20))
    l3.place(relx = 0.75, rely = 0.35)
    l3.configure(fg="White",bg="Black")
    month=ttk.Combobox(windowAa,values=['January','February','March',
                                       'April','May','June','July',
                                       'August','September','October',
                                       'November','December'])
    month.place(relx = 0.795, rely = 0.4, anchor = 'c')
    month.current()
    l4=Label(windowAa,text='Year:',font=("Arial Bold",20))
    l4.place(relx = 0.85, rely = 0.35)
    l4.configure(fg="White",bg="Black")
    year=ttk.Combobox(windowAa,values=['2020','2021','2022'])
    year.place(relx = 0.895, rely = 0.4, anchor = 'c')
    year.current()
    adult=ttk.Combobox(windowAa,values=['0','1','2','3','4','5','6','7','8','9'])
    adult.place(relx = 0.695, rely = 0.605, anchor = 'c')
    l5=Label(windowAa,text='Adults:',font=("Arial Bold",20))
    l5.place(relx = 0.65, rely = 0.55)
    l5.configure(fg="White",bg="Black")
    children=ttk.Combobox(windowAa,values=['0','1','2','3','4','5','6','7','8','9'])
    children.place(relx = 0.795, rely = 0.605, anchor = 'c')
    l6=Label(windowAa,text='Children(2-11yrs):',font=("Arial Bold",20))
    l6.place(relx = 0.75, rely =0.55)
    l6.configure(fg="White",bg="Black")
    infants=ttk.Combobox(windowAa,values=['0','1'])
    infants.place(relx = 0.695, rely = 0.7055, anchor='c')
    l7=Label(windowAa,text='Infants(below 2yrs):',font=("Arial Bold",20))
    l7.place(relx = 0.65, rely = 0.65)
    l7.configure(fg="White",bg="Black")
    bt=Button(windowAa,text="Back",fg="White",bg="Black",command=start1)
    bt.place(relx=0.1,rely=0.88)
    bt['font']=myFont
    bt2=Button(windowAa,text="Search",fg="White",bg="Black",command=comsearchit)
    bt2.place(relx=0.5,rely=0.9,anchor="c")
    bt2['font']=myFont
    
def Roadways_booking():
    
    def banking():

        def bill():
            
            thisis=[]
            ohm=[]
            ay=[]
            global bil        
            bil=Tk()   
            bil.attributes('-fullscreen',True)
            bil.title("bill")
            bil.configure(bg ="light blue")
            beu1=Button(bil,text="Back",fg="White",bg="Black",command=start1)
            beu1.place(relx=0.5,rely=0.9)
            beu1['font']=myFont
            dr=Label(bil,text="Ticket Conformation",font=("arial bold",30),bg="light blue",fg="black")
            dr.place(relx=0.01,rely=0.01)
            rr=Label(bil,text="Congratulations!! Thank you for using MRF's online Bus reservation facility.",font=("arial bold",20),bg="light blue",fg="black")
            tt=Label(bil,text="Your Booking Details are Indicated Below:",font=("arial bold",20),bg="light blue",fg="black")
            rr.place(relx=0.01,rely=0.08)
            tt.place(relx=0.01,rely=0.15)
            j123=Label(bil,text="PNR Number:",font=("arial bold",19),bg="light blue",fg="black")
            j123.place(relx=0.75,rely=0.01)
            pnrr=random.randint(1000000000,9999999999)
            pnr.append(str(pnrr))
            k123=Label(bil,text=pnrr,font=("arial bold",19),bg="light blue",fg="black")
            k123.place(relx=0.85,rely=0.01)
            j=Label(bil,text="Bus No:",font=("arial bold",19),bg="light blue",fg="black")
            j.place(relx=0.01,rely=0.20)
            k=Label(bil,text=available[0][0],font=("arial bold",19),bg="light blue",fg="black")
            k.place(relx=0.16,rely=0.20) 
            current_time = datetime.datetime.now() 
            j2=Label(bil,text="Date and Time of booking:",font=("arial bold",19),bg="light blue",fg="black")
            j2.place(relx=0.4,rely=0.20)
            konga=Label(bil,text=current_time,font=("arial bold",19),bg="light blue",fg="black")
            konga.place(relx=0.6,rely=0.20)
            y1=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
            y1.place(relx=0.01,rely=0.25)
            j3=Label(bil,text="From:",font=("arial bold",19),bg="light blue",fg="black")
            j3.place(relx=0.01,rely=0.30)
            k3=Label(bil,text=available[0][2],font=("arial bold",19),bg="light blue",fg="black")
            k3.place(relx=0.1,rely=0.30)
            j4=Label(bil,text="Departure:",font=("arial bold",19),bg="light blue",fg="black")
            j4.place(relx=0.3,rely=0.30)
            k4=Label(bil,text=available[0][4],font=("arial bold",19),bg="light blue",fg="black")
            k4.place(relx=0.4,rely=0.30)
            j5=Label(bil,text="To:",font=("arial bold",19),bg="light blue",fg="black")
            j5.place(relx=0.6,rely=0.30)
            k5=Label(bil,text=available[0][3],font=("arial bold",19),bg="light blue",fg="black")
            k5.place(relx=0.7,rely=0.30)  
            y2=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
            y2.place(relx=0.01,rely=0.35)        
            j6=Label(bil,text="Arrival:",font=("arial bold",19),bg="light blue",fg="black")
            j6.place(relx=0.01,rely=0.40)
            k6=Label(bil,text=available[0][4],font=("arial bold",19),bg="light blue",fg="black")
            k6.place(relx=0.1,rely=0.40)            
            j7=Label(bil,text="Number of Passengers:",font=("arial bold",19),bg="light blue",fg="black")
            j7.place(relx=0.3,rely=0.40)
            k8=Label(bil,text=ad+ch,font=("arial bold",19),bg="light blue",fg="black")
            k8.place(relx=0.5,rely=0.40)
            y3=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
            y3.place(relx=0.01,rely=0.44)
            j10=Label(bil,text="Passenger details:",font=("arial bold",30),bg="light blue",fg="black")
            j10.place(relx=0.01,rely=0.50)
            j11=Label(bil,text="S.I",font=("arial bold",19),bg="light blue",fg="black")
            j11.place(relx=0.01,rely=0.57)
            for i in range(s):
                    k11=Label(bil,text=(i+1),font=("arial bold",15),bg="light blue",fg="black")
                    k11.place(relx=0.01,rely=0.60+(i/30))            
            j12=Label(bil,text="Name",font=("arial bold",19),bg="light blue",fg="black")
            j12.place(relx=0.1,rely=0.57)
            for i in range(s):
                    kola=Roadwayspassenger[i][0]
                    print(kola)
                    k12=Label(bil,text=go[i],font=("arial bold",15),bg="light blue",fg="black")
                    k12.place(relx=0.1,rely=0.60+(i/30))                    
            j13=Label(bil,text="Age",font=("arial bold",19),bg="light blue",fg="black")
            j13.place(relx=0.25,rely=0.57)
            for i in range(s):
                    k13=Label(bil,text=re[i],font=("arial bold",15),bg="light blue",fg="black")
                    k13.place(relx=0.25,rely=0.60+(i/30))            
            j14=Label(bil,text="Gender",font=("arial bold",19),bg="light blue",fg="black")
            j14.place(relx=0.35,rely=0.57)
            for i in range(s):
                    k14=Label(bil,text=bo[i],font=("arial bold",15),bg="light blue",fg="black")
                    k14.place(relx=0.35,rely=0.60+(i/30))
            j14=Label(bil,text="Class",font=("arial bold",19),bg="light blue",fg="black")
            j14.place(relx=0.45,rely=0.57)
            for i in range(s):
                    k14=Label(bil,text=co[i],font=("arial bold",15),bg="light blue",fg="black")
                    k14.place(relx=0.45,rely=0.60+(i/30))                    
            j16=Label(bil,text="Seat",font=("arial bold",19),bg="light blue",fg="black")
            j16.place(relx=0.55,rely=0.57)
            for i in range(s):
                k14=Label(bil,text=se[i],font=("arial bold",15),bg="light blue",fg="black")
                k14.place(relx=0.55,rely=0.60+(i/30))             
            y4=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
            y4.place(relx=0.01,rely=0.74)
            j17=Label(bil,text="Fare Details:",font=("arial bold",30),bg="light blue",fg="black")
            j17.place(relx=0.01,rely=0.77)
            j18=Label(bil,text="Ticket Fee",font=("arial bold",19),bg="light blue",fg="black")
            j18.place(relx=0.01,rely=0.84)
            k18=Label(bil,text=c,font=("arial bold",25),bg="light blue",fg="black")
            k18.place(relx=0.01,rely=0.87)
            j19=Label(bil,text="Convenience Fee",font=("arial bold",19),bg="light blue",fg="black")
            j19.place(relx=0.2,rely=0.84)
            k19=Label(bil,text=s*15,font=("arial bold",25),bg="light blue",fg="black")
            k19.place(relx=0.2,rely=0.87)
            j20=Label(bil,text="Total Fee",font=("arial bold",19),bg="light blue",fg="black")
            j20.place(relx=0.4,rely=0.84)
            k20=Label(bil,text=c+(s*15),font=("arial bold",25),bg="light blue",fg="black")
            k20.place(relx=0.4,rely=0.87)
            thisis.append(go)
            thisis.append(re)
            thisis.append(bo)
            thisis.append(co)
            thisis.append(se)                    
            print(thisis)
            okq=available[0][1]+'.csv'
            fq=open(okq,'a')
            wobj=csv.writer(fq,delimiter=',')
            for i in range(0,s):
                wobj.writerow([thisis[0][i],thisis[1][i],thisis[2][i],thisis[3][i],thisis[4][i]])   
            fq.close()
            teach.pop()            
                
        def payment_mode():

            def debit_card():
                
                def debit_check():
                    num1=cardno.get()
                    num2=pinno.get()
                    if num1 in debit and num2 in debit:
                        bill()
                        debitwindow.destroy()
                    else: 
                        messagebox.showwarning("Attention","Numbers do not match")
                        debitwindow.destroy()
                        
                paymentwindow.destroy()    
                debitwindow=Tk()
                debitwindow.title("payment mode")
                debitwindow.attributes('-fullscreen',True) 
                debitwindow.configure(bg ="light Blue")
                deb1=Label(debitwindow,text="Enter required credentials to enter the portal",font=("Arial Bold",25))
                deb1.configure(fg="Black",bg="light Blue")
                deb1.place(relx=0.55,rely=0.2,anchor="center")
                lb0=Label(debitwindow,text="Amount:",font=("Arial Bold",25))
                lb0.configure(fg="black",bg="light blue")
                lb0.place(relx=0.45,rely=0.1)
                lbb0=Label(debitwindow,text=c+(s*15),font=("Arial Bold",25))
                lbb0.configure(fg="Red",bg="light blue")
                lbb0.place(relx=0.65,rely=0.1) 
                deb2=Label(debitwindow,text="Enter number in D",font=("Arial",20))
                deb2.place(relx=0.4,rely=0.4,anchor="center")
                deb2.configure(fg="Black",bg="Light Blue")
                cardno=Entry(debitwindow,show="*",width=10,font=('Arial Bold',15))
                cardno.place(relx=0.65,rely=0.4,anchor="center")
                deb3=Label(debitwindow,text="Enter number in M",font=("Arial",20))
                deb3.place(relx=0.4,rely=0.45,anchor="center")
                deb3.configure(fg="Black",bg="Light Blue")
                pinno=Entry(debitwindow,show="*",width=10,font=('Arial Bold',15))
                pinno.place(relx=0.65,rely=0.45,anchor="center")
                du1=Button(debitwindow,text="Submit",fg="White",bg="Black",command=debit_check)
                du1.place(relx=0.55,rely=0.5,anchor="center")
                du1['font']=myFont      
                du2=Button(debitwindow,text="Back",fg="White",bg="Black",command=debitwindow.destroy)
                du2.place(relx=0.65,rely=0.5,anchor="center")
                du2['font']=myFont  

            def bank_login():
                    
                def bankidpassword():
                    c=0
                    num1=usename.get()
                    num2=password1.get()
                    for i in range(len(banklogin)):
                        if num1 in banklogin[i][0] and num2 in banklogin[i][1]:
                            c+=1
                    if c==1:
                        bill()
                        banklog.destroy()
                    else: 
                        messagebox.showwarning("Attention","Invalid Username or Password!")
                        banklog.destroy()
                        
                paymentwindow.destroy()
                banklog=Tk()       
                banklog.attributes('-fullscreen',True)
                banklog.title("bank login")
                banklog.configure(bg ="light blue")
                lb0=Label(banklog,text="Amount:",font=("Arial Bold",25))
                lb0.configure(fg="black",bg="light blue")
                lb0.place(relx=0.45,rely=0.1)
                lbb0=Label(banklog,text=c+(s*15),font=("Arial Bold",25))
                lbb0.configure(fg="Red",bg="Light Blue")
                lbb0.place(relx=0.65,rely=0.1)        
                lb1=Label(banklog,text="Enter required  bank credentials for payment",font=("Arial",25))
                lb1.configure(fg="Black",bg="Light Blue")
                lb1.place(relx=0.55,rely=0.2,anchor="center")
                lb2=Label(banklog,text="Username",font=("Arial",20))
                lb2.place(relx=0.5,rely=0.4,anchor="center")
                lb2.configure(fg="Black",bg="Light Blue")
                usename=Entry(banklog,width=10,font=('Arial Bold',15))
                usename.place(relx=0.6,rely=0.4,anchor="center")
                lb3=Label(banklog,text="Password",font=("Arial",20))
                lb3.place(relx=0.5,rely=0.45,anchor="center")
                lb3.configure(fg="Black",bg="Light Blue")
                password1=Entry(banklog,show="*",width=10,font=('Arial Bold',15))
                password1.place(relx=0.6,rely=0.45,anchor="center")
                bue1=Button(banklog,text="Submit",fg="White",bg="Black",command=bankidpassword)
                bue1.place(relx=0.55,rely=0.5,anchor="center")
                bue1['font']=myFont
                bue2=Button(banklog,text="Back",fg="White",bg="Black",command=banklog.destroy)
                bue2.place(relx=0.65,rely=0.5,anchor="center")
                bue2['font']=myFont             
                
            paymentwindow=Tk()
            paymentwindow.title("payment mode")
            paymentwindow.attributes('-fullscreen',True) 
            paymentwindow.configure(bg ="Light Blue")
            pa1=Button(paymentwindow,text="Net banking",fg="White",bg="Black",command=bank_login)
            pa1.place(relx=0.5,rely=0.4,anchor="center")
            pa1['font']=myFont
            pa2=Button(paymentwindow,text="Debit card",fg="White",bg="Black",command=debit_card)
            pa2.place(relx=0.5,rely=0.66,anchor="center")
            pa2['font']=myFont 
            p1=Label(paymentwindow,text="Payment Mode",font=("Arial Bold",45))
            p1.configure(fg="Black",bg="Light Blue")
            p1.place(relx=0.5, rely=0.12, anchor="center")
            p2=Button(paymentwindow,text="Back",fg="White",bg="Black",command=paymentwindow.destroy)
            p2.place(relx=0.05,rely=0.9,anchor="center")
            p2['font']=myFont 
                           
        try:
            userportal.destroy()      
        except:
            try:
                cav.destroy()
            except:
                 print()
        
        global ad
        global ch
        global c
        c=0
        ad=0
        ch=0
        clas=teach[0].get()
        global s
        s=e[0]
        re=[]
        go=[]
        bo=[]
        se=[]
        co=[]
        for i in range (s):
            go.append(Roadwayspassenger[i][0].get())
            bo.append(Roadwayspassenger[i][2].get())
            co.append(Roadwayspassenger[i][3].get())
            se.append(Roadwayspassenger[i][4].get()) 
        for i in range(s):
            gh=0
            gh+=int(Roadwayspassenger[i][1].get())
            re.append(gh)
        print(re)
        
        for i in range(s):        
            op=0
            if re[i]<=13  or  re[i]>=60 :
                if clas=="A/C Sleeper":             
                    op+=1000
                    c+=op
                    print(c)
                elif clas=="A/C Non sleeper":
                    op+=750
                    c+=op
                elif clas=="Non A/C Sleeper":
                    op+=500
                    c+=op
                elif  clas=="Non A/C Non Sleeper":
                    op+=250
                    c+=op                                            
            else:
                    
                if clas=="A/C Sleeper":
                    op+=2000
                    c+=op                
                elif clas=="A/C Non sleeper":
                    op+=1500
                    c+=op
                elif clas=="Non A/C Sleeper":
                    op+=1000
                    c+=op
                elif  clas=="Non A/C Non Sleeper":
                    op+=500
                    c+=op
                        
        for i in range(s):
            if re[i]>=13:
                ad+=1
            else:
                ch+=1                                   
        print(c)
        inform.destroy()                 
        global bankin        
        bankin=Tk()
        bankin.attributes('-fullscreen',True)
        bankin.title("banking")
        C=PhotoImage(file="money.png")
        label2=Label(bankin,image=C)
        label2.place(relx = 0.5,rely = 0.5, anchor ='center')
        label2.image =C
        label2.pack
        Title=Label(bankin,text="PAYMENT",font=("arial bold",45),bg="Black",fg="White")
        Title.place(relx=0.4,rely=0.05)
        df=Label(bankin,text="AMOUNT TO BE PAYED",font=("arial bold",25),bg="Black",fg="White")
        df.place(relx=0.1,rely=0.2)
        rf=Label(bankin,text="Rs"+str(c),font=("arial bold",25),bg="Black",fg="red")
        rf.place(relx=0.4,rely=0.19)
        be1=Button(bankin,text="Back",fg="White",bg="Black",command=start1)
        be1.place(relx=0.1,rely=0.9)
        be1['font']=myFont
        ef=Label(bankin,text="CHOOSE A BANK",font=("arial bold",25),bg="Black",fg="White")
        ef.place(relx=0.1,rely=0.3)
        t=StringVar()
        io=Radiobutton(bankin,text="ICICI",variable=t,value="ICICI",bg="Black",fg="White",font=("arial bold",20))
        io.place(relx=0.1,rely=0.4)
        io1=Radiobutton(bankin,text="SBI",variable=t,value="SBI",bg="Black",fg="White",font=("arial bold",20))
        io1.place(relx=0.1,rely=0.5)
        io2=Radiobutton(bankin,text="HDFC",variable=t,value="HDFC",bg="Black",fg="White",font=("arial bold",20))
        io2.place(relx=0.1,rely=0.6)
        br=Button(bankin,text="Continue",fg="White",bg="Black",command=payment_mode)
        br.place(relx=0.9,rely=0.9)
        br['font']=myFont
    
    def input_information():
        
        try:
            userportal.destroy()      
        except:
            try:
                cav.destroy()
            except:
                print()
        global inform
        so=int(e2.get())
        e.append(so)
        windowra.destroy()
        inform=Tk()
        inform.attributes('-fullscreen',True)
        inform.title("Input information")
        inform.configure(bg="Light pink")
        photo=PhotoImage(file="project.png")
        label=Label(inform,image=photo)
        label.place(relx = 0.94,rely = 0.1, anchor ='center')
        label.image = photo
        label.pack
        l1=Label(inform,text="Enter the Details",font=("Arial Bold",45))
        l1.configure(fg="Black",bg="Light Pink")
        l1.place(relx=0.5,rely=0.1,anchor='center')   
        for j in range (11):
            if so==j:
                for i in range(j):
                    ne=[]
                    o1=Label(inform,text="Name",font=("Arial Bold",15))
                    o1.place(relx=0.11,rely=0.3+(i/10))
                    o1.configure(fg="Black",bg="Light Pink")
                    o2=Entry(inform,width=15,font=('Arial Bold',15))
                    o2.place(relx=0.15,rely=0.3+(i/10))
                    age=Label(inform,text="Age",font=("Arial Bold",15))
                    age.place(relx=0.27,rely=0.3+(i/10))
                    age.configure(fg="Black",bg="Light Pink")
                    age1=Entry(inform,width=15,font=('Arial Bold',15))
                    age1.place(relx=0.3,rely=0.3+(i/10))               
                    ge=Label(inform,text="Gender",font=("Arial Bold",15))
                    ge.place(relx=0.4,rely=0.3+(i/10))
                    ge.configure(fg="Black",bg="Light Pink")
                    ge1=ttk.Combobox(inform,values=["Male","Female","Transgender"])
                    ge1.place(relx=0.45,rely=0.3+(i/10))
                    Class=Label(inform,text="Select Class",font=("Arial Bold",15))
                    Class.place(relx=0.55,rely=0.3+(i/10))
                    Class.configure(fg="Black",bg="Light Pink")
                    Class1=ttk.Combobox(inform,values=['A/C Sleeper','A/C Non sleeper','Non A/C Sleeper','Non A/C Non Sleeper'])
                    Class1.place(relx=0.64,rely=0.3+(i/10))
                    teach.append(Class1)
                    pre=Label(inform,text="Select your seat",font=("Arial Bold",15))
                    pre.configure(fg="Black",bg="Light Pink")
                    pre.place(relx=0.74,rely=0.3+(i/10))
                    pre1=ttk.Combobox(inform,values=busseat) 
                    pre1.place(relx=0.86,rely=0.3+(i/10))
                    pre1.current()
                    bu1=Button(inform,text="Back",fg="White",bg="Black",command=inform.destroy)
                    bu1.place(relx=0.4,rely=0.8,anchor="center")
                    bu1['font']=myFont 
                    bu2=Button(inform,text="Proceed",fg="White",bg="Black",command=banking)
                    bu2.place(relx=0.6,rely=0.8,anchor="center")
                    bu2['font']=myFont
                    ne.append(o2)
                    ne.append(age1)
                    ne.append(ge1)
                    ne.append(Class1)
                    ne.append(pre1)
                    Roadwayspassenger.append(ne)
    
    def comsearchit():
        def namecheck():
            qwe=d1.get()
            iru=0
            for i in range(len(m)):
                if qwe==m[i][1]:
                    input_information()
                    root.destroy()
                    iru+=1
            if iru ==0:
                messagebox.showinfo("Oops!","Give a Bus name which is the chart")
                root.destroy()
                
        global available        
        m=[]
        of=userfrom.get()
        ot=userto.get()
        dateo=day.get()+" "+month.get()+" "+year.get()
        f=open("Roadways.csv",'r')
        lab=tom=0        
        robj=csv.reader(f,delimiter=",")
        for a in robj:
            if tom%2==0:
                if a[2]==of and a[3]==ot and dateo==a[4]:
                    m.append(a)
                    lab+=1
            tom+=1
        print(m)
        if lab==0:
            messagebox.showinfo("Oops!","No Bus found")
    
        class Table:       
            def __init__(self,root):
                for i in range(10,total_rows+10):
                    for j in range(10,total_columns+10):
                        self.e = Entry(root, width=17, fg='blue', 
                                        font=('Arial',15,'bold'))                   
                        self.e.grid(row=i+1, column=j+1)
                        self.e.insert(END, m[i-10][j-10])
        total_rows = len(m) 
        total_columns = len(m[0])
        root = Tk()
        root.attributes('-fullscreen',True)
        root.title("Roadways chart")
        root.configure(bg ="Light Blue")
        l1=Label(root,text="Available Buses",font=("Arial Bold",45))
        l1.configure(fg="Black",bg="Light Blue")
        l1.place(relx=0.5, rely=0.05, anchor="center")
        goq='Bus No.  \t  Bus Name\t  Origin\t\tDestination\t  Departure\t    Arrival\t\tStatus'        
        l2=Label(root,text=goq,font=("Arial Bold",17))
        l2.configure(fg="Black",bg="Light Blue")
        l2.place(relx=0.43, rely=0.15, anchor="center")
        for r in range(9):
            bi=Label(root,text="   ",bg="Light blue")
            bi.grid(row=r,column=0)            
        bi2=Label(root,text="Enter the name of the Bus you want to book",font=("Arial Bold",20))        
        bi2.place(relx=0.1,rely=0.6)
        bi2.configure(fg="Black",bg="Light Blue")
        d1=Entry(root,bg="white",fg="blue",width=25,font=('Arial Bold',20))
        d1.place(relx=0.5,rely=0.6)   
        bt2=Button(root,text="Book",fg="White",bg="Black",command=namecheck)
        bt2.place(relx=0.7,rely=0.7,anchor="c")
        bt2['font']=myFont
        bt3=Button(root,text="Back",fg="White",bg="Black",command=root.destroy)
        bt3.place(relx=0.3,rely=0.7,anchor="c")
        bt3['font']=myFont
        t = Table(root)
        available=m
        root.mainloop()
    try:
        userportal.destroy()      
    except:
        try:
            cav.destroy()
        except:
            print()

    global windowra                   
    windowra=Tk()    
    windowra.title("MRF.com/Guest/choosing mode of transport/Airways")
    windowra.attributes('-fullscreen',True)
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="roadw.png")
    label2=Label(windowra,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(windowra,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack   
    lc=Label(windowra,text='Enter the required details',font=("Arial Bold",45))
    lc.place(relx = 0.3, rely = 0.14)
    lc.configure(fg="White",bg="Black") 
    l1=Label(windowra,text='From:',font=("Arial Bold",20))
    l1.place(relx = 0.25, rely = 0.35)
    l1.configure(fg="White",bg="Black")
    userfrom=ttk.Combobox(windowra,values=Roadwaysdestination)
    userfrom.place(relx = 0.295, rely = 0.4, anchor = 'c')
    userfrom.current()
    l2=Label(windowra,text='To:',font=("Arial Bold",20))
    l2.place(relx = 0.25, rely = 0.55)
    l2.configure(fg="White",bg="Black")
    userto=ttk.Combobox(windowra,values=Roadwaysdestination)
    userto.place(relx = 0.295, rely = 0.6, anchor = 'c')
    userto.current()
    ld=Label(windowra,text='Day:',font=("Arial Bold",20))
    ld.place(relx = 0.65, rely = 0.35)
    ld.configure(fg="White",bg="Black")
    day=ttk.Combobox(windowra,values=vai)
    day.place(relx = 0.695, rely = 0.4, anchor = 'c')
    day.current()
    l3=Label(windowra,text='Month:',font=("Arial Bold",20))
    l3.place(relx = 0.75, rely = 0.35)
    l3.configure(fg="White",bg="Black")
    month=ttk.Combobox(windowra,values=['January','February','March',
                                       'April','May','June','July',
                                       'August','September','October',
                                       'November','December'])
    month.place(relx = 0.795, rely = 0.4, anchor = 'c')
    month.current()
    l4=Label(windowra,text='Year:',font=("Arial Bold",20))
    l4.place(relx = 0.85, rely = 0.35)
    l4.configure(fg="White",bg="Black")
    year=ttk.Combobox(windowra,values=['2020','2021','2022'])
    year.place(relx = 0.895, rely = 0.4, anchor = 'c')
    year.current()
    l5=Label(windowra,text='Number of Passengers:',font=("Arial Bold",20))
    l5.place(relx = 0.65, rely = 0.55)
    l5.configure(fg="White",bg="Black")
    e2=ttk.Combobox(windowra,values=['0','1','2','3','4','5','6','7','8','9','10'])
    e2.place(relx = 0.695, rely = 0.6, anchor = 'c')
    e2.current()
    bt=Button(windowra,text="Back",fg="White",bg="Black",command=start1)
    bt.place(relx=0.1,rely=0.88)
    bt['font']=myFont
    bt2=Button(windowra,text="Search",fg="White",bg="Black",command=comsearchit)
    bt2.place(relx=0.5,rely=0.9,anchor="c")
    bt2['font']=myFont

def Registration():

    def searchuserlist():
        un=ususer.get()
        u=uspass.get()
        u1=uspass1.get()
        k=0
        for aaw in userlogin:
            if aaw[0]==un:
                print(un)
                k+=1
                messagebox.showinfo("Sorry","Username already exists")
            elif u1!=u:
                messagebox.showinfo("Oops!","Your passwords does not match")
        if k==0 and u1==u:
            userlogin.append([un,u])
            messagebox.showinfo("Sucess","You are now a registered user. Now try loging in with your Username and password")
            reg.destroy()
            user_login()

    try:
        userwindow.destroy()      
    except:
        try:
            windowA.destroy()
        except:
            try:
                windowR.destroy()
            except:
                try:
                    windowr.destroy()
                except:
                    print()
        
    global reg            
    reg=Tk()
    reg.attributes('-fullscreen',True)
    reg.title("Registration")
    reg.configure(bg="Light pink")
    myFont = font.Font(size=20)
    photo=PhotoImage(file="project.png")
    label=Label(reg,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack   
    l1=Label(reg,text="Registration Portal",font=("Arial Bold",45))
    l1.configure(fg="Black",bg="Light pink")
    l1.place(relx=0.5, rely=0.04, anchor="center")
    l2=Label(reg,text="Enter the required credentials",font=("Arial Bold",25))
    l2.configure(fg="Black",bg="Light pink")
    l2.place(relx=0.5, rely=0.13,anchor="center")
    l3=Label(reg,text="Name",font=("Arial Bold",20))
    l3.configure(fg="Black",bg="Light pink")
    l3.place(relx=0.1, rely=0.2, anchor="center")
    usname=Entry(reg,width=25,font=('Arial Bold',20))
    usname.place(relx=0.3,rely=0.2, anchor="center")                           
    l4=Label(reg,text="Age",font=("Arial Bold",20))
    l4.configure(fg="Black",bg="Light pink")
    l4.place(relx=0.5, rely=0.2, anchor="center")
    usage=Entry(reg,width=25,font=('Arial Bold',20))
    usage.place(relx=0.7,rely=0.2, anchor="center")
    l5=Label(reg,text="Address",font=("Arial Bold",20))
    l5.configure(fg="Black",bg="Light pink")
    l5.place(relx=0.1, rely=0.4, anchor="center")
    usadd=Entry(reg,width=25,font=('Arial Bold',20))
    usadd.place(relx=0.3,rely=0.4, anchor="center")
    l6=Label(reg,text="Phone Number",font=("Arial Bold",20))
    l6.configure(fg="Black",bg="Light pink")
    l6.place(relx=0.5, rely=0.4, anchor="center")
    usph=Entry(reg,width=25,font=('Arial Bold',20))
    usph.place(relx=0.7,rely=0.4, anchor="center")
    l7=Label(reg,text="Email",font=("Arial Bold",20))
    l7.configure(fg="Black",bg="Light pink")
    l7.place(relx=0.1, rely=0.6, anchor="center")
    usemail=Entry(reg,width=25,font=('Arial Bold',20))
    usemail.place(relx=0.3,rely=0.6, anchor="center")
    l8=Label(reg,text="Username",font=("Arial Bold",20))
    l8.configure(fg="Black",bg="Light pink")
    l8.place(relx=0.5, rely=0.6, anchor="center")
    ususer=Entry(reg,width=25,font=('Arial Bold',20))
    ususer.place(relx=0.7,rely=0.6, anchor="center")
    l9=Label(reg,text="Password",font=("Arial Bold",20))
    l9.configure(fg="Black",bg="Light pink")
    l9.place(relx=0.1, rely=0.8, anchor="center")
    uspass=Entry(reg,show="*",width=25,font=('Arial Bold',20))
    uspass.place(relx=0.3,rely=0.8, anchor="center")
    l10=Label(reg,text="Confirm Password",font=("Arial Bold",20))
    l10.configure(fg="Black",bg="Light pink")
    l10.place(relx=0.5, rely=0.8, anchor="center")
    uspass1=Entry(reg,show="*",width=25,font=('Arial Bold',20))
    uspass1.place(relx=0.7,rely=0.8, anchor="center")
    but1=Button(reg,text="Submit",fg="White",bg="black",command=searchuserlist)
    but1.place(relx = 0.4 ,rely = 0.9, anchor = 'c')
    but1['font']=myFont
    but2=Button(reg,text="Back",fg="White",bg="black",command=start)
    but2.place(relx = 0.6 ,rely = 0.9, anchor = 'c')
    but2['font']=myFont
    
def Guest_login():

    try:
        window.destroy()
    except:
        try:
            cav.destroy()
        except:
            print()

    global window1     
    window1=Tk()
    window1.title("MRF.com/Guest/choosing mode of transport")
    window1.attributes('-fullscreen',True)
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(window1,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack 
    photo=PhotoImage(file="project.png")
    label=Label(window1,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    l1=Label(window1,text="Choose your mode of transport",font=("Arial Bold",45),anchor='c')
    l1.configure(fg="White",bg="black")
    l1.pack()
    gt=Button(window1,text="Airways",fg="White",bg="Black",command= Guest_Airways)
    gt.place(relx = 0.5, rely = 0.4, anchor = 'c')
    gt['font']=myFont
    gt1=Button(window1,text="Railways",fg="White",bg="Black",command= Guest_Railways)
    gt1.place(relx = 0.5, rely = 0.5, anchor = 'c')
    gt1['font']=myFont
    gt2=Button(window1,text="Roadways",fg="White",bg="Black",command= Guest_Roadways)
    gt2.place(relx = 0.5, rely = 0.6, anchor = 'c')
    gt2['font']=myFont
    bt=Button(window1,text="Back",fg="White",bg="Black",command=start)
    bt.place(relx=0.5,rely=0.7,anchor="c")
    bt['font']=myFont

def Guest_Airways():
    
    def comsearchit():
        m=[]
        of=guestfrom.get()
        ot=guestto.get()
        dateo=day.get()+" "+month.get()+" "+year.get()
        f=open("Airways.csv",'r')
        lab=tom=0
        robj=csv.reader(f,delimiter=",")
        for a in robj:
            if tom%2==0: 
                if a[2]==of and a[3]==ot and dateo==a[4]:
                    m.append(a)
                    lab+=1
            tom+=1
        print(m)
        if lab==0:
            messagebox.showinfo("Oops!","No Flight found")
    
        class Table:       
            def __init__(self,root):
                for i in range(10,total_rows+10):
                    for j in range(10,total_columns+10):
                        self.e = Entry(root, width=17, fg='blue', 
                                        font=('Arial',16,'bold'))                   
                        self.e.grid(row=i+1, column=j+1)
                        self.e.insert(END, m[i-10][j-10])  

        total_rows = len(m) 
        total_columns = len(m[0])
        myFont = font.Font(size=30)
        root = Tk()
        root.attributes('-fullscreen',True)
        root.title("Airways chart")
        root.configure(bg ="Light Blue")
        l1=Label(root,text="Airways Chart",font=("Arial Bold",45))
        l1.configure(fg="Black",bg="Light Blue")
        l1.place(relx=0.5, rely=0.05, anchor="center")
        goq='Flight No.  \t  Flight Name\t  Origin\t\tDestination\t  Departure\t    Arrival\t\tStatus'
        
        l2=Label(root,text=goq,font=("Arial Bold",17))
        l2.configure(fg="Black",bg="Light Blue")
        l2.place(relx=0.43, rely=0.15, anchor="center")
        for r in range(9):
            bi=Label(root,text="   ",bg="Light Blue")
            bi.grid(row=r,column=0)
        l1=Label(root,text="For booking register or login using user login",font=("Arial Bold",20))
        l1.configure(fg="Black",bg="White")
        l1.place(relx=0.46, rely=0.7, anchor="center")
        bt=Button(root,text="Click here to Register",fg="White",bg="Black",command=Registration)
        bt.place(relx=0.4,rely=0.8,anchor="c")
        bt['font']=myFont
        bt1=Button(root,text="Click here to Login",fg="White",bg="Black",command=user_login)
        bt1.place(relx=0.5,rely=0.8,anchor="c")
        bt1['font']=myFont
        bt3=Button(root,text="Back",fg="White",bg="Black",command=root.destroy)
        bt3.place(relx=0.6,rely=0.8,anchor="c")
        bt3['font']=myFont
        t = Table(root)
        root.mainloop()
    
    try:
        window1.destroy()      
    except:
        try:
            cav.destroy()
        except:
            print()
        
    global windowA             
    windowA=Tk()
    windowA.title("MRF.com/Guest/choosing mode of transport/Airways")
    windowA.attributes('-fullscreen',True)
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="1307258.png")
    label2=Label(windowA,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(windowA,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    lc=Label(windowA,text='Enter the required details',font=("Arial Bold",45))
    lc.place(relx = 0.3, rely = 0.1)
    lc.configure(fg="White",bg="Black")
    l1=Label(windowA,text='From:',font=("Arial Bold",20))
    l1.place(relx = 0.25, rely = 0.35)
    l1.configure(fg="White",bg="Black")
    guestfrom=ttk.Combobox(windowA,values=Airwaysdestination)
    guestfrom.place(relx = 0.295, rely = 0.4, anchor = 'c')
    guestfrom.current()
    l2=Label(windowA,text='To:',font=("Arial Bold",20))
    l2.place(relx = 0.25, rely = 0.55)
    l2.configure(fg="White",bg="Black")
    guestto=ttk.Combobox(windowA,values=Airwaysdestination)
    guestto.place(relx = 0.295, rely = 0.6, anchor = 'c')
    guestto.current()
    ld=Label(windowA,text='Day:',font=("Arial Bold",20))
    ld.place(relx = 0.65, rely = 0.35)
    ld.configure(fg="White",bg="Black")
    day=ttk.Combobox(windowA,values=vai)
    day.place(relx = 0.695, rely = 0.4, anchor = 'c')
    day.current()
    l3=Label(windowA,text='Month:',font=("Arial Bold",20))
    l3.place(relx = 0.75, rely = 0.35)
    l3.configure(fg="White",bg="Black")
    month=ttk.Combobox(windowA,values=['January','February','March',
                                       'April','May','June','July',
                                       'August','September','October',
                                       'November','December'])
    month.place(relx = 0.795, rely = 0.4, anchor = 'c')
    month.current()
    l4=Label(windowA,text='Year:',font=("Arial Bold",20))
    l4.place(relx = 0.85, rely = 0.35)
    l4.configure(fg="White",bg="Black")
    year=ttk.Combobox(windowA,values=['2020','2021','2022'])
    year.place(relx = 0.895, rely = 0.4, anchor = 'c')
    year.current()
    adult=ttk.Combobox(windowA,values=['1','2','3','4','5','6','7','8','9'])
    adult.place(relx = 0.695, rely = 0.605, anchor = 'c')
    l5=Label(windowA,text='Adults:',font=("Arial Bold",20))
    l5.place(relx = 0.65, rely = 0.55)
    l5.configure(fg="White",bg="Black")
    children=ttk.Combobox(windowA,values=['1','2','3','4','5','6','7','8','9'])
    children.place(relx = 0.795, rely = 0.605, anchor = 'c')
    l6=Label(windowA,text='Children(2-11yrs):',font=("Arial Bold",20))
    l6.place(relx = 0.75, rely =0.55)
    l6.configure(fg="White",bg="Black")
    infants=ttk.Combobox(windowA,values=['0','1'])
    infants.place(relx = 0.695, rely = 0.7055, anchor='c')
    l7=Label(windowA,text='Infants(below 2yrs):',font=("Arial Bold",20))
    l7.place(relx = 0.65, rely = 0.65)
    l7.configure(fg="White",bg="Black")
    bt=Button(windowA,text="Back",fg="White",bg="Black",command=start1)
    bt.place(relx=0.1,rely=0.88)
    bt['font']=myFont
    bt2=Button(windowA,text="Search",fg="White",bg="Black",command=comsearchit)
    bt2.place(relx=0.5,rely=0.9,anchor="c")
    bt2['font']=myFont
                                       
def Guest_Railways():
    
    def comsearchit():
        m=[]
        of=guestfrom.get()
        ot=guestto.get()
        dateo=day.get()+" "+month.get()+" "+year.get()
        f=open("Railways.csv",'r')
        lab=tom=0
        robj=csv.reader(f,delimiter=",")
        for a in robj:
            if tom%2==0:
                if a[2]==of and a[3]==ot and dateo==a[4]:
                    m.append(a)
                    lab+=1
            tom+=1
        print(m)
        if lab==0:
            messagebox.showinfo("Oops!","No Train found")
    
        class Table:       
            def __init__(self,root):
                for i in range(10,total_rows+10):
                    for j in range(10,total_columns+10):
                        self.e = Entry(root, width=17, fg='blue', 
                                        font=('Arial',16,'bold'))                   
                        self.e.grid(row=i+1, column=j+1)
                        self.e.insert(END, m[i-10][j-10])

        total_rows = len(m) 
        total_columns = len(m[0])
        root = Tk()
        root.attributes('-fullscreen',True)
        root.title("Railways chart")
        root.configure(bg ="Light Blue")
        l1=Label(root,text="Available Trains",font=("Arial Bold",45))
        l1.configure(fg="Black",bg="Light Blue")
        l1.place(relx=0.5, rely=0.05, anchor="center")
        goq='Train No.  \t  Train Name\t  Origin\t\tDestination\t  Departure\t    Arrival\t\tStatus'
        
        l2=Label(root,text=goq,font=("Arial Bold",17))
        l2.configure(fg="Black",bg="Light Blue")
        l2.place(relx=0.43, rely=0.15, anchor="center")
        for r in range(9):
            bi=Label(root,text="   ",bg="Light Blue")
            bi.grid(row=r,column=0)
        l1=Label(root,text="For booking register or login using user login",font=("Arial Bold",25))
        l1.configure(fg="Black",bg="Light Blue")
        l1.place(relx=0.46, rely=0.7, anchor="center")
        bt=Button(root,text="Click here to Register",fg="White",bg="Black",command=Registration)
        bt.place(relx=0.4,rely=0.8,anchor="c")
        bt['font']=myFont
        bt1=Button(root,text="Click here to Login",fg="White",bg="Black",command=user_login)
        bt1.place(relx=0.5,rely=0.8,anchor="c")
        bt1['font']=myFont 
        bt3=Button(root,text="Back",fg="White",bg="Black",command=root.destroy)
        bt3.place(relx=0.6,rely=0.8,anchor="c")
        bt3['font']=myFont
        t = Table(root)
        root.mainloop()         

    try:
        window1.destroy()      
    except:
        try:
            cav.destroy()
        except:
            print()
        
    global windowR    
    windowR=Tk()
    windowR.title("MRF.com/Guest/choosing mode of transport/Railays")
    windowR.attributes('-fullscreen',True)
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="Coverphoto1.png")
    label2=Label(windowR,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(windowR,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack
    lc=Label(windowR,text='Enter the required details',font=("Arial Bold",45))
    lc.place(relx = 0.3, rely = 0.14)
    lc.configure(fg="White",bg="Black")
    l1=Label(windowR,text='From:',font=("Arial Bold",20))
    l1.place(relx = 0.25, rely = 0.35)
    l1.configure(fg="White",bg="Black")   
    guestfrom=ttk.Combobox(windowR,values=Railwaysdestination)
    guestfrom.place(relx = 0.295, rely = 0.4, anchor = 'c')
    guestfrom.current()
    l2=Label(windowR,text='To:',font=("Arial Bold",20))
    l2.place(relx = 0.25, rely = 0.55)
    l2.configure(fg="White",bg="Black")
    guestto=ttk.Combobox(windowR,values=Railwaysdestination)
    guestto.place(relx = 0.295, rely = 0.6, anchor = 'c')
    guestto.current()
    ld=Label(windowR,text='Day:',font=("Arial Bold",20))
    ld.place(relx = 0.55, rely = 0.35)
    ld.configure(fg="White",bg="Black")
    day=ttk.Combobox(windowR,values=vai)
    day.place(relx = 0.595, rely = 0.4, anchor = 'c')
    day.current()
    l3=Label(windowR,text='Month:',font=("Arial Bold",20))
    l3.place(relx = 0.65, rely = 0.35)
    l3.configure(fg="White",bg="Black")
    month=ttk.Combobox(windowR,values=['January','February','March',
                                       'April','May','June','July',
                                       'August','September','October',
                                       'November','December'])
    month.place(relx = 0.695, rely = 0.4, anchor = 'c')
    month.current()
    l4=Label(windowR,text='Year:',font=("Arial Bold",20))
    l4.place(relx = 0.75, rely = 0.35)
    l4.configure(fg="White",bg="Black")
    year=ttk.Combobox(windowR,values=['2020','2021','2022'])
    year.place(relx = 0.795, rely = 0.4, anchor = 'c')
    year.current()
    adult=ttk.Combobox(windowR,values=['0','1','2','3','4','5','6'])
    adult.place(relx = 0.595, rely = 0.605, anchor = 'c')
    l5=Label(windowR,text='Adults(12-60yrs):',font=("Arial Bold",20))
    l5.place(relx = 0.55, rely = 0.55)
    l5.configure(fg="White",bg="Black")
    children=ttk.Combobox(windowR,values=['0','1','2','3','4','5','6'])
    children.place(relx = 0.795, rely = 0.605, anchor = 'c')
    l6=Label(windowR,text='Children(5-11yrs):',font=("Arial Bold",20))
    l6.place(relx = 0.75, rely =0.55)
    l6.configure(fg="White",bg="Black")
    seniormen=ttk.Combobox(windowR,values=['0','1','2','3','4','5','6'])
    seniormen.place(relx = 0.595, rely = 0.7055, anchor='c')
    l7=Label(windowR,text='Senior Men(60+yrs):',font=("Arial Bold",20))
    l7.place(relx = 0.55, rely = 0.65)
    l7.configure(fg="White",bg="Black")
    seniorwomen=ttk.Combobox(windowR,values=['0','1','2','3','4','5','6'])
    seniorwomen.place(relx = 0.795, rely = 0.7055, anchor='c')
    l8=Label(windowR,text='Senior Women(58+yrs):',font=("Arial Bold",20))
    l8.place(relx = 0.75, rely = 0.65)
    l8.configure(fg="White",bg="Black")
    bt=Button(windowR,text="Back",fg="White",bg="Black",command=start1)
    bt.place(relx=0.1,rely=0.88)
    bt['font']=myFont
    bt2=Button(windowR,text="Search",fg="White",bg="Black",command=comsearchit)
    bt2.place(relx=0.5,rely=0.9,anchor="c")
    bt2['font']=myFont
        
def Guest_Roadways():

    def comsearchit():
        m=[]
        of=guestfrom.get()
        ot=guestto.get()
        dateo=day.get()+" "+month.get()+" "+year.get()
        f=open("Roadways.csv",'r')
        lab=tom=0
        robj=csv.reader(f,delimiter=",")
        for a in robj:
            if tom%2==0:
                if a[2]==of and a[3]==ot and dateo==a[4]:
                    m.append(a)
                    lab+=1
            tom+=1
        print(m)
        if lab==0:
            messagebox.showinfo("Oops!","No Bus found")
    
        class Table:       
            def __init__(self,root):
                for i in range(10,total_rows+10):
                    for j in range(10,total_columns+10):
                        self.e = Entry(root, width=17, fg='blue', 
                                        font=('Arial',16,'bold'))                   
                        self.e.grid(row=i+1, column=j+1)
                        self.e.insert(END, m[i-10][j-10])
        total_rows = len(m) 
        total_columns = len(m[0])
        root = Tk()
        root.attributes('-fullscreen',True)
        root.title("Roadways chart")
        root.configure(bg ="Light blue")
        l1=Label(root,text="Available Buses",font=("Arial Bold",45))
        l1.configure(fg="Black",bg="Light blue")
        l1.place(relx=0.5, rely=0.05, anchor="center")        
        goq='Bus No.  \t  Bus Name\t  Origin\t\tDestination\t  Departure\t    Arrival\t\tStatus'       
        l2=Label(root,text=goq,font=("Arial Bold",17))
        l2.configure(fg="Black",bg="Light Blue")
        l2.place(relx=0.43, rely=0.15, anchor="center")
        for r in range(9):
            bi=Label(root,text="   ",bg="Light blue")
            bi.grid(row=r,column=0)
        l3=Label(root,text="For booking register or login using user login",font=("Arial Bold",25))
        l3.configure(fg="Black",bg="Light Blue")
        l3.place(relx=0.47, rely=0.7, anchor="center")
        bt1=Button(root,text="Click here to Register",fg="White",bg="Black",command=Registration)
        bt1.place(relx=0.4,rely=0.8,anchor="c")
        bt1['font']=myFont
        bt2=Button(root,text="Click here to Login",fg="White",bg="Black",command=user_login)
        bt2.place(relx=0.5,rely=0.8,anchor="c")
        bt2['font']=myFont
        bt3=Button(root,text="Back",fg="White",bg="Black",command=root.destroy)
        bt3.place(relx=0.6,rely=0.8,anchor="c")
        bt3['font']=myFont
        t = Table(root)
        root.mainloop()

    try:
        window1.destroy()      
    except:
        try:
            cav.destroy()
        except:
            print()
        
    global windowr                   
    windowr=Tk()    
    windowr.title("MRF.com/Guest/choosing mode of transport/Airways")
    windowr.attributes('-fullscreen',True)
    myFont = font.Font(size=20)
    Coverphoto=PhotoImage(file="roadw.png")
    label2=Label(windowr,image=Coverphoto)
    label2.place(relx = 0.5,rely = 0.5, anchor ='center')
    label2.image = Coverphoto
    label2.pack
    photo=PhotoImage(file="project.png")
    label=Label(windowr,image=photo)
    label.place(relx = 0.94,rely = 0.1, anchor ='center')
    label.image = photo
    label.pack   
    lc=Label(windowr,text='Enter the required details',font=("Arial Bold",45))
    lc.place(relx = 0.3, rely = 0.14)
    lc.configure(fg="White",bg="Black") 
    l1=Label(windowr,text='From:',font=("Arial Bold",20))
    l1.place(relx = 0.25, rely = 0.35)
    l1.configure(fg="White",bg="Black")
    guestfrom=ttk.Combobox(windowr,values=Roadwaysdestination)
    guestfrom.place(relx = 0.295, rely = 0.4, anchor = 'c')
    guestfrom.current()
    l2=Label(windowr,text='To:',font=("Arial Bold",20))
    l2.place(relx = 0.25, rely = 0.55)
    l2.configure(fg="White",bg="Black")
    guestto=ttk.Combobox(windowr,values=Roadwaysdestination)
    guestto.place(relx = 0.295, rely = 0.6, anchor = 'c')
    guestto.current()
    ld=Label(windowr,text='Day:',font=("Arial Bold",20))
    ld.place(relx = 0.65, rely = 0.35)
    ld.configure(fg="White",bg="Black")
    day=ttk.Combobox(windowr,values=vai)
    day.place(relx = 0.695, rely = 0.4, anchor = 'c')
    day.current()
    l3=Label(windowr,text='Month:',font=("Arial Bold",20))
    l3.place(relx = 0.75, rely = 0.35)
    l3.configure(fg="White",bg="Black")
    month=ttk.Combobox(windowr,values=['January','February','March',
                                       'April','May','June','July',
                                       'August','September','October',
                                       'November','December'])
    month.place(relx = 0.795, rely = 0.4, anchor = 'c')
    month.current()
    l4=Label(windowr,text='Year:',font=("Arial Bold",20))
    l4.place(relx = 0.85, rely = 0.35)
    l4.configure(fg="White",bg="Black")
    year=ttk.Combobox(windowr,values=['2020','2021','2022'])
    year.place(relx = 0.895, rely = 0.4, anchor = 'c')
    year.current()
    l5=Label(windowr,text='Number of Passengers:',font=("Arial Bold",20))
    l5.place(relx = 0.65, rely = 0.55)
    l5.configure(fg="White",bg="Black")
    e2=ttk.Combobox(windowr,values=['0','1','2','3','4','5','6','7','8','9','10'])
    e2.place(relx = 0.695, rely = 0.6, anchor = 'c')
    e2.current()
    bt=Button(windowr,text="Back",fg="White",bg="Black",command=start1)
    bt.place(relx=0.1,rely=0.88)
    bt['font']=myFont
    bt2=Button(windowr,text="Search",fg="White",bg="Black",command=comsearchit)
    bt2.place(relx=0.5,rely=0.9,anchor="c")
    bt2['font']=myFont       
start()





