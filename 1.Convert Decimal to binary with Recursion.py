def decimalToBinary(n):
    if n==0:
        return
    else:
        decimalToBinary(int(n/2))
        print(n%2, end="")

def main():
    t= int(input())
    while t>0:
        n= int(input())
        decimalToBinary(n)
        t-=1

if __name__ == '__main__':
    main()