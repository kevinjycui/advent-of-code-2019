import math
import sys

codes = [0]*50000000

def intcode(i, REL, MEM, score):
    RET = []
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
            maxx = 0
            maxy = 0

            for o in range(len(RET)):
                if o%3 == 0:
                    maxx = max(maxx, RET[o]+1)
                elif o%3 == 1:
                    maxy = max(maxy, RET[o]+1)

            game = []
            for y in range(maxy):
                game.append([' ']*maxx)

            ball = 0
            board = 0

            for o in range(0, len(RET), 3):
                if RET[o+2] == 0:
                    game[RET[o+1]][RET[o]] = ' '
                elif RET[o+2] == 1:
                    game[RET[o+1]][RET[o]] = 'X'
                elif RET[o+2] == 2:
                    game[RET[o+1]][RET[o]] = '#'
                elif RET[o+2] == 3:
                    game[RET[o+1]][RET[o]] = '='
                    board = RET[o]
                else:
                    game[RET[o+1]][RET[o]] = 'O'
                    ball = RET[o]

##            for g in game:
##                for h in g:
##                    print(h, end='')
##                print()

            if ball == board:
                MEM = 0
            else:
                MEM = (ball - board) // abs(ball - board)
                
            if PM[0] == '0':
                codes[codes[i+1]] = MEM
            elif PM[0] == '2':
                codes[REL+codes[i+1]] = MEM
            i += 2
        elif OP == 4:
            if PM[0] == '0':
                RET.append(codes[codes[i+1]])
            elif PM[0] == '1':
                RET.append(codes[i+1])
            elif PM[0] == '2':
                RET.append(codes[REL+codes[i+1]])
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

    for o in range(0, len(RET), 3):
        if RET[o] == -1 and RET[o+1] == 0:
            score = RET[o+2]
    return i, REL, RET, score

with open('input.txt') as f:
    tempcode = f.readline().split(',')
    for c in range(len(tempcode)):
        codes[c] = int(tempcode[c])

    codes[0] = 2
    
    i = 0
    REL = 0
    score = 0

    i, REL, out, score = intcode(i, REL, 0, score)

    print(score)
    
        
