def cal(s):
    res = 0
    tmp = 1
    i = len(s) - 1
    while i >= 0:
        res = res + int(s[i]) * tmp
        tmp = tmp * 2
        i = i - 1
    return res

tn_2 = [0]

def Prepare(s):
    if len(s) > 21:
        return
    if len(s) > 0 and s[0] != '0':
        tn_2.append(cal(s))
    Prepare('0' + s + '0')
    Prepare('1' + s + '1')

def check(n):
    s = ""
    while n > 0:
        s = str(n % 3) + s
        n = int(n / 3)
    if s == s[::-1]:
        return True
    return False

def thuan_nghich():
    a, b, m = map(int, input().split())
    if m > 3:
        res = 0
        for i in range(2):
            if i >= a and i <= b:
                res = res + 1
        print(res)
        return
    Prepare('')
    Prepare('0')
    Prepare('1')

    tn_2.sort()
    A = set(tn_2)


    if m == 3:
        tn_3 = []
        res = 0
        for i in A:
            if check(i) == True:
                tn_3.append(i)
        for i in tn_3:
            if i >= a and i <= b:
                res = res + 1
        print(res)
        return
    res = 0
    for i in A:
        if i >= a and i <= b:
            res = int(res + 1)
    print(res)


thuan_nghich()