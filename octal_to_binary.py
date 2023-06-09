n=int(input())
c=""
while n!=0:
    s=n%10
    if s==0:
        c="".join(["000",c])
    elif s==1:
        c="".join(["001",c])
    elif s==2:
        c="".join(["010",c])
    elif s==3:
        c="".join(["011",c])
    elif s==4:
        c="".join(["100",c])
    elif s==5:
        c="".join(["101",c])
    elif s==6:
        c="".join(["110",c])
    elif s==7:
        c="".join(["111",c])
    else:
        break
    n=n//10
print(int(c))