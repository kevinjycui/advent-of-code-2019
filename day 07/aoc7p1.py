import math
from collections import Counter

def ampCalc(seq):
    MEM = 0
    for amp in range(5):
        i = 0
        phase = False
        while True:
            OM = codes[i]
            OP = abs(OM)%100
            if OP == 99:
                break
            elif OP == 1 or OP == 2:
                PM = str(math.floor(abs(OM)/100))
                while len(PM) < 3:
                    PM = '0'+PM
                if PM[2] == '0':
                    a = codes[codes[i+1]]
                else:
                    a = codes[i+1]
                if PM[1] == '0':
                    b = codes[codes[i+2]]
                else:
                    b = codes[i+2]
                if OP == 1:
                    codes[codes[i+3]] = a + b
                else:
                    codes[codes[i+3]] = a * b
                i += 4
            elif OP == 3:
                if phase:
                    codes[codes[i+1]] = MEM
                else:
                    codes[codes[i+1]] = seq[amp]
                    phase = True
                i += 2
            elif OP == 4:
                MEM = codes[codes[i+1]]
                i += 2
            elif OP == 5 or OP == 6:
                PM = str(math.floor(abs(OM)/100))
                while len(PM) < 2:
                    PM = '0'+PM
                if PM[1] == '0':
                    a = codes[codes[i+1]]
                else:
                    a = codes[i+1]
                if PM[0] == '0':
                    b = codes[codes[i+2]]
                else:
                    b = codes[i+2]
                if OP == 5 and a != 0:
                    i = b
                elif OP == 6 and a == 0:
                    i = b
                else:
                    i += 3
            elif OP == 7 or OP == 8:
                PM = str(math.floor(abs(OM)/100))
                while len(PM) < 3:
                    PM = '0'+PM
                if PM[2] == '0':
                    a = codes[codes[i+1]]
                else:
                    a = codes[i+1]
                if PM[1] == '0':
                    b = codes[codes[i+2]]
                else:
                    b = codes[i+2]
                if OP == 7:
                    if a<b:
                        codes[codes[i+3]] = 1
                    else:
                        codes[codes[i+3]] = 0
                if OP == 8:
                    if a==b:
                        codes[codes[i+3]] = 1
                    else:
                        codes[codes[i+3]] = 0
                i += 4
            else:
                print('Error')
                break
    return MEM
            

with open('input.txt') as f:
    codes = f.readline().split(',')
    for c in range(len(codes)):
        codes[c] = int(codes[c])

    MAX = 0

    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        seq = [a, b, c, d, e]
                        if list(Counter(seq).values()) == [1, 1, 1, 1, 1]:
                            MAX = max(MAX, ampCalc(seq))

    print(MAX)
