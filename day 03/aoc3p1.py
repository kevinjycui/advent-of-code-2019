with open('input.txt') as f:
    s = f.readline().split(',')
    t = f.readline().split(',')

    scale = 10000

    grid = []
    for i in range(scale*2):
        grid.append([0]*(scale*2))

    x = scale
    y = scale

    grid[x][y] = 1

    for c in s:
        dire = c[0]
        magn = int(c[1:])
        
        if dire == 'U':
            for y in range(y-1, y-magn-1, -1):
                if grid[x][y] == 0:
                    grid[x][y] = 2
        elif dire == 'D':
            for y in range(y+1, y+magn+1):
                if grid[x][y] == 0:
                    grid[x][y] = 2
        elif dire == 'L':
            for x in range(x-1, x-magn-1, -1):
                if grid[x][y] == 0:
                    grid[x][y] = 2
        elif dire == 'R':
            for x in range(x+1, x+magn+1):
                if grid[x][y] == 0:
                    grid[x][y] = 2

    x = scale
    y = scale

    mn = 2000000

    for c in t:
        dire = c[0]
        magn = int(c[1:])

        if dire == 'U':
            for y in range(y-1, y-magn-1, -1):
                if grid[x][y] == 2:
                    grid[x][y] = 3
                    mn = min(mn, abs(x-scale)+abs(y-scale))
        elif dire == 'D':
            for y in range(y+1, y+magn+1):
                if grid[x][y] == 2:
                    grid[x][y] = 3
                    mn = min(mn, abs(x-scale)+abs(y-scale))
        elif dire == 'L':
            for x in range(x-1, x-magn-1, -1):
                if grid[x][y] == 2:
                    grid[x][y] = 3
                    mn = min(mn, abs(x-scale)+abs(y-scale))
        elif dire == 'R':
            for x in range(x+1, x+magn+1):
                if grid[x][y] == 2:
                    grid[x][y] = 3
                    mn = min(mn, abs(x-scale)+abs(y-scale))

    print(mn)
