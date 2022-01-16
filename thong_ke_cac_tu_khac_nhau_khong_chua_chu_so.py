import re

dic = {}
def solve():
    s = input()
    reg = '[a-zA-Z]+'
    s = re.findall(reg, s)
    for i in  s:
        i = i.lower()
        try:
            dic[i] += 1
        except:
            dic[i] = 1
T = int(input())
while T:
    solve()
    T -= 1
dic = sorted(dic.items(), key = lambda x : (-x[1], x[0]))
for i in dic:
    print(i[0], i[1])