from collections import Counter

x = 125730
y = 579381

count = 0

for pswd in range(x, y+1):
    s = str(pswd)

    valid = False
    for c in Counter(s).values():
        if c > 1:
            valid = True
    
    if list(s) == sorted(s) and valid:
        count += 1

print(count)
