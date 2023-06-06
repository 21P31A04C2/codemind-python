n=int(input())
for i in range(n):
    a=int(input())
    s=str(a)
    if a==int(s[::-1]):
        print("True")
    else:
        print("False")