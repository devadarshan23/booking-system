def Admin():
    f=open("About us.txt","w")
    print("Enter Data for About us option")
    while True:
        s=input()
        if s.upper()=="EXIT":
            break
        s+="\n"
        f.write(s)
    f.close()
    
def Show():
    f=open("About us.txt","r")
    s=' '
    while s:
        s=f.read()
        s=s.strip()
        print(s)
    f.close()
    
Admin()
Show()
