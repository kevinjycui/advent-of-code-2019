with open('input.txt') as f:
    codes = f.readline().split(',')
    for c in range(len(codes)):
        codes[c] = int(codes[c])
    codes[1] = 12
    codes[2] = 2
    i = 0
    while True:
        if codes[i] == 99:
            break
        elif codes[i] == 1:
            codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
        elif codes[i] == 2:
            codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
        i += 4
    print(codes[0])
