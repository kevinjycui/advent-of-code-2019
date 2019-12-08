with open('input.txt') as f:
    s = f.readline()
    size = 25*6
    MIN = 2**31
    PSWD = 0
    for i in range(0, len(s), size):
        layer = s[i:i+size]
        if len(layer) == size and layer.count('0') < MIN:
            MIN = layer.count('0')
            PSWD = layer.count('1') * layer.count('2')
    print(PSWD)
