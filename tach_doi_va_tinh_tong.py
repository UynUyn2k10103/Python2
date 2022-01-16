def solve():
    s = input()
    n = len(s)
    if n == 1:
        print(s)
        return

    while n > 1:
        a = int(len(s) / 2)
        a = int(s[0 : a]) + int (s[a : n])
        print(a)
        s = str(a)
        n = len(s)

solve()