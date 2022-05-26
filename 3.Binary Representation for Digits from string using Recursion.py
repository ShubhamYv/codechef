def revDigits(str):
    n= len(str)
    if n==0:
        return
    else:
        lastChar= str[n-1]
        revDigits(str[0:n-1])
        if (lastChar.isdigit()):
            decimalToBinary(int(lastChar))
        print()

#convert in binary
def decimalToBinary(n):
    if n==0:
        return
    else:
        decimalToBinary(int(n/2))
        print(n%2, end="")

def main():
    str= input()
    revDigits(str)

if __name__ == '__main__':
    main()