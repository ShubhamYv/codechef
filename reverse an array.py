n= int(input())
arr= list(map(int, input().split()))
low=0
high= n-1
while low< high:
    temp= arr[low]
    arr[low]= arr[high]
    arr[high]= temp
    low+=1
    high-=1
for i in range(n):
    print(arr[i], end=" ")