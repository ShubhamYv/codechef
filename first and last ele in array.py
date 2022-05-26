def main():
    n= int(input())
    arr= list(map(int, input().split()))
    ele= int(input())
    first=-1
    last=-1
    for i in range(n):
        if arr[i]== ele:
            if first==-1:
                first= i
            else:
                last= i
        else:
            pass
    print(first, last)

if __name__ == '__main__':
    main()

