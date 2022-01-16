def solve ():
  s = input() 
  if len(s) < 2:
    print("NO")
    return
  if s[-1] == '6':
    if s[-2] == '8':
      print("YES")
      return
  print("NO")
  return

T = int (input())

while T != 0:
  solve()
  T -= 1