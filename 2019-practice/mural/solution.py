import sys, math

T = int(input())
for test in range(T):
    N = int(input())
    wall = []
    totals = []
    total = 0
    instring = input()
    for n in instring:
        wall.append(int(n))
    length = math.ceil(len(wall) / 2)
    for i, n in enumerate(wall):
        if (i + 1 < length):
            total = total + n
        if (i + 1 == length):
            total = total + n
            totals.append(total)
        if (i + 1 > length):
            total = total + n - wall[i - length]
            totals.append(total)
    print('Case #{}: {}'.format(test + 1, max(totals)))
