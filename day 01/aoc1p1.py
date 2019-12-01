import math
sm = 0
with open('input.txt') as f:
    for n in f:
        sm += math.floor(int(n)/3)-2
print(sm) #3390830
