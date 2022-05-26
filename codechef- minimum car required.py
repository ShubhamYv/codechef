t= int(input())
while t>0:
    n= int(input())
    if n%4==0:
        res= n/4
    else:
        res= n//4+1
    print(int(res))
    t-=1
