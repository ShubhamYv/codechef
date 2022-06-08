t= int(input())
while t>0:
    a, b= map(int, input().split())
    sum= list(str(a+b))
    count=0
    for i in range(len(sum)):
        if (sum[i] == '1'):
            count = count + 2
            continue
        elif (sum[i] == "0" or sum[i] == "6" or sum[i] == "9"):
            count = count + 6
            continue
        elif (sum[i] == '2' or sum[i] == "3" or sum[i] == "5"):
            count = count + 5
            continue
        elif (sum[i] == "4"):
            count = count + 4
            continue
        elif (sum[i] == "7"):
            count = count + 3
            continue
        else:
            count = count + 7
            continue
    print(count)
    t-=1