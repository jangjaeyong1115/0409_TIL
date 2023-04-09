from sys import stdin


T = int(stdin.readline())
numbers = ['0','1','2','3','4','5','6','7','8','9']

for i in range(T):
    x = stdin.readline().rstrip()

    b = 0

    for number in numbers:
        if x.find(number) != -1:
            b += 1
    print(b)