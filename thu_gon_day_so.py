n = int(input())
L = []
for i in input().split():
    if len(L) == 0:
        L.append(int(i))
    else:
        if (L[-1] + int(i)) % 2 == 0:
            L = L[:-1]
        else:
            L.append(int(i))

print(len(L))