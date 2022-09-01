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
        label.place(relx = 0.95,rely = 0.01, anchor ='center')
        label.image = photo
        label.pack

        bt['font']=myFont
        abc=0
        abc+=1
            if abc==0:
                messagebox.showinfo("Oops!","None of the "+v+" names match to given name")

        Title=Label(bankin,text="Choose your payment method",font=("arial bold",45),bg="Orange",fg="black")
        Title.place(relx=0.25,rely=0.05)
        df=Label(bankin,text="AMOUNT TO BE PAYED",font=("arial bold",20),bg="light green",fg="black")
        df.place(relx=0.1,rely=0.2)
        rf=Label(bankin,text="Rs"+str(c),font=("arial bold",25),bg="light green",fg="red")
        rf.place(relx=0.4,rely=0.19)


        def namecheck():
            qwe=d1.get()
            iru=0
            for i in range(len(m)):
                if qwe==m[i][1]:
                    input_information()
                    iru+=1
            if iru ==0:
                messagebox.showinfo("Oops!","Give a Flight name which is the chart")
                

    l5=Label(windowra,text='Number of Passengers:',font=("Arial Bold",20))
    l5.place(relx = 0.65, rely = 0.55)
    l5.configure(fg="White",bg="Blue")
    e2=ttk.Combobox(windowra,values=['1','2','3','4','5','6','7','8','9','10'])
    e2.place(relx = 0.7, rely = 0.6, anchor = 'c')
    e2.current()

       def information():

                    o1=Label(inform,text="Name",font=("Arial Bold",15))
                    o1.place(relx=0.11,rely=0.3+(i/10))
                    o1.configure(fg="White",bg="Black")
                    o2=Entry(inform,width=10,font=('Arial Bold',15))
                    o2.place(relx=0.15,rely=0.3+(i/10))
                    age=Label(inform,text="Age",font=("Arial Bold",15))
                    age.place(relx=0.25,rely=0.3+(i/10))
                    age.configure(fg="White",bg="Black")
                    age1=Entry(inform,width=10,font=('Arial Bold',15))
                    age1.place(relx=0.3,rely=0.3+(i/10))
                    ge=Label(inform,text="Gender",font=("Arial Bold",15))
                    ge.place(relx=0.4,rely=0.3+(i/10))
                    ge.configure(fg="White",bg="Black")
                    ge1=ttk.Combobox(inform,values=["Male","Female","Transgender"])
                    ge1.place(relx=0.45,rely=0.3+(i/10))
                    quo=Label(inform,text="Class",fg="Blue",bg="yellow",font=("Arial Bold",15))
                    quo.place(relx=0.55,rely=0.3+(i/10))
                    quo.configure(fg="White",bg="Black")
                    drop3=ttk.Combobox(inform,values=["First A.C","Second A.C","Third A.C","Sleeper"])
                    drop3.place(relx=0.64,rely=0.31+(i/10),anchor="center")
                    teach.append(drop3)
                    pre=Label(inform,text="Preference",font=("Arial Bold",15))
                    pre.place(relx=0.7,rely=0.3+(i/10))
                    pre.configure(fg="White",bg="Black")
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


                    
            thisis=[]
            ohm=[]
            ay=[]
            global bil
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
            kevin=0
            for i in range(0,s):
                if kevin%2==0:
                    wobj.writerow([thisis[0][i],thisis[1][i],thisis[2][i],thisis[3][i],thisis[4][i]])
                kevin+=1    
            fq.close()





        
