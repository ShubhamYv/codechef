def merge(arr, l, mid, r):
    n= mid-l+1
    m= r-mid
    arr1= [0]*n
    arr2= [0]*m
    for i in range(n):
        arr1[i]= arr[l+i]
    for i in range(m):
        arr2[i]= arr[mid+1+i]
    i=0
    j=0
    k=l
    while (i<n and j<m):
        if arr1[i]< arr2[j]:
            arr[k]=arr1[i]
            k+=1
            i+=1
        else:
            arr[k]=arr2[j]
            k+=1
            j+=1
    while i<n:
        arr[k] = arr1[i]
        k += 1
        i += 1
    while j<m:
        arr[k] = arr2[j]
        k += 1
        j += 1
    return arr

def mergeSort(arr, l, r):
    if l<r:
        mid= l+(r-l)//2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)
        merge(arr, l, mid, r)

def main():
    n= int(input())
    arr= list(map(int, input().split()))
    mergeSort(arr, 0, n-1)
    for i in range(n):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    main()