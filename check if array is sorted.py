def isSorted(arr, n):
    if n==0 or n==1:
        return True
    for i in range(1,n):
        if arr[i-1]> arr[i]:
            return False
    return True

def main():
    n= int(input())
    arr= list(map(int,input().split()))
    print(isSorted(arr, n))

if __name__ == '__main__':
    main()