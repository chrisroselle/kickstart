import sys

T = int(input())
for test in range(1, T+1):
    N, R, C, Sr, Sc = [int(tmp) for tmp in input().split(" ")]
    board = [[False for _ in range(C)] for _ in range(R)]
    instructions = input()
    board[Sr - 1][Sc - 1] = True
    position = [Sr - 1, Sc - 1]
    for i in instructions:
        while board[position[0]][position[1]] == True:
            if i == 'N':
                position[0] = position[0] - 1
            if i == 'S':
                position[0] = position[0] + 1
            if i == 'E':
                position[1] = position[1] + 1
            if i == 'W':
                position[1] = position[1] - 1
        board[position[0]][position[1]] = True
    print('Case #{}: {} {}'.format(test, position[0] + 1, position[1] + 1))
