def revDigits(str):
    n= len(str)
    if n==0:
        return
    else:
        lastChar= str[n-1]
        if (lastChar.isdigit()):  #if u want only alphabet value just write .isalph()
            print(lastChar, end="")
        revDigits(str[0:n-1])  

revDigits("a1b2c3b4")