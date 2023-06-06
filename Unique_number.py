n=int(input())
s=str(n)
c=0
for i in s:
    if s.count(i)!=1:
        c=c+1
if c==0:
    print("Unique Number")
else:
    print("Not Unique Number")