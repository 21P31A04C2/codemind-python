def fun(n):
    s=str(n)
    x1=int(s[::-1])+n
    s1=str(x1)
    if x1==int(s1[::-1]):
        return x1
    else:
        return fun(x1)
x=int(input())
print(fun(x))
