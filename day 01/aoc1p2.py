import math
n = 0
sm = 0
with open('input.txt') as f:
    for n in f:
        a = int(n)
        while math.floor(a/3)-2 >= 0:
            a = math.floor(a/3)-2
            sm += a
print(sm)
