n = int(input())
check = 0
res = []
L = []
for i in range(n):
    s = input().split()
    if len(L) == 0 and len(s) == 6:
        res.append(1)
    L.append(s)
    if len(L) > 1 and len(s) == 6 and len(L[-2]) == 7:
        res.append(1)
    if len(s) == 7:
        check += 1
    if check == 4:
        res.append(2)
        check = 0

print(len(res))
for i in res:
    print(i)

'''
8
Minh ve minh co nho ta
Muoi lam nam ay thiet tha man nong
Minh ve minh co nho khong
Nhin cay nho nui nhin song nho nguon
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
'''