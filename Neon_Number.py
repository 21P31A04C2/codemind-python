n=int(input())
n1=n*n
s=str(n1)
c=0
for i in s:
    c=c+int(i)
if c==n:
    print("Neon Number")
else:
    print("Not Neon Number")