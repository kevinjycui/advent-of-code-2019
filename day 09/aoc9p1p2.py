import math
import sys
with open('input.txt') as f:
    codes = [0]*50000000
    tempcode = f.readline().split(',')
    for c in range(len(tempcode)):
        codes[c] = int(tempcode[c])
    i = 0
    REL = 0
    while True:
        OM = codes[i]
        OP = abs(OM)%100
        PM = str(math.floor(abs(OM)/100))
        if OP == 99:
            break
        elif OP == 1 or OP == 2:
            while len(PM) < 3:
                PM = '0'+PM
            if PM[2] == '0':
                a = codes[codes[i+1]]
            elif PM[2] == '1':
                a = codes[i+1]
            else:
                a = codes[REL+codes[i+1]]
            if PM[1] == '0':
                b = codes[codes[i+2]]
            elif PM[1] == '1':
                b = codes[i+2]
            else:
                b = codes[REL+codes[i+2]]
            if PM[0] == '0':
                c = codes[i+3]
            else:
                c = REL+codes[i+3]
            if OP == 1:
                codes[c] = a + b
            else:
                codes[c] = a * b
            i += 4
        elif OP == 3:
            if PM[0] == '0':
                codes[codes[i+1]] = int(input())
            elif PM[0] == '2':
                codes[REL+codes[i+1]] = int(input())
            i += 2
        elif OP == 4:
            if PM[0] == '0':
                print(codes[codes[i+1]])
            elif PM[0] == '2':
                print(codes[REL+codes[i+1]])
            i += 2
        elif OP == 5 or OP == 6:
            while len(PM) < 2:
                PM = '0'+PM
            if PM[1] == '0':
                a = codes[codes[i+1]]
            elif PM[1] == '1':
                a = codes[i+1]
            else:
                a = codes[REL+codes[i+1]]
            if PM[0] == '0':
                b = codes[codes[i+2]]
            elif PM[0] == '1':
                b = codes[i+2]
            else:
                b = codes[REL+codes[i+2]]
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
            elif PM[2] == '1':
                a = codes[i+1]
            else:
                a = codes[REL+codes[i+1]]
            if PM[1] == '0':
                b = codes[codes[i+2]]
            elif PM[1] == '1':
                b = codes[i+2]
            else:
                b = codes[REL+codes[i+2]]
            if PM[0] == '0':
                c = codes[i+3]
            elif PM[0] == '2':
                c = REL+codes[i+3]
            if OP == 7:
                if a<b:
                    codes[c] = 1
                else:
                    codes[c] = 0
            if OP == 8:
                if a==b:
                    codes[c] = 1
                else:
                    codes[c] = 0
            i += 4
        elif OP == 9:
            if PM[0] == '0':
                REL += codes[codes[i+1]]
            elif PM[0] == '1':
                REL += codes[i+1]
            else:
                REL += codes[REL+codes[i+1]]
            i += 2
        else:
            print('Error')
            break            
            
