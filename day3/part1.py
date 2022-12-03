# D3P1

#fname = 'example.txt'
fname = 'input1.txt'
fp = open(fname, 'r')

def priority(c):
    if ord(c) > 96:
        return ord(c) - 96
    else:
        return ord(c) - 38

total = 0

for line in fp:
    sack = line.strip()
    sackLen = len(sack)
    c1 = sack[:int((len(sack))/2)]  # Compartment 1 contents
    c2 = sack[int(len(sack)/2):]    # Compartment 2 contents
    print(f'The line {sack} is len {sackLen} and has substrings: {c1}  {c2}')
    inum = 0
    for item in c1:
        if c2.find(c1[inum]) != -1:
            print(f'Found match at position {inum} with character {c1[inum]}')
            total += priority(c1[inum])
            break
        else:
            inum += 1

print(f'Fin: total = {total}')
fp.close()
