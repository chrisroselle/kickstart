from sys import stdout as o

t = int(input())
for i in range(1, t + 1):
    a, b = [int(s) for s in input().split(" ")]
    n = int(input())
    guesses = 0
    while (guesses < n):
        guess = (a + (b-a)//2)
        print(guess)
        o.flush()
        guesses = guesses + 1
        response = str(input())
        if (response == "CORRECT" or response == "WRONG_ANSWER"):
            break
        if (response == "TOO_BIG"):
            b = guess
        if (response == "TOO_SMALL"):
            a = guess