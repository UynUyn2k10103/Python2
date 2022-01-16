import re

dic = {}

def solve():
    s = input()
    reg = '\w+'
    s = re.findall(reg, s)
    for i in  s:
        i = i.lower()
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    
T, k= map (int, input().split())
while T:
    solve()
    T -= 1

dicn = {}


for i in dic:
    if dic[i] >= k:
        dicn.setdefault(i, dic[i])
    
dicn = sorted(dicn.items(), key = lambda x : (-x[1], x[0]))
for j in dicn:
    print(j[0], j[1])