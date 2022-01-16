from decimal import ROUND_HALF_UP, Decimal
import decimal
from fractions import Fraction

class HS():
    def __init__(self, ma, name, diem):
        self.ma = ma
        self.name = name
        self.diem = diem
    def phanloai(self):
        if self.diem > 9.5:
            self.loai = 'XUAT SAC'
        elif self.diem >= 8.0:
            self.loai = 'DAT'
        elif self.diem >= 5.0:
            self.loai = 'CAN NHAC'
        else:
            self.loai = 'TRUOT'
    
    def total(self):
        self.phanloai()
        print(self.ma, self.name, self.diem, self.loai)
n = int(input())
L = []

for i in range(n):

    name = ' '.join(input().split()).strip().title()
    diem = 0
    diem = Decimal(0)
    for i in range(2):
        tmp = Decimal(input())
        if tmp > 10:
            tmp /= Decimal(10)
        diem += tmp
    diem /= Decimal(2)
    diem = diem.quantize(Decimal('0.01'), ROUND_HALF_UP)
    id = 'TS{:02d}'.format(i + 1)
    L.append(HS(id, name, diem))

l = sorted(L, key= lambda x : (- x.diem))
for hs in l:
    hs.total()

'''
3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
'''