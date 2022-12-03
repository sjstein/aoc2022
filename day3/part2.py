# D3P2

#fname = 'example.txt'
fname = 'input1.txt'
fp = open(fname, 'r')

def priority(c):
    if ord(c) > 96:
        return ord(c) - 96
    else:
        return ord(c) - 38


total = 0
line = fp.readlines()
flen = len(line)
print(f'length = {flen}')
lnum = 0
cnum = 0

while lnum < flen:
    for char in line[lnum]:
        if line[lnum+1].find(line[lnum][cnum]) != -1 and line[lnum+2].find(line[lnum][cnum]) != -1:
            # Found a match
            print(f'Found a match at {cnum} with character {line[lnum][cnum]}')
            total += priority(line[lnum][cnum])
            cnum = 0
            break
        else:
            cnum += 1

    lnum += 3

print(f'Fin: total = {total}')
fp.close()
