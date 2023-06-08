l=input()
l1=[]
s=[]
u=[]
for i in l:
    if i!=' ' and i in 'aeiouAEIOU' and i not in l1:
        l1.append(i)
for i in l1:
    if i.islower():
        s.append(i)
    else:
        u.append(i)
if len(s)==5 or len(u)==5:
    print("True")
else:
    print("False")