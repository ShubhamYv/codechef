"""NOTE: t(n)=O(n)"""
def sorting(arr,n):
    low=0
    high= n-1
    mid=0
    while mid<=high:
        if arr[mid]==0:
            arr[mid], arr[low]= arr[low], arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid], arr[high]= arr[high], arr[mid]
            high-=1
    return arr

def main():
    n= int(input())
    arr= list(map(int, input().split()))
    sorting(arr, n)
    for i in range(n):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    main()