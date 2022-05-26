def bubbleSort(arr, n):
    for i in range(n):
        swapped=0
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                swapped+=1
        if swapped==0:
            break

def main():
    t= int(input())
    while t>0:
        n= int(input())
        arr= list(map(int, input().split()))
        bubbleSort(arr, n)
        for i in range(n):
            print(arr[i], end=" ")
        print()
        t-=1

if __name__ == '__main__':
    main()
