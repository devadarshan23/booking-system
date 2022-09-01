from tkinter import *
from tkinter import ttk
import pickle
import csv
import os
from tkinter import messagebox
import random
window=Tk()
window.attributes('-fullscreen',True)
window.title("MRF.com")
window.configure(bg ="#00ffff")
l1=Label(window,text="Welcome to Move Run Fly",font=("Arial Bold",45))
l1.configure(fg="Black",bg="#00ffff")
l1.place(relx=0.5, rely=0.12, anchor="center")
banklogin=[["Srijith","12f214"],["Devadarshan","12f207"],["Syed","12f242"],["1","1"]]
userlogin=[["Srijith","12f214"],["Devadarshan","12f207"],["Syed","12f242"],["1","1"]]
fromlist=["monday","tuesday","wednesday","thursday","friday"]
banks=[("ICICI","ICICI"),("SBI","SBI"),('HDFC','HDFC')]
debit=[['1','1'],['2','2']]
me=[]
m=[]
Places=["AGRA FORT(AF)","AHMEDABAD(ADI)","MUMBAI CENTRAL(BCT)","HYDERABAD(HYB)","KOLKATA(KOAA)","DELHI(DLI)","COIMBATORE Jn.(CBE)","BANGALORE CITY(SBC)","TIRUPATI(TPTY)","CHENNAI CENTRAL(MAS)","PUNE Jn.(PUNE)"]
        

def Admin_id():
    print("nothing inside")
    
    
    
