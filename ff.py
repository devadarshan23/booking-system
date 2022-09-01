import csv
import os
def CREATE_CSV():
    f = open("Empl.csv","w")
    wobj=csv.writer(f,delimiter=",")
    while True:
        code=int(input("enter code"))
        name=input("Enter Employee name")
        age = int(input("Enter age:"))
        dept = input("Enter Department")
        sal = float(input("Enter salary"))
        wobj.writerow([code,name,age,dept,sal])
        f.flush()
        ch=input("Any more entries Y/N")
        if ch not in "Yy":
            break
    f.close()
def SHOW(fna):
    f=open(fna,"r")
    f.seek(0)
    c=0
    robj=csv.reader(f,delimiter=",")
    print("CODE\tNAME\tAGE\tDEPT\tSALARY")
    for a in robj:
        if c%2==0:
            print(a[0],a[1],a[2],a[3],a[4],sep = "\t")
        c+=1
    f.close
#CREATE_CSV()
#SHOW("Empl.csv")

'''def APPEND():
    f=open("chennai.txt",'a')
    print("Enter information about chennai and type 'Exit' to stop:")
    while True:
        s=input()
        if s.upper()=='EXIT':
            break
        s+='\n'
        f.write(s)
    f.close()
def PRINT():
    f=open("chennai.txt","r")
    s='  '
    print("\nFile Contents:")
    while s:
        s=f.read()
        s=s.strip()
        print(s)
    f.close()'''

#APPEND()
def SEARCH():
    f=open("Empl.csv","r")
    f.seek(0)
    c=0
    sc=int(input("Enter Employee code to be searched"))
    robj=csv.reader(f,delimiter =",")
    for a in robj:
        if c%2==0 and int(a[0])==sc:
            print("Record found",a[0],a[1],a[2],a[3],a[4])
            break
        else:
            print("searching record not found")
    f.close()
#SEARCH()
def SORT():
    f=open("Empl.csv","r")
    f.seek(0)
    c=0
    robj=csv.reader(f,delimiter =",")
    s=[]
    for a in robj:
        if c%2==0:
            s.append(a)
        c+=1
    f.close()
    for i in range(len(s)-1):
        for j in range(len(s)-i-1):
             if s[j][1]>s[j+1][1]:
                 s[j],s[j+1]=s[j+1],s[j]
    print("Sorted records")
    print("Code \tName \tAge \t Dept \tSalary")
    for a in s:
        print(a[0],a[1],a[2],a[3],a[4], sep ="\t")
SORT()





'''def CREATE():
    f=open("story.txt","a")
    print("Enter story and 'Exit' to stop:")
    while True:
        s=input()
        if s.upper()=="EXIT":
            break
        s+="\n"
        f.write(s)
    f.close()
def PRINT():
    f=open("story.txt","r")
    s=' '
    c=0
    while s:
        s=f.readline()
        c+=1
        s.strip()
        print(s)
    print("Total no of lines:",c-1)
    f.close()
def COUNT():
    f=open("story.txt","r")
    s,c =' ',0
    while s:
        s=f.read()
        s=s.strip()
        for a in s.split():
            b=a[::-1]
            if a==b:
                c+=1
    f.close()
    print("No of palindrome words:",c)
CREATE()
PRINT()
COUNT() '''

