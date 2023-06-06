n=int(input())
o1=n*n
s=str(n)
s1=int(s[::-1])
n1=s1*s1
s2=str(n1)
o2=int(s2[::-1])
if o1==o2:
    print("True")
else:
    print("False")