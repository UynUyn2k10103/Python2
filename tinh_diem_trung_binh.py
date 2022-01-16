def solve():
    dic = {}
    n = int(input())
    for i in input().split():
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    dic = sorted(dic.items(), key = lambda x : x[0])
    
    sum = 0.0
    dem = 0
    for i in dic:
        if i[0] == dic[0][0] or i[0] == dic[len(dic) - 1][0]:
            continue
        
        sum += float(i[0]) * i[1]
        dem += i[1]
    print('{:.2f}'.format(sum/dem))
solve()