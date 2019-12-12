import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

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

    ans = []

    for c in moons[0].keys():
        past = []
        t = 0
        while True:
            s = ''
            for m in range(len(moons)):
                s += str(moons[m][c])+','+str(velos[m][c])+','
            if s in past:
                break
            
            past.append(s)
            
            for m in range(len(moons)):
                for o in moons:
                    if o[c] == moons[m][c]:
                        continue
                    velos[m][c] += (o[c]-moons[m][c])//abs(o[c]-moons[m][c])
            for m in range(len(moons)):
                moons[m][c] += velos[m][c]

            t += 1
            
        ans.append(t)
    
    print(lcm(ans[0], lcm(ans[1], ans[2])))
