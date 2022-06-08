t= int(input())
for i in range(t):
    n= int(input())
    arr= list(map(str, input().split()))
    s_count=0
    t_count=0
    for i in range(n):
        if arr[i]== "START38":
            s_count+=1
        if arr[i]== "LTIME108":
            t_count+=1
    print(s_count, t_count)