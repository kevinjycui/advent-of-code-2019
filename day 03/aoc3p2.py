with open('input.txt') as f:
    s = f.readline().split(',')
    t = f.readline().split(',')

    scale = 7000

    grid = []
    steps = []
    for i in range(scale*2):
        steps.append([0]*(scale*2))
        grid.append([0]*(scale*2))

    x = scale
    y = scale

    grid[x][y] = 1

    xl = []
    yl = []
    v = []

    for c in s:
        dire = c[0]
        magn = int(c[1:])
        
        if dire == 'U':
            for y in range(y-1, y-magn-1, -1):
                steps[x][y] = steps[x][y+1]+1
                if grid[x][y] == 0:
                    grid[x][y] = 2
                    xl.append(x)
                    yl.append(y)
                    v.append(steps[x][y])
        elif dire == 'D':
            for y in range(y+1, y+magn+1):
                steps[x][y] = steps[x][y-1]+1
                if grid[x][y] == 0:
                    grid[x][y] = 2
                    xl.append(x)
                    yl.append(y)
                    v.append(steps[x][y])
        elif dire == 'L':
            for x in range(x-1, x-magn-1, -1):
                steps[x][y] = steps[x+1][y]+1
                if grid[x][y] == 0:
                    grid[x][y] = 2
                    xl.append(x)
                    yl.append(y)
                    v.append(steps[x][y])
        elif dire == 'R':
            for x in range(x+1, x+magn+1):
                steps[x][y] = steps[x-1][y]+1
                if grid[x][y] == 0:
                    grid[x][y] = 2
                    xl.append(x)
                    yl.append(y)
                    v.append(steps[x][y])

    for i in range(scale*2):
        for j in range(scale*2):
            steps[i][j] = 0

    x = scale
    y = scale

    mn = 2000000

    for c in t:
        dire = c[0]
        magn = int(c[1:])

        if dire == 'U':
            for y in range(y-1, y-magn-1, -1):
                steps[x][y] = steps[x][y+1]+1
                if grid[x][y] == 2:
                    for p in range(len(v)):
                        if xl[p] == x and yl[p] == y:
                            mn = min(mn, steps[x][y]+v[p])
        elif dire == 'D':
            for y in range(y+1, y+magn+1):
                steps[x][y] = steps[x][y-1]+1
                if grid[x][y] == 2:
                    for p in range(len(v)):
                        if xl[p] == x and yl[p] == y:
                            mn = min(mn, steps[x][y]+v[p])
        elif dire == 'L':
            for x in range(x-1, x-magn-1, -1):
                steps[x][y] = steps[x+1][y]+1
                if grid[x][y] == 2:
                    for p in range(len(v)):
                        if xl[p] == x and yl[p] == y:
                            mn = min(mn, steps[x][y]+v[p])
        elif dire == 'R':
            for x in range(x+1, x+magn+1):
                steps[x][y] = steps[x-1][y]+1
                if grid[x][y] == 2:
                    for p in range(len(v)):
                        if xl[p] == x and yl[p] == y:
                            mn = min(mn, steps[x][y]+v[p])

    print(mn)
