n=int(input("Enter number of students: "))
present,sum,min,max,absent=0,0,51,-1,0
marks=[]
for i in range(n):
    temp = input("\nEnter Marks of students "+str(i+1)+" or AB if absent: ")
    marks.append(temp)
    if temp!="AB":
        present+=1
        sum+=int(temp)
        if int(temp)>max:
            max=int(temp)
        if int(temp)<min:
            min=int(temp)
        else:
            absent+=1
avg=sum/present
    
max_f=0
mark=[]
for i in range(0,51):
    f=0
    for j in marks:
        if j!="AB" and i==int(j):
            f+=1
        if f>max_f:
            max_f=f
            mark.clear()
            mark.append(i)
        elif f==max_f:
            mark.append(i)
            
print("\nAverage:", avg)            
print("\nHighest and Lowest marks are:",max, "and ",min,)
print("\nAbsent are:", absent)
print("\nHighest frequency are",max_f," is: ",mark)
