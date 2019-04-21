t = int(input())

def get_value(l, r):
  check = trinkets[l:r+1]
  d = {}
  over = []
  indexes = {}
  over_indexes = {}
  i = 0
  for t in check:
    if t not in d:
      d[t] = 1
      indexes[t] = []
      indexes[t].append(i)
    else:
      if d[t] == s:
        d[t] = 0
        over.append(t)
        over_indexes[t] = indexes[t]
      if t not in over:
        d[t] = (d[t] + 1)
        indexes[t].append(i)
      else:
        over_indexes[t].append(i)
    i += 1
  return sum(d.values()), over, over_indexes
  
def checks(over, over_indexes):
  mins = []
  maxes = []
  pairs = []
  mins.append(0)
  mins.append(n-1)
  for i in over:
    oitotal = len(over_indexes[i])
    excess = oitotal - s
    # mins
    for i2 in over_indexes[i][0:excess]:
      if i2 + 1 not in mins:
          mins.append(i2 + 1)
    # maxes
    for i2 in over_indexes[i][-excess:]:
      if i2 - 1 not in mins:
          mins.append(i2 - 1)
  for j in mins:
    for k in mins:
      if j >= k:
        continue
      pairs.append([j,k])
  return pairs

for i in range(1,t+1):
  n, s = input().split(" ")
  n = int(n)
  s = int(s)
  trinkets = input().split(" ")
  trinkets = list(map(int, trinkets))
  value, over, over_indexes = get_value(0, n-1)
  pairs = checks(over, over_indexes)
  values = []
  for j in pairs:
    value, over, over_indexes = get_value(j[0], j[1])
    values.append(value)
  print("Step #{}: {}".format(i, max(values)))

  