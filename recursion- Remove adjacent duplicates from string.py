def remAdjDuplicate(str):
    if (len(str)==1):
        return str
    if (str[0]==str[1]):
        return remAdjDuplicate(str[1:])
    return str[0]+remAdjDuplicate(str[1:])

def main():
    str= input()
    print(remAdjDuplicate(str))

if __name__ == '__main__':
    main()