def payment_mode():

    def debit_card():
        
        def debit_check():
        
            x=0
            num1=cardno.get()
            num2=pinno.get()
            for i in range(len(debit)):
                if num1 in debit[i][0] and num2 in debit[i][1]:
                    x+=1
            if x==1:
                bill()
                debitwindow.destroy()
            else: 
                messagebox.showwarning("Attention","Invalid Username or Password!")
                banklog.destroy()
                
        debitwindow=Tk()
        debitwindow.title("payment mode")
        debitwindow.attributes('-fullscreen',True) 
        debitwindow.configure(bg ="light Green")
        deb1=Label(debitwindow,text="Enter required credentials to enter the portal",font=("Arial",20))
        deb1.configure(fg="White",bg="light Green")
        deb1.place(relx=0.55,rely=0.2,anchor="center")
        deb2=Label(debitwindow,text="Username")
        deb2.place(relx=0.5,rely=0.4,anchor="center")
        cardno=Entry(debitwindow)
        cardno.place(relx=0.6,rely=0.4,anchor="center")
        deb3=Label(debitwindow,text="Password")
        deb3.place(relx=0.5,rely=0.45,anchor="center")
        pinno=Entry(debitwindow,show="*")
        pinno.place(relx=0.6,rely=0.45,anchor="center")
        du1=Button(debitwindow,text="Submit",fg="Blue",bg="yellow",command=debit_check)
        du1.place(relx=0.55,rely=0.5,anchor="center")
        du2=Button(debitwindow,text="Back",fg="Blue",bg="yellow",command=debitwindow.destroy)
        du2.place(relx=0.65,rely=0.5,anchor="center")


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
            
        banklog=Tk()       
        banklog.attributes('-fullscreen',True)
        banklog.title("bank login")
        banklog.configure(bg ="light blue")
        lb0=Label(banklog,text="Amount:",font=("Arial",20))
        lb0.configure(fg="black",bg="light blue")
        lb0.place(relx=0.55,rely=0.1)
        lbb0=Label(banklog,text=c+(s*15),font=("Arial",15))
        lbb0.configure(fg="black",bg="light blue")
        lbb0.place(relx=0.65,rely=0.1)        
        lb1=Label(banklog,text="Enter required  bank credentials for payment",font=("Arial",20))
        lb1.configure(fg="black",bg="light blue")
        lb1.place(relx=0.55,rely=0.2,anchor="center")
        lb2=Label(banklog,text="Username")
        lb2.place(relx=0.5,rely=0.4,anchor="center")
        usename=Entry(banklog)
        usename.place(relx=0.6,rely=0.4,anchor="center")
        lb3=Label(banklog,text="Password")
        lb3.place(relx=0.5,rely=0.45,anchor="center")
        password1=Entry(banklog,show="*")
        password1.place(relx=0.6,rely=0.45,anchor="center")
        bue1=Button(banklog,text="Submit",fg="Blue",bg="yellow",command=bankidpassword)
        bue1.place(relx=0.55,rely=0.5,anchor="center")
        bue2=Button(banklog,text="Back",fg="Blue",bg="yellow",command=banklog.destroy)
        bue2.place(relx=0.65,rely=0.5,anchor="center")

    
    paymentwindow=Tk()
    paymentwindow.title("payment mode")
    paymentwindow.attributes('-fullscreen',True) 
    paymentwindow.configure(bg ="light Green")
    pa1=Button(paymentwindow,text="net banking",fg="Blue",bg="yellow",command=bank_login)
    pa1.place(relx=0.55,rely=0.5,anchor="center")
    pa2=Button(paymentwindow,text="debit card",fg="Blue",bg="yellow",command=debit_card)
    pa2.place(relx=0.55,rely=0.7,anchor="center")
    p1=Label(paymentwindow,text="Payment Mode",font=("Arial Bold",45))
    p1.configure(fg="Black",bg="light green")
    p1.place(relx=0.5, rely=0.12, anchor="center")
    p2=Button(paymentwindow,text="back",fg="Blue",bg="yellow",command=paymentwindow.destroy)
    p2.place(relx=0.05,rely=0.9,anchor="center")
    
    
    
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
def bill():
    bil=Tk()
   
    bil.attributes('-fullscreen',True)
    bil.title("bill")
    bil.configure(bg ="light blue")
    beu1=Button(bil,text="Back",fg="Blue",bg="yellow",command=bil.destroy)
    beu1.place(relx=0.01,rely=0.99)
    dr=Label(bil,text="Ticket Conformation",font=("arial bold",30),bg="light blue",fg="black")
    dr.place(relx=0.01,rely=0.01)
    rr=Label(bil,text="Congratulations!! thank you for using MRF's online  rail reservation facility.",font=("arial bold",20),bg="light blue",fg="black")
    tt=Label(bil,text="Your Booking Details are Indicated Below:",font=("arial bold",20),bg="light blue",fg="black")
    rr.place(relx=0.01,rely=0.08)
    tt.place(relx=0.01,rely=0.15)
    j=Label(bil,text="Train No:",font=("arial bold",19),bg="light blue",fg="black")
    j.place(relx=0.01,rely=0.20)


    k=Label(bil,text=m[0][0],font=("arial bold",19),bg="light blue",fg="black")
    k.place(relx=0.16,rely=0.20)




    
    j1=Label(bil,text="Class:",font=("arial bold",19),bg="light blue",fg="black")
    j1.place(relx=0.3,rely=0.20)

    k1=Label(bil,text=vari3.get(),font=("arial bold",19),bg="light blue",fg="black")
    k1.place(relx=0.4,rely=0.20)

    
    j2=Label(bil,text="Date and Time of booking:",font=("arial bold",19),bg="light blue",fg="black")
    j2.place(relx=0.6,rely=0.20)
    y1=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
    y1.place(relx=0.01,rely=0.25)
    j3=Label(bil,text="From:",font=("arial bold",19),bg="light blue",fg="black")
    j3.place(relx=0.01,rely=0.30)

    k3=Label(bil,text=m[0][2],font=("arial bold",19),bg="light blue",fg="black")
    k3.place(relx=0.1,rely=0.30)





    
    j4=Label(bil,text="Departure:",font=("arial bold",19),bg="light blue",fg="black")
    j4.place(relx=0.3,rely=0.30)

    k4=Label(bil,text=m[0][4],font=("arial bold",19),bg="light blue",fg="black")
    k4.place(relx=0.4,rely=0.30)

    
    j5=Label(bil,text="To:",font=("arial bold",19),bg="light blue",fg="black")
    j5.place(relx=0.6,rely=0.30)

    k5=Label(bil,text=m[0][3],font=("arial bold",19),bg="light blue",fg="black")
    k5.place(relx=0.7,rely=0.30)




    
    y2=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
    y2.place(relx=0.01,rely=0.35)
    
    j6=Label(bil,text="Arrival:",font=("arial bold",19),bg="light blue",fg="black")
    j6.place(relx=0.01,rely=0.40)


    k6=Label(bil,text=m[0][4],font=("arial bold",19),bg="light blue",fg="black")
    k6.place(relx=0.1,rely=0.40)






    
    j7=Label(bil,text="Distance:",font=("arial bold",19),bg="light blue",fg="black")
    j7.place(relx=0.3,rely=0.40)
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
        k12=Label(bil,text=me[i][0].get(),font=("arial bold",15),bg="light blue",fg="black")
        k12.place(relx=0.1,rely=0.60+(i/30))

    


    
    j13=Label(bil,text="Age",font=("arial bold",19),bg="light blue",fg="black")
    j13.place(relx=0.25,rely=0.57)

    for i in range(s):
        k13=Label(bil,text=me[i][1].get(),font=("arial bold",15),bg="light blue",fg="black")
        k13.place(relx=0.25,rely=0.60+(i/30))



    
    j14=Label(bil,text="Gender",font=("arial bold",19),bg="light blue",fg="black")
    j14.place(relx=0.35,rely=0.57)

    for i in range(s):
        k14=Label(bil,text=me[i][2].get(),font=("arial bold",15),bg="light blue",fg="black")
        k14.place(relx=0.35,rely=0.60+(i/30))
        



    
    j15=Label(bil,text="Coach",font=("arial bold",19),bg="light blue",fg="black")
    j15.place(relx=0.45,rely=0.57)

    if vari3.get()=="First A.C":
        rand=random.randint(1,2)
        rand1=random.randint(1,29)
        coach="F"+str(rand)
        for i in range(s):
            
            k15=Label(bil,text=coach,font=("arial bold",15),bg="light blue",fg="black")
            k15.place(relx=0.45,rely=0.60+(i/30))
        for i in range(s):
            
            k16=Label(bil,text=rand1+i,font=("arial bold",15),bg="light blue",fg="black")
            k16.place(relx=0.55,rely=0.61+(i/30))
            
    elif vari3.get()=="Second A.C":
        
        rand=random.randint(1,3)
        rand1=random.randint(1,51)
        coach="A"+str(rand)
        for i in range(s):
            
            
            k15=Label(bil,text=coach,font=("arial bold",15),bg="light blue",fg="black")
            k15.place(relx=0.45,rely=0.60+(i/30))
        for i in range(s):
            
            
            k16=Label(bil,text=rand1+i,font=("arial bold",15),bg="light blue",fg="black")
            k16.place(relx=0.55,rely=0.61+(i/30))

        
    elif vari3.get()=="Third A.C":
        
        rand=random.randint(1,3)
        rand1=random.randint(1,69)
        coach="B"+str(rand)
        for i in range(s):
            
            
            k15=Label(bil,text=coach,font=("arial bold",15),bg="light blue",fg="black")
            k15.place(relx=0.45,rely=0.61+(i/30))
        for i in range(s):
            
            
             
            
            
           k16=Label(bil,text=rand1+i,font=("arial bold",15),bg="light blue",fg="black")
           k16.place(relx=0.55,rely=0.60+(i/30))

    elif  vari3.get()=="Sleeper":
        
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
    
    
    
    
def banking():
            
    global c
    global ad
    global ch
    global s
    ad=0
    ch=0
    c=0
    
    bankin=Tk()
    s=int(e2.get())#e2 is the variable used for no of passengers
    bankin.attributes('-fullscreen',True)
    bankin.title("banking")
    bankin.configure(bg ="light Green")
    
    
    re=[]     
    for i in range(s):
        gh=0
        gh+=int(me[i][1].get())
        re.append(gh)
    
    print(re)    
    for i in range(s):        
        op=0
        if re[i]<=13  or  re[i]>=60 :
            if vari3.get()=="First A.C":
                op+=1000
                c+=op
            
            elif vari3.get()=="Second A.C":
                op+=750
                c+=op
            elif vari3.get()=="Third A.C":
                op+=500
                c+=op
            elif  vari3.get()=="Sleeper":
                op+=250
                c+=op                                            
        else:
            
            if vari3.get()=="First A.C":
                op+=2000
                c+=op
            
            elif vari3.get()=="Second A.C":
                op+=1500
                c+=op
            elif vari3.get()=="Third A.C":
                op+=1000
                c+=op
            elif  vari3.get()=="Sleeper":
                op+=500
                c+=op
            
                        
    for i in range(s):
        if re[i]>=13:
            ad+=1
        else:
            ch+=1
    print(c)
      
    df=Label(bankin,text="AMOUNT TO BE PAYED",font=("arial bold",20),bg="light green",fg="black")
    df.place(relx=0.1,rely=0.1)
    rf=Label(bankin,text="Rs"+str(c),font=("arial bold",25),bg="light green",fg="red")
    rf.place(relx=0.4,rely=0.09)
    be1=Button(bankin,text="Back",fg="Blue",bg="yellow",command=bankin.destroy)
    be1.place(relx=0.1,rely=0.9)
    ef=Label(bankin,text="CHOOSE A BANK",font=("arial bold",25),bg="light green",fg="black")
    ef.place(relx=0.1,rely=0.3)
    t=StringVar()
    

    io=Radiobutton(bankin,text="ICICI",variable=t,value="ICICI",fg="black",bg="light green",font=("arial bold",10))
    io.place(relx=0.1,rely=0.35)
    io1=Radiobutton(bankin,text="SBI",variable=t,value="SBI",fg="black",bg="light green",font=("arial bold",10))
    io1.place(relx=0.1,rely=0.45)
    io2=Radiobutton(bankin,text="HDFC",variable=t,value="HDFC",fg="black",bg="light green",font=("arial bold",10))
    io2.place(relx=0.1,rely=0.55)
    
    
    br=Button(bankin,text="Continue",fg="Blue",bg="yellow",command=payment_mode)
    br.place(relx=0.9,rely=0.9)
        
        

    
