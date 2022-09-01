from tkinter import *
def bill():
        
        bil=Tk()   
        bil.attributes('-fullscreen',True)
        bil.title("bill")
        bil.configure(bg ="light blue")
        beu1=Button(bil,text="Back",fg="Blue",bg="yellow",command=bil.destroy)
        beu1.place(relx=0.5,rely=0.9)
        beu1['font']=myFont
        dr=Label(bil,text="Ticket Conformation",font=("arial bold",30),bg="light blue",fg="black")
        dr.place(relx=0.01,rely=0.01)
        rr=Label(bil,text="Congratulations!! Thank you for using MRF's online Bus reservation facility.",font=("arial bold",20),bg="light blue",fg="black")
        tt=Label(bil,text="Your Booking Details are Indicated Below:",font=("arial bold",20),bg="light blue",fg="black")
        rr.place(relx=0.01,rely=0.08)
        tt.place(relx=0.01,rely=0.15)
        j=Label(bil,text="Bus No:",font=("arial bold",19),bg="light blue",fg="black")
        j.place(relx=0.01,rely=0.20)
        k=Label(bil,text=available[0][0],font=("arial bold",19),bg="light blue",fg="black")
        k.place(relx=0.16,rely=0.20) 
        j1=Label(bil,text="Class:",font=("arial bold",19),bg="light blue",fg="black")
        j1.place(relx=0.3,rely=0.20)
        k1=Label(bil,text=clas,font=("arial bold",19),bg="light blue",fg="black")
        k1.place(relx=0.4,rely=0.20)
        current_time = datetime.datetime.now() 
        j2=Label(bil,text="Date and Time of booking:",font=("arial bold",19),bg="light blue",fg="black")
        j2.place(relx=0.6,rely=0.20)
        konga=Label(bil,text=current_time,font=("arial bold",19),bg="light blue",fg="black")
        konga.place(relx=0.8,rely=0.20)
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
        j7=Label(bil,text="Number of Passengers:",font=("arial bold",19),bg="light blue",fg="black")
        j7.place(relx=0.3,rely=0.40)
        k8=Label(bil,text=ad,font=("arial bold",19),bg="light blue",fg="black")
        k8.place(relx=0.67,rely=0.40)
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

bill()


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
                        
                debitwindow=Tk()
                debitwindow.title("payment mode")
                debitwindow.attributes('-fullscreen',True) 
                debitwindow.configure(bg ="light Green")
                deb1=Label(debitwindow,text="Enter required credentials to enter the portal",font=("Arial Bold",25))
                deb1.configure(fg="White",bg="light Green")
                deb1.place(relx=0.55,rely=0.2,anchor="center")
                deb2=Label(debitwindow,text="Enter number in D",font=("Arial",20))
                deb2.place(relx=0.4,rely=0.4,anchor="center")
                cardno=Entry(debitwindow,show="*",width=10,font=('Arial Bold',15))
                cardno.place(relx=0.65,rely=0.4,anchor="center")
                deb3=Label(debitwindow,text="Enter number in M",font=("Arial",20))
                deb3.place(relx=0.4,rely=0.45,anchor="center")
                pinno=Entry(debitwindow,show="*",width=10,font=('Arial Bold',15))
                pinno.place(relx=0.65,rely=0.45,anchor="center")
                du1=Button(debitwindow,text="Submit",fg="Blue",bg="yellow",command=debit_check)
                du1.place(relx=0.55,rely=0.5,anchor="center")
                du1['font']=myFont      
                du2=Button(debitwindow,text="Back",fg="Blue",bg="yellow",command=debitwindow.destroy)
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
                    
                banklog=Tk()       
                banklog.attributes('-fullscreen',True)
                banklog.title("bank login")
                banklog.configure(bg ="light blue")
                lb0=Label(banklog,text="Amount:",font=("Arial Bold",25))
                lb0.configure(fg="black",bg="light blue")
                lb0.place(relx=0.45,rely=0.1)
                lbb0=Label(banklog,text=c+(s*15),font=("Arial Bold",25))
                lbb0.configure(fg="black",bg="light blue")
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
                bue1=Button(banklog,text="Submit",fg="Blue",bg="yellow",command=bankidpassword)
                bue1.place(relx=0.55,rely=0.5,anchor="center")
                bue1['font']=myFont
                bue2=Button(banklog,text="Back",fg="Blue",bg="yellow",command=banklog.destroy)
                bue2.place(relx=0.65,rely=0.5,anchor="center")
                bue2['font']=myFont             
            
            paymentwindow=Tk()
            paymentwindow.title("payment mode")
            paymentwindow.attributes('-fullscreen',True) 
            paymentwindow.configure(bg ="light Green")
            pa1=Button(paymentwindow,text="Net banking",fg="Blue",bg="yellow",command=bank_login)
            pa1.place(relx=0.5,rely=0.4,anchor="center")
            pa1['font']=myFont
            pa2=Button(paymentwindow,text="Debit card",fg="Blue",bg="yellow",command=debit_card)
            pa2.place(relx=0.5,rely=0.66,anchor="center")
            pa2['font']=myFont 
            p1=Label(paymentwindow,text="Payment Mode",font=("Arial Bold",45))
            p1.configure(fg="Black",bg="light green")
            p1.place(relx=0.5, rely=0.12, anchor="center")
            p2=Button(paymentwindow,text="Back",fg="Blue",bg="yellow",command=paymentwindow.destroy)
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


