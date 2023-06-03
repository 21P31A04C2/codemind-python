n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    s=str(i)
    c=0
    for i in s:
        c=c+1
    if c%2==0:
        l1.append(int(s))
print(len(l1))       