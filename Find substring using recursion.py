def isSubstring(str1, str2):
    size1= len(str1)
    size2= len(str2)
    if size1==0:
        return False
    if size2==0:
        return True
    if str1[0]==str2[0]:
        return exactSame(str1,str2)
    return isSubstring(str1[1:], str2)

def exactSame(str1, str2):
    size1= len(str1)
    size2= len(str2)
    if size1==0:
        return False
    if size2==0:
        return True
    if str1[0]==str2[0]:
        return exactSame(str1[1:], str2[1:])
    return False

def main():
    t= int(input())
    while t>0:
        str1, str2= map(str, input().split())
        res=isSubstring(str1,str2)
        if (res== True):
            print("YES")
        else:
            print("NO")
        t-=1

if __name__ == '__main__':
    main()

