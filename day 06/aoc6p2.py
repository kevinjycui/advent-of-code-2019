depth = []
orbits = []
ref = {}

class Orbit(object):
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent

def dfs(node, d):
    depth[node] = d
    for o in orbits:
        if o.parent == node:
            dfs(o.node, d+1)

def lca(a, b):
    dist = 0
    while depth[a] > depth[b]:
        print(depth[a], depth[b])
        for o in orbits:
            if o.node == a:
                a = o.parent
                dist += 1
                break
    while depth[b] > depth[a]:
        print(depth[a], depth[b])
        for o in orbits:
            if o.node == b:
                b = o.parent
                dist += 1
                break
    while a != b:
        print(depth[a], depth[b])
        for o in orbits:
            if o.node == a:
                a = o.parent
                dist += 1
                break
        for o in orbits:
            if o.node == b:
                b = o.parent
                dist += 1
                break

    print(depth[a], depth[b])
    return dist-2

with open('input.txt') as f:
    i = 0
    for n in f:
        m = n.split(')')
        if m[0].strip() not in ref.keys():
            ref[m[0].strip()] = i
            i += 1
        if m[1].strip() not in ref.keys():
            ref[m[1].strip()] = i
            i += 1
        orbits.append(Orbit(ref[m[1].strip()], ref[m[0].strip()]))

    depth = [0]*i
    root = ref['COM']
    start = ref['YOU']
    end = ref['SAN']

    dfs(root, 0)

    print(lca(start, end))
