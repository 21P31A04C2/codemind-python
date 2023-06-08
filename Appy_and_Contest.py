n=int(input())
for i in range(n):
    n,a,b,k=map(int,input().split())
    c=0
    for j in range(1,n+1):
        if c>=k:
            break
        if j%a==0 and j%b!=0:
            c=c+1
        elif j%b==0 and j%a!=0:
            c=c+1
    if c>=k:
        print("Win")
    else:
        print("Lose")