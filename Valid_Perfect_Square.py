import math
def fun(n):
    s=int(math.sqrt(n))
    if n==s*s:
        return True
    else:
        return False
n=int(input())
for i in range(n):
    s=int(input())
    if fun(s):
        print("True")
    else:
        print("False")