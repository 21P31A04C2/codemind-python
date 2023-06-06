n=int(input())
s=str(n)
e,o,m=0,0,0
for i in s:
    if int(i)%2==0:
        e=e+1
    else:
        o=o+1
if len(s)==e:
    print("Even")
elif len(s)==o:
    print("Odd")
else:
    print("Mixed")
    