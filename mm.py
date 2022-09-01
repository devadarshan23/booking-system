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
adminku=[["Srijith","12f214"],["Devadarshan","12f207"],["Syed","12f242"],["1","1"]]
f=open("Airways.csv","r")
robj=csv.reader(f,delimiter=",")
e=list(robj)
c=0
for i in range(3):   
    m=Label(window,text=i,font=("Arial Bold",15))
    m.configure(fg="Black",bg="orange")
    b=0.3+i
    m.place(relx=0.5, rely=b, anchor="center")


''''for i in range(len(e)):
    if c%2==0:
        m='b'
        k=str(i) 
        m+=k
        print(m)
        print(e[i])
        m=Label(window,text=e[i],font=("Arial Bold",15))
        m.configure(fg="Black",bg="orange")
        b=0.3+i
        m.place(relx=0.5, rely=b, anchor="center")
    c+=1
window.mainloop()'''
    
