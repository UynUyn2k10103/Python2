def prepare():
    num = 10**6
    num *= 2
    l = [0] * (num + 1)

    for i in range (2, num + 1):
        if l[i]: continue
        for j in range (i, num + 1, i):
            tmp = j // i
            l[j] = l[tmp] + i
    
    return l 


n = int(input())
sum = 0

l = prepare()

while n > 0:
    n -= 1
    tmp = int(input())
    sum += l[tmp]

print(sum)