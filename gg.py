import pickle
def CREATE():
    b=[]
    f=open("books.dat","wb")
    while True:
        bcode=int(input("enter book code"))
        title=input("Book title")
        subject=input("Subject")
        qty=int(input("Enter Quantity"))
        price=float(input("Enter Price"))
        b.append([bcode,title,subject,qty,price])
        ch=input("Any more books y/n")
        if ch not in "Yy":
            break
    pickle.dump(b,f)
    f.close()
def SHOW():
    b=[]
    f=open("books.dat","rb")
    b=pickle.load(f)
    for a in b:
        print(a)
    f.close()
CREATE()
SHOW()
    
