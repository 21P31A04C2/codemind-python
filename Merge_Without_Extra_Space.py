n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    c=l1+l2
    c.sort()
    print(*c)
    