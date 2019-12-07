import math
from collections import Counter

def ampCalc(seq):
    MEM = 0
    EXIT = False
    AMPMEM = [codes.copy(), codes.copy(), codes.copy(), codes.copy(), codes.copy()]
    IMEM = [0, 0, 0, 0, 0]
    loop = 0
    while not EXIT:
        for amp in range(5):
            phase = False
            pause = False
            while not pause:
                OM = AMPMEM[amp][IMEM[amp]]
                OP = abs(OM)%100
                if OP == 99:
                    EXIT = True
                    break
                elif OP == 1 or OP == 2:
                    PM = str(math.floor(abs(OM)/100))
                    while len(PM) < 3:
                        PM = '0'+PM
                    if PM[2] == '0':
                        a = AMPMEM[amp][AMPMEM[amp][IMEM[amp]+1]]
                    else:
                        a = AMPMEM[amp][IMEM[amp]+1]
                    if PM[1] == '0':
                        b = AMPMEM[amp][AMPMEM[amp][IMEM[amp]+2]]
                    else:
                        b = AMPMEM[amp][IMEM[amp]+2]
                    if OP == 1:
                        AMPMEM[amp][AMPMEM[amp][IMEM[amp]+3]] = a + b
                    else:
                        AMPMEM[amp][AMPMEM[amp][IMEM[amp]+3]] = a * b
                    IMEM[amp] += 4
                elif OP == 3:
                    if phase or loop>0:
                        AMPMEM[amp][AMPMEM[amp][IMEM[amp]+1]] = MEM
                    else:
                        AMPMEM[amp][AMPMEM[amp][IMEM[amp]+1]] = seq[amp]
                        phase = True
                    IMEM[amp] += 2
                elif OP == 4:
                    MEM = AMPMEM[amp][AMPMEM[amp][IMEM[amp]+1]]
                    IMEM[amp] += 2
                    pause = True
                elif OP == 5 or OP == 6:
                    PM = str(math.floor(abs(OM)/100))
                    while len(PM) < 2:
                        PM = '0'+PM
                    if PM[1] == '0':
                        a = AMPMEM[amp][AMPMEM[amp][IMEM[amp]+1]]
                    else:
                        a = AMPMEM[amp][IMEM[amp]+1]
                    if PM[0] == '0':
                        b = AMPMEM[amp][AMPMEM[amp][IMEM[amp]+2]]
                    else:
                        b = AMPMEM[amp][IMEM[amp]+2]
                    if OP == 5 and a != 0:
                        IMEM[amp] = b
                    elif OP == 6 and a == 0:
                        IMEM[amp] = b
                    else:
                        IMEM[amp] += 3
                elif OP == 7 or OP == 8:
                    PM = str(math.floor(abs(OM)/100))
                    while len(PM) < 3:
                        PM = '0'+PM
                    if PM[2] == '0':
                        a = AMPMEM[amp][AMPMEM[amp][IMEM[amp]+1]]
                    else:
                        a = AMPMEM[amp][IMEM[amp]+1]
                    if PM[1] == '0':
                        b = AMPMEM[amp][AMPMEM[amp][IMEM[amp]+2]]
                    else:
                        b = AMPMEM[amp][IMEM[amp]+2]
                    if OP == 7:
                        if a<b:
                            AMPMEM[amp][AMPMEM[amp][IMEM[amp]+3]] = 1
                        else:
                            AMPMEM[amp][AMPMEM[amp][IMEM[amp]+3]] = 0
                    if OP == 8:
                        if a==b:
                            AMPMEM[amp][AMPMEM[amp][IMEM[amp]+3]] = 1
                        else:
                            AMPMEM[amp][AMPMEM[amp][IMEM[amp]+3]] = 0
                    IMEM[amp] += 4
                else:
                    print('Error')
                    break
        loop += 1    
    return MEM
            

with open('input.txt') as f:
    codes = f.readline().split(',')
    for c in range(len(codes)):
        codes[c] = int(codes[c])

    MAX = 0

    for a in range(5, 10):
        for b in range(5, 10):
            for c in range(5, 10):
                for d in range(5, 10):
                    for e in range(5, 10):
                        seq = [a, b, c, d, e]
                        if list(Counter(seq).values()) == [1, 1, 1, 1, 1]:
                            MAX = max(MAX, ampCalc(seq))

    print(MAX)
