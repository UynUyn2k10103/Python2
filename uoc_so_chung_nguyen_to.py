def Ucln(a, b):
  while a * b != 0:
    if a >= b:
      a %= b
    else:
      b %= a
  return a + b

def check(a, b):
  a = Ucln(a, b)
  s = str (a)
  a = 0
  for i in s:
    a += int(i)
  if a < 2:
    print ("NO")
    return
  i = 2
  while i * i <= a:
    if a % i == 0:
      print("NO")
      return
    i += 1
  print("YES")

def solve():
  Input = [int (i) for i in input().split()]
  check(Input[0], Input[1])

T = int (input())
while T != 0:
  solve()
  T -= 1
