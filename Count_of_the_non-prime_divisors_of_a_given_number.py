def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1
    if c==0:
        return True
    return False
a =int(input())
c=[]
for i in range(1,a+1):
    if a%i==0:
        if prime(i):
            pass
        else:
            c.append(i)
print(len(c)+1)