a=int(input())
b=int(input())
l1=[]
l2=[]
c,d=0,0
for i in range(1,a):
    if a%i==0:
        c=c+i
for i in range(1,b):
    if b%i==0:
        d=d+i
if a==d and b==c:
    print("Amicable")
else:
    print("Not Amicable")