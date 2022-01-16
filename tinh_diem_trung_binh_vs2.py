from decimal import ROUND_HALF_UP, Decimal


class SinhVien():
    def __init__(self, ma, ten, mon1, mon2, mon3):
        self.ma = 'SV{:02d}'.format(ma)
        self.ten = ten
        tmp = Decimal((mon1 * 3 + mon2 * 3 + mon3 * 2)) / Decimal(8)
        tmp = tmp.quantize(Decimal('0.01'), ROUND_HALF_UP)
        self.trungbinh = tmp #'{:.2f}'.format(tmp)
    def printf(self, thuhang):
        print(self.ma, self.ten, self.trungbinh, thuhang)

n = int(input())
L = []
for i in range(1, n + 1):
    name = input().strip()
    tmp = name.split()
    name = ' '.join(tmp).strip().title()
    mon1 = Decimal(input())
    mon2 = Decimal(input())
    mon3 = Decimal(input())
    # tmp = Decimal((mon1 * 3 + mon2 * 3 + mon3 * 2)) / Decimal(8)
    
    L.append(SinhVien(i, name, mon1, mon2, mon3))

L = sorted(L, key=lambda x : (-Decimal(x.trungbinh), x.ma))

dem = 0

i = 0

while i < n:
    dem = i  + 1
    vt = i
    while i < n and L[i].trungbinh == L[vt].trungbinh:
        L[i].printf(dem)
        i += 1 


