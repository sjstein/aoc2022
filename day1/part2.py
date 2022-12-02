# D1P2

fname = 'input1.txt'
fp = open(fname, 'r')

total = 0
sums = []
threesum = 0


for line in fp:
    if line.strip() == '':
        print(f'Found a terminator: total = {total}')
        sums.append(total)
        total = 0
    else:
        total += int(line)

sums.sort(reverse=True)
threesum += sums[0]
threesum += sums[1]
threesum += sums[2]
print(f'Sorted list of sums: {sums}')
print(f'Sum of highest three elf calories: {threesum}')
fp.close()
