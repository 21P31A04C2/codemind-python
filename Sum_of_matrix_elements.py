r=int(input())
c=int(input())
l=[]
s=0
for i in range(r):
    l.append(list(map(int,input().split())))
for i in range(r):
    for j in range(c):
        s=s+l[i][j]
print(s)