arr= list(map(int, input().split()))
count=0
for i in range(len(arr)):
    if arr[i]>=10:
        count+=1
    else:
        pass
print(count)