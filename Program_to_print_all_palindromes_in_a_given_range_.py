def fun(n):
    s=str(n)
    if n==int(s[::-1]):
        return True
    return False
a=int(input())
b=int(input())
for i in range(a,b):
    if fun(i):
        print(i,end=' ')