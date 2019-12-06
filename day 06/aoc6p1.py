with open('input.txt') as f:
    ref = {}
    orbits = []
    i = 0
    for n in f:
        m = n.split(')')
        if m[0].strip() not in ref.keys():
            ref[m[0].strip()] = i
            i += 1
        if m[1].strip() not in ref.keys():
            ref[m[1].strip()] = i
            i += 1
        while len(orbits)<=i:
            orbits.append([])
        orbits[ref[m[0].strip()]].append(ref[m[1].strip()])

    count = 0

    for o in range(len(orbits)):
        q = [o]
        while len(q)>0:
            p = q.pop()
            for j in orbits[p]:
                q.append(j)
                count += 1

    print(count)