def input_information():
    inform=Tk()
    inform.attributes('-fullscreen',True)
    inform.title("input information")
    inform.configure(bg ="light Green")
    for j in range (20):
        if e2.get()==str(j):
            
            
            for i in range(j):
                ne=[]
                o1=Label(inform,text="Name")
                o1.place(relx=0.01,rely=0.3+(i/10))
                o2=Entry(inform)
                o2.place(relx=0.04,rely=0.3+(i/10))
                ne.append(o2)
                age=Label(inform,text="age")
                age.place(relx=0.13,rely=0.3+(i/10))
                age1=Entry(inform)
                age1.place(relx=0.16,rely=0.3+(i/10))
                ne.append(age1)                
                var=StringVar(inform)
                var1=StringVar(inform)
                ge=Label(inform,text="Gender")
                ge.place(relx=0.25,rely=0.3+(i/10))
                ge1=OptionMenu(inform,var,"Male","Female","Transgender")
                ge1.place(relx=0.30,rely=0.3+(i/10))
                ne.append(var)
                pre=Label(inform,text="Preference")
                pre.place(relx=0.39,rely=0.3+(i/10))
                pre1=OptionMenu(inform,var1,"No Preferences","Lower","Middle","Upper")
               
                pre1.place(relx=0.44,rely=0.3+(i/10))
                ne.append(var1)
                me.append(ne)
    
        
    bh=Button(inform,text="Continue",fg="Blue",bg="yellow",command=banking)
    bh.place(relx=0.9,rely=0.9)
    bh1=Button(inform,text="Back",fg="Blue",bg="yellow",command=inform.destroy)
    bh1.place(relx=0.1,rely=0.9)
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
    global d1
    
    def searchpannalama():
        
        
        
        of=vari.get()
        ot=vari1.get()
        dateo=e1.get()
        print(dateo)
        f=open("Railways.csv",'r')
        lab=tom=0
        robj=csv.reader(f,delimiter=",")
        for a in robj:
            if tom%2==0:
                
                
                if a[2]==of and a[3]==ot and dateo==a[5]:
                    m.append(a)
                    lab+=1
            tom+=1
        print(m)
        if lab==0:
            messagebox.showinfo("Oops!","No Train found")
        
    
    
   
    
        class Table:
            def __init__(self,strain):
                c=0
                for i in range(7,total_rows+7):
                    if c%2==0:
                        for j in range(7,total_columns+7):
                            self.e = Entry(strain, width=17, fg='blue', 
                                   font=('Arial',16,'bold'))
                            self.e.grid(row=i+1, column=j+1)
                            self.e.insert(END, m[i-7][j-7])
                c+=1
        f=open("Railways.csv","r")
        robj=csv.reader(f,delimiter=",")
        e=list(robj)
        total_rows = len(m)
        total_columns = len(m[0])
        f.close()
  
        strain=Tk()
        strain.attributes('-fullscreen',True)
        strain.title("search train")
        strain.configure(bg ="light Green")
        s1=Label(strain,text="Available Trains",font=("Arial Bold",30))
        s1.configure(fg="blue",bg="light Green")
        s1.place(relx=0.13, rely=0.04, anchor="center")
        for r in range(6):
            bi=Label(strain,text="   ",bg="light green")
            bi.grid(row=r,column=0)#till here
        t=Table(strain)
        g1=Button(strain,text="BOOK",fg="blue",bg="light green",command=input_information)
        g1.place(relx=0.9,rely=0.9)
                
        
        g2=Button(strain,text="BACK",fg="blue",bg="light green",command=strain.destroy)
        g2.place(relx=0.1,rely=0.9)
        bi2=Label(strain,text="enter the train name that you want to book")
        bi2.place(relx=0.1,rely=0.6)
        d1=Entry(strain,bg="yellow",fg="blue")
        d1.place(relx=0.3,rely=0.6)
        
            
            
                
                 
       
        
       
    global e2
    global vari
    global vari1
    global vari3
    global e1
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
    drop1=OptionMenu(railbook,vari,Places[0],Places[1],Places[2],Places[3],Places[4],Places[5],Places[6],Places[7])
    drop1.place(relx=0.20,rely=0.4,anchor="center")
    vari.set("chennai")
    To=Label(railbook,text="DESTINATION",fg="Blue",bg="yellow")
    To.place(relx=0.07,rely=0.5,anchor="center")
    drop2=OptionMenu(railbook,vari1,Places[0],Places[1],Places[2],Places[3],Places[4],Places[5],Places[6],Places[7])
    drop2.place(relx=0.20,rely=0.5,anchor="center")
    vari1.set("delhi")
    date=Label(railbook,text="DATE",fg="Blue",bg="yellow")
    date.place(relx=0.07,rely=0.6)
    e1=Entry(railbook,bg="yellow",fg="blue")
    e1.place(relx=0.18,rely=0.6)

    nop=Label(railbook,text="NO OF PASSENGERS",fg="Blue",bg="yellow")
    nop.place(relx=0.07,rely=0.7)
    e2=Entry(railbook,bg="yellow",fg="blue")
    e2.place(relx=0.18,rely=0.7)
    quo=Label(railbook,text="CLASS",fg="Blue",bg="yellow")
    quo.place(relx=0.11,rely=0.8)
    drop3=OptionMenu(railbook,vari3,"First A.C","Second A.C","Third A.C","Sleeper")
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
    bu5=Button(railbook,text="Search Train",fg="Blue",bg="yellow",command=searchpannalama)
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
''' banking and bill
roadways airways copy paste seat no selection
entry label positioning for user input
table label formatting
help menu
registeration
know more about indian transport option
matching with user input'''
