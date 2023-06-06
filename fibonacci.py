n=int(input())
count=3
l=[0,1,1]
c,a,b=0,1,1
while count<n:
    c=a+b
    l.append(c)
    count=count+1
    b=a
    a=c
print(*l)