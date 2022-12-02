# D1P1

fname = 'input1.txt'
fp = open(fname, 'r')

total = 0
max = 0


for line in fp:
    if line.strip() == '':
        print(f'Found a terminator: total = {total}')
        if total > max:
            max = total
        total = 0
    else:
        total += int(line)

print(f'found max calories as: {max}')
fp.close()
