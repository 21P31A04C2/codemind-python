n=int(input())
l=list(map(int,input().split()))
e,o=0,0
for i in range(len(l)):
    if i%2==0:
        e=e+l[i]
    else:
        o=o+l[i]
if abs(e-o)==0:
    print("YES")
else:
    print("NO")