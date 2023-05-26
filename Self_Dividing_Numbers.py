def selfnum(n):
    t=n
    while t:
        d=t%10
        t=t//10
        if d==0 or n%d!=0:
            return False
    return True
n=int(input())
m=int(input())
for i in range(n,m+1):
    if selfnum(i):
        print(i,end=' ')
    