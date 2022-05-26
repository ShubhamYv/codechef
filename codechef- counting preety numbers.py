# t= int(input())
# while t>0:
#     x, y= map(int, input().split())
#     count=0
#     for i in range(x, y+1):
#         if i%10 in (2,3,9):
#             count+=1
#     print(count)
#     t-=1
#

T = int(input())
for i in range(T):
    count = 0
    L, R = list(map(int, input().split()))
    for i in range(L, R+1):
        c = i % 10
        if ((c == 2) or (c == 3) or (c == 9)):
            count = count + 1
    print(count)
