# cook your dish here
for i in range(int(input())):
    N=int(input())
    array=list(map(int,input().split()))
    K=int(input())
    before=array[K-1]
    array.sort()
    after=array.index(before)
    print(after+1)