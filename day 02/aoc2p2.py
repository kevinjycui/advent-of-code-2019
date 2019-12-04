for noun in range(0, 100):
    for verb in range(0, 100):
        with open('input.txt') as f:
            codes = f.readline().split(',')
            for c in range(len(codes)):
                codes[c] = int(codes[c])
            codes[1] = noun
            codes[2] = verb
            i = 0
            while True:
                if codes[i] == 99:
                    break
                elif codes[i] == 1:
                    codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
                elif codes[i] == 2:
                    codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
                i += 4
            if codes[0] == 19690720:
                print(100*noun+verb)
