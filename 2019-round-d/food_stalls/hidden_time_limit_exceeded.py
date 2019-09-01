import sys

def sorted_add(list, value):
    if (len(list) == 0):
        list.append(value)
        return
    min = 0
    max = len(list)
    i = max//2
    v = list[i]
    while(True):
        i = min + (max - min)//2
        v = list[i]
        #print('min: {} max: {} i: {} v: {} value: {}'.format(min, max, i, v, value))
        if (abs(max - min) <= 1):
            if (value > v):
                if (i == len(list) - 1):
                    list.append(value)
                else:
                    list.insert(i+1, value)
            else:
                if (i == 0):
                    list.insert(0, value)
                else:
                    list.insert(i-1, value)
            break
        if (value > v):
            min = i
        elif (value < v):
            max = i
        else:
            list.insert(i, value)
            break

def cost():
    return c + abs(xw - x)

T = int(input())
for test in range(1, T+1):
    K, N = (int(n) for n in input().split())
    X = [int(n) for n in input().split()]
    C = [int(n) for n in input().split()]
    # print('K = {}'.format(K))
    # print('N = {}'.format(N))
    # print('X = {}'.format(X))
    # print('C = {}'.format(C))
    total = 0
    for i, xw in enumerate(X):
        warehouse = i
        warehouse_cost = C[i]
        # the maximum value of a single stall in the current minimum
        local_max = 0
        # the total value of all stalls in current minimum
        local_total = warehouse_cost
        # the list of values
        local_mins = []
        for x, c in zip(X,C) :
            if (x == xw):
                continue;
            stall_cost = cost()
            # print('local_mins = {}'.format(local_mins))
            # print('stall cost = {}'.format(stall_cost))
            if (len(local_mins) < K):
                sorted_add(local_mins, stall_cost)
                # print('local_mins after add = {}'.format(local_mins))
                local_total = local_total + stall_cost
                if (stall_cost > local_max):
                    local_max = stall_cost
            else:
                if (stall_cost < local_max):
                    local_total = local_total - local_max + stall_cost
                    local_mins.remove(local_max)
                    # print('local_mins after remove = {}'.format(local_mins))
                    sorted_add(local_mins, stall_cost)
                    # print('local_mins after add = {}'.format(local_mins))
                    local_max = local_mins[-1]
        if (total == 0 or local_total < total):
            total = local_total   
    print('Case #{}: {}'.format(test, total))
