n=int(input())
s=len(str(n))
p=0
sum=0
for i in str(n):
    p=p+1
    for j in range(p,n+1):
        sum+=int(i)**j
        break

if n==sum:
    print("True")
else:
    print("False")