def thuan_nghich(s):
    s1 = s[::-1]
    if s1 == s:
        return True
    return False

def chan(s):
    for i in s:
        if int(i) % 2 == 1:
            return False
    return True

def solve():
    n = int (input())
    i = 22
    tmp = 100
    while i < n:
        if thuan_nghich(str(i)) and chan(str(i)):
            print(i, end = ' ')
        if i == tmp:
            i = tmp * 10
            tmp *= 100
        else:
            i += 2
    print()

T = int(input())

for t in range(T):
    solve()