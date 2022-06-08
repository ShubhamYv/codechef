t= int(input())
for i in range(t):
    str= input()
    if str[0:]== str[::-1]:
        print("wins")
    else:
        print("loses")