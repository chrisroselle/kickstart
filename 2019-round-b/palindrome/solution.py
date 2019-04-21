t = int(input())

def check(a, b):
  checkstr = master[a-1:b]
  d = {}
  for c in checkstr:
    if c not in d:
      d[c] = 1
    else:
      d[c] = (d[c] + 1) % 2
  odd = False
  for c2 in d:
    if d[c2] == 1:
      if odd == True:
         return False
      else:
        odd = True
  if odd == True:
    if (((b - a) + 1) % 2) == 1:
      return True
    else:
      return False
  return True
  

for i in range(1,t+1):
  n, q = input().split(" ")
  n = int(n)
  q = int(q)
  master = str(input())
  possible = 0
  for i2 in range(1,q+1):
    l, r = input().split(" ")
    l = int(l)
    r = int(r)
    if (check(l,r)):
      possible += 1
  print("Case #{}: {}".format(i,possible))
  