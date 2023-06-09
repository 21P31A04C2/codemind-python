n=int(input())
for i in range(n):
    s=input()
    x=[]
    y=[]
    c=0
    m=len(s)
    for i in range(m-1,-1,-1):
        if s[i]!='':
            x.append(s[i])
    for i in s:
        if i!='':
            y.append(i)
    for i in range(len(x)):
        if x[i]==y[i]:
            c=c+1
    if c==len(x) and len(x)%2==0:
        print("YES EVEN")
    elif c==len(x) and len(x)%2!=0:
        print("YES ODD")
    else:
        print("NO")