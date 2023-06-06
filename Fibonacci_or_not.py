n=int(input())
c,a,b=0,1,1
if n==0 or n==1:
    print("True")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("True")
    else:
        print("False")