t= int(input())
while t>0:
    x, y= map(int, input().split())
    if x<y:
        print("FIRST")
    elif x>y:
        print("SECOND")
    else:
        print("ANY")
    t-=1