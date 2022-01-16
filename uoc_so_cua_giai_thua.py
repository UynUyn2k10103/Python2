def solve():
    n, p = map (int, input().split())
    x = 0
    for i in range (p, n + 1):
        c = i
        while c % p == 0:
            x += 1
            c = int(c / p)
    print(x)

T = int(input())
for i in range(T):
    solve()