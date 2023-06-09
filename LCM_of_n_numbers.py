from math import gcd
n=int(input())
l=list(map(int,input().split()))
c=1
for i in l:
    c=c*i//gcd(c,i)
print(c)