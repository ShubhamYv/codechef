t= int(input())
p1_score, p2_score, lead, leader=0, 0, 0, 0
while t!=0:
    p1, p2= map(int, input().split())
    p1_score+= p1
    p2_score+= p2
    diff= p1_score- p2_score

    if diff>0 and diff> lead:
        lead= diff
        leader=1

    elif diff<0 and abs(diff)> lead:
        lead= abs(diff)
        leader= 2
    t-=1
print(leader, lead)