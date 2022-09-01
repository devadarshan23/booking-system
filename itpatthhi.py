def create():
    e=[]
    f1=open("itroadways.txt","w")
    f2=open("itrailways.txt","w")
    f3=open("itairways.txt","w")
    print("Input text for roadways,railways and airways and type exit to Exit ")
    for i in range(3):
        s=' '
        while True:
            s=input()
            if s.upper()=="EXIT":
                break
            s+="\n"
            e.append(s)
    f1.write(e[0])
    f2.write(e[1])
    f3.write(e[2])
    f1.close()
    f2.close()
    f3.close()
def PRINT():
    fna=input("Enter file name")
    q=fna+'.txt'
    f=open(q,"r")
    s=' '
    print("\nFile Contents:")
    while s:
        s=f.read()
        s=s.strip()
        print(s)
    f.close()
#create()
PRINT()
        
    
    
