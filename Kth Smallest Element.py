def bubbleSort(arr, n):
    for i in range(n):
        swapped=0
        for j in range(n-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                swapped+=1
        if swapped==0:
            break


def main():
    n= int(input())
    arr= list(map(int, input().split()))
    k= int(input())
    res=0
    bubbleSort(arr, n)
    for i in range(n):
        res= arr[k-1]
    print(res)

if __name__ == '__main__':
    main()