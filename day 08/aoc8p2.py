with open('input.txt') as f:
    s = f.readline()
    size = 25*6
    image = []
    for i in range(6):
        image.append(['2']*25)
    for i in range(0, len(s), size):
        layer = s[i:i+size]
        layer_img = []
        for l in range(0, size, 25):
            layer_img.append(layer[l:l+25])
        for r in range(6):
            for c in range(25):
                if image[r][c] == '2':
                    image[r][c] = layer_img[r][c]
    for i in range(6):
        for j in range(25):
            if (image[i][j] == '1'):
                print('#', end='')
            else:
                print(' ', end='')
        print()
