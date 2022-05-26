t= int(input())
while t>0:
    n, height= map(int, input().split())
    arr= list(map(int, input().split()))
    count=0
    for i in range(n):
        if arr[i]> height:
            count+=1
    print(count)
    t-=1