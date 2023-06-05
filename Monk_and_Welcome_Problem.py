n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append(l1[i]+l2[i])
print(*l)