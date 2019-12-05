from collections import Counter

x = 125730
y = 579381

count = 0

for pswd in range(x, y+1):
    s = str(pswd)
    
    if list(s) == sorted(s) and 2 in Counter(s).values():
        count += 1

print(count)
