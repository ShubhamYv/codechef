t= int(input())
while t>0:
    x, y= map(int, input().split())
    month= 30
    expend= x- (30*y)
    if expend>=0:
        print("YES")
    else:
        print("NO")
    t-=1