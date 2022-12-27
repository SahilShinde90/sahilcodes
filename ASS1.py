Crick=[]
BadM=[]
FootB=[]

def accept(A,str):
    a=int(input("Enter the number students who like to play: "))
    print("Enter the number of students who like to play" ,str)
    for i in range(0,a):
        b=input("")
        A.append(b)
    print("successfull\n")    
    
def display(str):
    if(str=="Cricket"):
        print(Crick)
    if(str=="Badminton"):
        print(BadM)
    if(str=="Football"):
        print(FootB)

accept(Crick,"Cricket")
accept(BadM,"Badminton")
accept(FootB,"Football")

display("Cricket")
display("Badminton")
display("Football")

cm=[]
def intersection(a=[],b=[]):
    c=[]
    for i in a:
        if i in b:
            cm=c.append(i)
    return c
print(f"\nStudents who likes to play both cricket & badminton are = {intersection(Crick,BadM)}")

def twosetonly(a=[],b=[]):
    only=a+b
    for i in intersection(Crick,BadM):
        only.remove(i)
        only.remove(i)
        
    print(f"\nStudents playing either cricket or badminton but not both are = {only}")    
    
def Not2but3rd(a=[],b=[],c=[]):
    for i in c:
        if i in a:
            c.remove(i)
    for i in c:
        if i in b:
            c.remove(i)
            
    y=len(c)
    print(f"\nNumber of students who play football but not Cricket & Badminton are = {y}")

def TwobutNot3rd(a=[],b=[],c=[]):
    g=a+b
    h=intersection(a,b)
    for i in c:
        if i in g:
            g.remove(i)
    for i in c:
        if i in h:
            g.remove(i)
    
    x=len(g)
    print(f"\nNumber of students who play Cricket and Badminton but not Football are = {x}")
    
intersection(Crick,BadM)
twosetonly(Crick,BadM)
Not2but3rd(Crick,BadM,FootB)
TwobutNot3rd(Crick,BadM,FootB)
