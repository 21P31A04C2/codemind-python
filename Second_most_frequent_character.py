def fun(n):
    no=256
    c=[0]*no
    for i in range(len(n)):
        c[ord(n[i])]=c[ord(n[i])]+1
    f,s=0,0
    for i in range(no):
        if c[i]>c[f]:
            s=f
            f=i
        elif (c[i]>c[s] and c[i]!=c[f]):
            s=i
    return chr(s)
s=input()
r=fun(s)
if r!=NULL:
    print(r)
else:
    print('-1')