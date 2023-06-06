def fun(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1
    if c==0:
        return True
    return False
a=int(input())
b=int(input())
for i in range(a,b):
    if i>1:
        if fun(i):
            print(i)