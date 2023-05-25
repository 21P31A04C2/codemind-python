n=input().lower()
s=list(n.split())
c=0
#print(s)
for i in s:
    if i==i[::-1]:
        c=c+1
print(c)