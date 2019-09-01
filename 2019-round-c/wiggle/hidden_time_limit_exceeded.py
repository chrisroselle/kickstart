import sys

T = int(input())
for test in range(1, T+1):
    N, R, C, Sr, Sc = [int(tmp) for tmp in input().split(" ")]
    instructions = input()
    visited = []
    visited.append((Sr - 1, Sc - 1))
    position = [Sr - 1, Sc - 1]
    for i in instructions:
        while (position[0], position[1]) in visited:
            if i == 'N':
                position[0] = position[0] - 1
            if i == 'S':
                position[0] = position[0] + 1
            if i == 'E':
                position[1] = position[1] + 1
            if i == 'W':
                position[1] = position[1] - 1
        visited.append((position[0], position[1]))
    print('Case #{}: {} {}'.format(test, position[0] + 1, position[1] + 1))
