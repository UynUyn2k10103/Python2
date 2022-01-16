def solve():
    s = input()
    if len(s) < 3:
        print('NO')
        return

    ind = -1
    for i in range(1, len(s)):
        if ord(s[i - 1]) < ord(s[i]):
            continue
        else:
            ind = i 
            break
    if ind == -1:
        print('NO')
        return

    for i in range(ind, len(s)):
        if ord(s[i - 1]) <= ord(s[i]):
            print('NO')
            return
    print('YES')
T = int(input())
while T != 0:
  solve()
  T -= 1