def airwaysbill():

    def bill():
        
        bil=Tk()
        bil.attributes('-fullscreen',True)
        bil.title("bill")
        bil.configure(bg ="light blue")
        beu1=Button(bil,text="Back",fg="Blue",bg="yellow",command=bil.destroy)
        beu1.place(relx=0.01,rely=0.99)
        dr=Label(bil,text="Ticket Conformation",font=("arial bold",30),bg="light blue",fg="black")
        dr.place(relx=0.01,rely=0.01)
        rr=Label(bil,text="Congratulations!! thank you for using MRF's online  Airline reservation facility.",font=("arial bold",20),bg="light blue",fg="black")
        tt=Label(bil,text="Your Booking Details are Indicated Below:",font=("arial bold",20),bg="light blue",fg="black")
        rr.place(relx=0.01,rely=0.08)
        tt.place(relx=0.01,rely=0.15)
        j=Label(bil,text="Airline No:",font=("arial bold",19),bg="light blue",fg="black")
        j.place(relx=0.01,rely=0.20)
        k=Label(bil,text=air[0][0],font=("arial bold",19),bg="light blue",fg="black")#works only when one flight available
        k.place(relx=0.16,rely=0.20)





    
        j1=Label(bil,text="Class:",font=("arial bold",19),bg="light blue",fg="black")
        j1.place(relx=0.3,rely=0.20)

        k1=Label(bil,text='',font=("arial bold",19),bg="light blue",fg="black")
        k1.place(relx=0.4,rely=0.20)

    
        j2=Label(bil,text="Date and Time of booking:",font=("arial bold",19),bg="light blue",fg="black")
        j2.place(relx=0.6,rely=0.20)
        y1=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
        y1.place(relx=0.01,rely=0.25)
        j3=Label(bil,text="From:",font=("arial bold",19),bg="light blue",fg="black")
        j3.place(relx=0.01,rely=0.30)

        k3=Label(bil,text=air[0][2],font=("arial bold",19),bg="light blue",fg="black")
    
        k3.place(relx=0.1,rely=0.30)





    
        j4=Label(bil,text="Departure:",font=("arial bold",19),bg="light blue",fg="black")
        j4.place(relx=0.3,rely=0.30)

        k4=Label(bil,text=air[0][4],font=("arial bold",19),bg="light blue",fg="black")
        k4.place(relx=0.4,rely=0.30)

    
        j5=Label(bil,text="To:",font=("arial bold",19),bg="light blue",fg="black")
        j5.place(relx=0.6,rely=0.30)

        k5=Label(bil,text=air[0][3],font=("arial bold",19),bg="light blue",fg="black")
        k5.place(relx=0.7,rely=0.30)




    
        y2=Label(bil,text="--"*100,font=("arial bold",19),bg="light blue",fg="black")
        y2.place(relx=0.01,rely=0.35)
    
        j6=Label(bil,text="Arrival:",font=("arial bold",19),bg="light blue",fg="black")
        j6.place(relx=0.01,rely=0.40)


        k6=Label(bil,text=air[0][4],font=("arial bold",19),bg="light blue",fg="black")
        k6.place(relx=0.1,rely=0.40)






    
        j7=Label(bil,text="Arival Terminal:",font=("arial bold",19),bg="light blue",fg="black")
        j7.place(relx=0.3,rely=0.40)
        rand2=random.randint(1,10)

        k7=Label(bil,text=rand2,font=("arial bold",23),bg="light blue",fg="black")
        k7.place(relx=0.45,rely=0.40)
        
        j8=Label(bil,text="Adult:",font=("arial bold",19),bg="light blue",fg="black")
        j8.place(relx=0.60,rely=0.40)

        #k8=Label(bil,text=adult.get(),font=("arial bold",19),bg="light blue",fg="black")
        #k8.place(relx=0.67,rely=0.40)



    
        j9=Label(bil,text="Child:",font=("arial bold",19),bg="light blue",fg="black")
        j9.place(relx=0.75,rely=0.40)

        #k9=Label(bil,text=children.get(),font=("arial bold",19),bg="light blue",fg="black")
        #k9.place(relx=0.8,rely=0.40)

    




    
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
            print()
            
            #k12=Label(bil,text=Airwayspassenger[i][0].get(),font=("arial bold",15),bg="light blue",fg="black")
            #k12.place(relx=0.1,rely=0.60+(i/30))

    


    
        j13=Label(bil,text="Age",font=("arial bold",19),bg="light blue",fg="black")
        j13.place(relx=0.25,rely=0.57)

        for i in range(s):
            print()
            #k13=Label(bil,text=Airwayspassenger[i][1].get(),font=("arial bold",15),bg="light blue",fg="black")
            #k13.place(relx=0.25,rely=0.60+(i/30))



    
        j14=Label(bil,text="Gender",font=("arial bold",19),bg="light blue",fg="black")
        j14.place(relx=0.35,rely=0.57)

        for i in range(s):
            print()
            #k14=Label(bil,text=Airwayspassenger[i][2].get(),font=("arial bold",15),bg="light blue",fg="black")
            #k14.place(relx=0.35,rely=0.60+(i/30))
        



    
        j15=Label(bil,text="Allowbgs",font=("arial bold",19),bg="light blue",fg="black")
        j15.place(relx=0.45,rely=0.57)

        for i in range(s):
            k15=Label(bil,text="15",font=("arial bold",15),bg="light blue",fg="black")
            k15.place(relx=0.50,rely=0.60+(i/30))



        


        


    
        j16=Label(bil,text="Seat",font=("arial bold",19),bg="light blue",fg="black")
        j16.place(relx=0.55,rely=0.57)
    

    


    
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

        #k19=Label(bil,text=s*,font=("arial bold",25),bg="light blue",fg="black")calculate tax by taking 23% of each ticket
        #k19.place(relx=0.2,rely=0.87)

    
        j20=Label(bil,text="Gross Amount",font=("arial bold",19),bg="light blue",fg="black")
        j20.place(relx=0.4,rely=0.84)

        #k20=Label(bil,text=c+(s*15),font=("arial bold",25),bg="light blue",fg="black")
        #k20.place(relx=0.4,rely=0.87)






