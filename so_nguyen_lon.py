def prepare(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else: b %= a
    
    return a + b

n = int(input())
sum = 0

while n > 0:
    n -= 1
    a = int(input())
    b = int(input())
    print(prepare(a, b))