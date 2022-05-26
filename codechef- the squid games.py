t= int(input())
while t>0:
    n= int(input())
    arr= list(map(int, input().split()))
    min=10000
    sum=0
    for i in range(n):
        if arr[i]< min:
            min= arr[i]

    for j in range(n):
        sum= sum+ arr[j]

    prize= sum- min
    print(prize)
    t-=1
