import math
from collections import Counter

def quad(x, y):
    if x >= 0 and y > 0:
        return 1
    if x > 0 and y <= 0:
        return 2
    if x <= 0 and y < 0:
        return 3
    if x < 0 and y >= 0:
        return 4

def pythag(ax, ay, bx, by):
    return math.sqrt((ax - bx)**2 + (ay - by)**2)

def cotangent(x, y):
    if y == 0:
        return x
    return x/y

class Asteroid(object):
    def __init__(self, x, y, dx, dy, q, dist):
        self.x, self.y, self.dx, self.dy, self.q, self.dist = x, y, dx, dy, q, dist
    def __gt__(self, other):
        if self.q == other.q:
            cot_s = cotangent(self.dx, self.dy)
            cot_o = cotangent(other.dx, other.dy)
            if cot_s == cot_o:
                return self.dist > other.dist
            return cot_s > cot_o
        return self.q > other.q

def slope(tx, ty, ox, oy):
    x = ox - tx
    y = - (oy - ty)
    fctr = 2
    while fctr <= abs(x) and fctr <= abs(y):
        if x % fctr == 0 and y % fctr == 0:
            x //= fctr
            y //= fctr
        else:
            fctr += 1
    if x == 0:
        y //= abs(y)
    if y == 0:
        x //= abs(x)
    return x, y

with open('input.txt') as f:
    graph = []
    
    for n in f:
        graph.append(n)
    coords = []
    for r in range(len(graph)):
        for c in range(len(graph[r])):
            if graph[r][c] == '#':
                coords.append((c, r))

    MAX = 0
    view = []
    MX, MY = -1, -1
    for x, y in coords:
        asteroids = []
        check = []
        for _x, _y in coords:
            if x != _x or y != _y:
                slp = slope(x, y, _x, _y)
                asteroids.append(Asteroid(_x, _y, slp[0], slp[1], quad(slp[0], slp[1]), pythag(x, y, _x, _y)))
                check.append(slp)
        if MAX < len(Counter(check)):
            MAX = len(Counter(check))
            view = asteroids.copy()
            MX, MY = x, y

    view.sort()

    total = []

    while len(view) > 0:
        revolution = []
        v = 0
        while v < len(view):
            if (view[v].dx, view[v].dy) not in revolution:
                total.append(view[v].x * 100 + view[v].y)
##                print(str(len(total))+' at', view[v].x, view[v].y)
                revolution.append((view[v].dx, view[v].dy))
                view.pop(v)
            else:
                v += 1
    
    print(total[199])

            
