t= int(input())
for i in range(t):
    str1= input()
    str2= input()
    for i in range(len(str1)):
        if str1[i]== str2[i]:
            print("g", end="")
        else:
            print("b", end="")
    print(end="\n")