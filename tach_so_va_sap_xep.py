n = int(input())
L = []
for i in range(n):
    s = input()
    res = ""
    j = 0
    while j < len(s):
        while j < len(s) and s[j] >= '0' and s[j] <= '9':
            res = res + s[j]
            j += 1
        if res != '':
            L.append(int(res))
            res = ''
            continue
        j += 1
        
L.sort()
for i in L:
    print(i)
