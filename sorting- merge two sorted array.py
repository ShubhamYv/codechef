def mergeTwoSortedArray(arr1, arr2, n, m):
    arr3= [None]*(n+m)
    i=0
    j=0
    k=0
    while (i<n and j<m):
        if arr1[i]< arr2[j]:
            arr3[k]= arr1[i]
            k+=1
            i+=1
        else:
            arr3[k]= arr2[j]
            k+=1
            j+=1

    while i<n:
        arr3[k]= arr1[i]
        k+=1
        i+=1

    while j<m:
        arr3[k]= arr2[j]
        k+=1
        j+=1
    return arr3

def main():
    t= int(input())
    while t>0:
        n= int(input())
        arr1= list(map(int, input().split()))
        m= int(input())
        arr2= list(map(int, input().split()))
        res= mergeTwoSortedArray(arr1, arr2, n, m)
        for i in range(n+m):
            print(res[i], end=" ")
        print()
        t-=1

if __name__ == '__main__':
    main()
