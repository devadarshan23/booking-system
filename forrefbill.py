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
        
    def banking():
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
        Title=Label(bankin,text="Choose your payment method",font=("arial bold",45),bg="Orange",fg="black")
        Title.place(relx=0.3,rely=0.05)
        df=Label(bankin,text="AMOUNT TO BE PAYED",font=("arial bold",20),bg="light green",fg="black")
        df.place(relx=0.1,rely=0.2)
        rf=Label(bankin,text="Rs"+str(c),font=("arial bold",25),bg="light green",fg="red")
        rf.place(relx=0.4,rely=0.19)
        be1=Button(bankin,text="Back",fg="Blue",bg="yellow",command=start1)
        be1.place(relx=0.1,rely=0.9)
        be1['font']=myFont
        ef=Label(bankin,text="CHOOSE A BANK",font=("arial bold",25),bg="light green",fg="black")
        ef.place(relx=0.1,rely=0.3)
        t=StringVar()
        io=Radiobutton(bankin,text="ICICI",variable=t,value="ICICI",fg="black",bg="light green",font=("arial bold",20))
        io.place(relx=0.1,rely=0.4)
        io1=Radiobutton(bankin,text="SBI",variable=t,value="SBI",fg="black",bg="light green",font=("arial bold",20))
        io1.place(relx=0.1,rely=0.5)
        io2=Radiobutton(bankin,text="HDFC",variable=t,value="HDFC",fg="black",bg="light green",font=("arial bold",20))
        io2.place(relx=0.1,rely=0.6)
        br=Button(bankin,text="Continue",fg="Blue",bg="yellow",command=payment_mode)
        br.place(relx=0.9,rely=0.9)
        br['font']=myFont
