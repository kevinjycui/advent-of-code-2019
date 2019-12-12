with open('input.txt') as f:
    moons = []
    velos = []
    for i in range(4):
        moons.append({})
        velos.append({})
        s = f.readline()[1:-2].split(', ')
        for c in s:
            moons[i][c.split('=')[0]] = int(c.split('=')[1])
            velos[i][c.split('=')[0]] = 0

    for t in range(1000):
        for m in range(len(moons)):
            for o in moons:
                for c in moons[m].keys():
                    if o[c] == moons[m][c]:
                        continue
                    velos[m][c] += (o[c]-moons[m][c])//abs(o[c]-moons[m][c])
        for m in range(len(moons)):
            for c in moons[m].keys():
                moons[m][c] += velos[m][c]

    energy = 0

    for m in range(len(moons)):
        pot = 0
        kin = 0
        for c in moons[m].keys():
            pot += abs(moons[m][c])
            kin += abs(velos[m][c])
        energy += pot*kin

    print(energy)
