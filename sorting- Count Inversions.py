def merge(arr, l, mid, r):
    n= mid-l+1
    m= r-mid
    arr1= [0]*n
    arr2= [0]*m
    for i in range(n):
        arr1[i]= arr[l+i]
    for i in range(m):
        arr2[i]= arr[mid+1+i]
    inv_count=0
    i=0
    j=0
    k=l
    while (i < n and j < m):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr[k] = arr2[j]
            inv_count += (n-1)
            k += 1
            j += 1
    while i < n:
        arr[k] = arr1[i]
        k += 1
        i += 1
    while j < m:
        arr[k] = arr2[j]
        k += 1
        j += 1
    return inv_count

def mergeSort(arr, l, r):
    inv_count=0
    if l < r:
        mid = l + (r - l)//2
        inv_count += mergeSort(arr, l, mid)
        inv_count += mergeSort(arr, mid + 1, r)
        inv_count += merge(arr, l, mid, r)
    return inv_count

def main():
    t= int(input())
    while t>0:
        n= int(input())
        arr= list(map(int, input().split()))
        print(mergeSort(arr, 0, n-1))
        t-=1

if __name__ == '__main__':
    main()


"""
Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is
already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum.
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
"""

"""Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5
has three inversions (2, 1), (4, 1), (4, 3)."""


# """BASIC APPROACH"""
# def inversionCount(arr, n):
#     count=0
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[j]< arr[i]:
#                 count+=1
#     return count
# def main():
#     t= int(input())
#     while t>0:
#         n= int(input())
#         arr= list(map(int, input().split()))
#         print(inversionCount(arr, n))
#         t-=1
# if __name__ == '__main__':
#     main()