import pickle
def CREATE():
    e=[]
    f=open("Admin Id and Password.dat","wb")
    while True:
        Username=input("Enter the username")
        Password=input("Enter the Password")
        e.append([Username,Password])
        ch=input("Any more entries y/n")
        if ch not in "Yy":
            break
    pickle.dump(e,f)
    f.close()
def SHOW():
    e=[]
    f=open("Admin Id and Password.dat","rb")
    e=pickle.load(f)
    for a in e:
        print(a)
    f.close()
CREATE()
SHOW()

