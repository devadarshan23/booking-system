a=[]
n= int(input("**Enter number of Entries**\n"))
print("*****Enter",n,"names,classes and sections with a maximum of 24 characters each*****\n")
for i in range(n):
    b=[]
    name=input("\t\t\t\tEnter Name    : ")
    classs=input("\t\t\t\tEnter Class   : ")
    section= input("\t\t\t\tEnter Section : ")
    b.append(name)
    b.append(classs)
    b.append(section)
    a.append(b)
print("\t")
print("-"*98)
print("\t ","NAME" +' '*20,"\tCLASS" +' '*19,"\tSECTION"+' '*17)
print("\t")
print("-"*98)
for i in a:
    print()
    for j in i:
        print("\t",j+ ' '*(25-len(j)),end = ' ')
print()
print("\t")
print("-"*98)
print("CC")
