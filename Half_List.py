n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)-1,len(l)//2-1,-1):
    l1.append(l[i])
for i in range(0,len(l)//2):
    l1.append(l[i])
print(*l1)