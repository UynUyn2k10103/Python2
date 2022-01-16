def solve():
  s = input()
  for i in s:
    if i != '4' and i != '7':
      print("NO")
      return
  print("YES")

T = int (input())
while T != 0:
  solve()
  T -= 1
