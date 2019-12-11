from collections import Counter

def slope(tx, ty, ox, oy):
    x = ox - tx
    y = oy - ty
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
                coords.append((r, c))
    MAX = 0
    for x, y in coords:
        view = []
        for _x, _y in coords:
            if x != _x or y != _y:
                view.append(slope(x, y, _x, _y))
        MAX = max(MAX, len(Counter(view)))
    print(MAX)
