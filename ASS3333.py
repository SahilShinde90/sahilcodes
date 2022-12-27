r=int(input("Enter rows: "))
c=int(input("Enter colums: "))
a=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=int(input(f"a[{i}][{j}]: "))
        t.append(val)
    a.append(t)
b=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=int(input(f"b[{i}][{j}]: "))
        t.append(val)
    b.append(t)
add=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=a[i][j]+b[i][j]
        t.append(val)
    add.append(t)
sub=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=a[i][j]-b[i][j]
        t.append(val)
    sub.append(t)
mul=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=a[i][j]*b[i][j]
        t.append(val)
    mul.append(t)
print(a)
print(b)
print(add)
print(sub)
print(mul)

