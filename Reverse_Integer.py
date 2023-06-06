n=int(input())
s=str(n)
if n<0:
    n=-n
    s=str(n)
    print(-int(s[::-1]))
else:
    print(int(s[::-1]))
    