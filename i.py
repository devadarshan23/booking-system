import tkinter
import pickle
import os
window=tkinter.Tk()
window.title("MRF.com")
window.geometry=('100*100')
window.configure(bg ="Orange")
from tkinter import Label
from tkinter import PhotoImage
l1=Label(window,text="Welcome to Move Run Fly",font=("Arial Bold",25))
l1.pack()
l1.configure(fg="White",bg="Orange")


#photo=tkinter.PhotoImage(file="C:/Users/ADMIN/Desktop/sri-2020-CS/project.png")
#l1.place(relx = 0.0,rely = .0, anchor ='center')
#label=tkinter.Label(window,image=photo).grid(row=1000,column=1000)
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

def Display():
    l1.configure(text="You have selected Admin login")
def Guest_login():
    f=open("guest login.txt","w")
    s= ' ' 
    while True:
        b=input()
        s+=b
        s+="\n"
        if b.upper()=="EXIT": 
            break
    f.write(s)
    f.close()
def Print():
    print("Useless")
def Exit():
    print("Thank you")
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
    
    
def Airways():
    windowA=tkinter.Tk()
    windowA.title("MRF.com/Guest/choosing mode of transport/Airways")
    windowA.geometry('100x100')
    windowA.configure(bg ="Blue")
    from tkinter import Label
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
       'Jaipur International Airport(Jaipur, Rajasthan)'
       'Chennai International Airport(Chennai, Tamil Nadu)'
       'Civil Aerodrome(Coimbatore, Tamil Nadu)'
       'Chandigarh Airport(Chandigarh)'
       'Dabolim Airport(Goa)'])
    airportsfrom.place(relx = 0.3, rely = 0.4, anchor = 'c')
    airportsfrom.current()
    print(airportsfrom.current(),airportsfrom.get())
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
       'Jaipur International Airport(Jaipur, Rajasthan)'
       'Chennai International Airport(Chennai, Tamil Nadu)'
       'Civil Aerodrome(Coimbatore, Tamil Nadu)'
       'Chandigarh Airport(Chandigarh)'
       'Dabolim Airport(Goa)'])
    airportsto.place(relx = 0.3, rely = 0.6, anchor = 'c')
    airportsto.current()
    print(airportsto.current(),airportsto.get())
    l3=Label(windowA,text='Month:',font=("Arial Bold",10))
    l3.place(relx = 0.65, rely = 0.35)
    l3.configure(fg="White",bg="Blue")
    month=ttk.Combobox(windowA,values=['January','February','March',
                                       'April','May','June','July',
                                       'August','September','October',
                                       'November','December'])
    month.place(relx = 0.7, rely = 0.4, anchor = 'c')
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
    
    
    
                                              

    
    


    

def Railways():
    windowR=tkinter.Tk()
    windowR.title("MRF.com/Guest/choosing mode of transport/Airways")
    windowR.geometry('100x100')
    windowR.configure(bg ="Blue")
    from tkinter import Label
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
    print(railwaysfrom.current(),railwaysfrom.get())
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
    print(railwaysto.current(),railwaysto.get())
    l3=Label(windowR,text='Month:',font=("Arial Bold",10))
    l3.place(relx = 0.65, rely = 0.35)
    l3.configure(fg="White",bg="Blue")
    month=ttk.Combobox(windowR,values=['January','February','March',
                                       'April','May','June','July',
                                       'August','September','October',
                                       'November','December'])
    month.place(relx = 0.7, rely = 0.4, anchor = 'c')
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
    
    

    
    

def Roadways():
    windowr=tkinter.Tk()
    windowr.title("MRF.com/Guest/choosing mode of transport/Airways")
    windowr.geometry('100x100')
    windowr.configure(bg ="Blue")
    from tkinter import Label
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
    print(roadwaysfrom.current(),roadwaysfrom.get())
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
    print(roadwaysto.current(),roadwaysto.get())
    l3=Label(windowr,text='Month:',font=("Arial Bold",10))
    l3.place(relx = 0.65, rely = 0.35)
    l3.configure(fg="White",bg="Blue")
    month=ttk.Combobox(windowr,values=['January','February','March',
                                       'April','May','June','July',
                                       'August','September','October',
                                       'November','December'])
    month.place(relx = 0.7, rely = 0.4, anchor = 'c')
    month.current()
    l4=Label(windowr,text='Year:',font=("Arial Bold",10))
    l4.place(relx = 0.75, rely = 0.35)
    l4.configure(fg="White",bg="Blue")
    year=ttk.Combobox(windowr,values=['2020','2021','2022'])
    year.place(relx = 0.8, rely = 0.4, anchor = 'c')
    year.current()
    
    
def msg():
    from tkinter import messagebox
    messagebox.showinfo("Help","What do you need")
def Admin_id():
    adminwindow=tkinter.Tk()
    tkinter.Label(adminwindow,text="Username").grid(row=25,column=25)
    tkinter.Entry(adminwindow).grid(row=25,column=26)
    tkinter.Label(adminwindow,text="Password").grid(row=26,column=25)
    tkinter.Entry(adminwindow,show="*").grid(row=26,column=26)
def About_us():
    f=open("About us.txt","r")
    s=' '
    s=s.read()
    s=s.strip()
    print(s)
    f.close()

bt=tkinter.Button(window,text="Admin Login",fg="Orange",bg="Blue",command=Admin_id)
bt.place(relx = 0.5, rely = 0.4, anchor = 'c')
bt2=tkinter.Button(window,text="User Login",fg="Orange",bg="Blue",command=Print)
bt2.place(relx = 0.5, rely = 0.5, anchor = 'c')
bt3=tkinter.Button(window,text="Guest Login",fg="Orange",bg="Blue",command=Guest)
bt3.place(relx = 0.5, rely = 0.6, anchor = 'c')
bt4=tkinter.Button(window,text="Exit",fg="Orange",bg="Blue",command=Exit)
bt4.place(relx = 0.5, rely = 0.7, anchor = 'c')
'''from tkinter import scrolledtext

txt=scrolledtext.scrolledtext(window,width=40,height=10)'''

'''t=Entry(window,width =10)
t.grid(column = 10, row = 10)
def clicked():
    res="Welcome to"+t.get()
    l1.configure(t=res)
    
bt=tkinter.Button(window,text="Enter",fg="Orange",bg="Blue",command=clicked)

bt.grid(column=40,row=0)'''





    

window.mainloop()
