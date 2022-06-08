t= int(input())
while t!=0:
    n= int(input())
    arr= list(map(int, input().split()))
    count=0
    for i in range(n):
        if arr[i]>= 1000:
            count+=1
        else:
            pass
    print(count)
    t-=1