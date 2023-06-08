n=int(input())
for i in range(n):
    s=int(input())
    b=list(map(int,input().split()))
    c=0
    for i in b:
        if i%2==1:
            c=c+1
    print(int(c/2))