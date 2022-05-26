# def countTheTriangle(arr, n):  #O(n^3)
#     count=0
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1, n):
#                 if (arr[i]+arr[j]>arr[k] and arr[i]+arr[k]>arr[j] and arr[k]+arr[j]>arr[i]):
#                     count+=1
#     return count

def countTheTriangle(arr,n): #O(n^2)
    arr.sort()
    count=0
    for i in range(n-1, 0, -1):
        l=0
        r=i-1
        while (l<r):
            if arr[l]+arr[r]>arr[i]:
                count+=r-l
                r-=1
            else:
                l+=1
    return count

def main():
    n= int(input())
    arr= list(map(int, input().split()))
    print(countTheTriangle(arr, n))

if __name__ == '__main__':
    main()