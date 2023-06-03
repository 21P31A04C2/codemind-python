import math
def isprime(n):
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
    
s=int(input())
l=list(map(int,input().split()))
n,p=1,1
for i in l:
    if isprime(i):
        p=p*i
    else:
        n=n*i
print(abs(p-n))
