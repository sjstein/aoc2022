# D2P1

fname = 'input1.txt'
fp = open(fname, 'r')
# Input format:
#  A = Rock
#  B = Paper
#  C = Scissors
# Response format:
#  X = Rock (1)
#  Y = Paper (2)
#  Z = Scissors (3)
# Scoring:
#  Lose : 0, Draw : 3, Win : 6
#  A X = 4 [d]; B X = 1 [l]; C X [w] = 7
#  A Y = 8 [w]; B Y = 5 [d]; C Y [l] = 2
#  A Z = 3 [l]; B Z = 9 [w]; C Z [d] = 6

total = 0

for line in fp:
    t, u = line.strip().split(' ')  # (t)hem, (u)s
    print(f'Them={t}, Us={u}')
    if t == "A" and u == "X":
        total += 4
    if t == 'A' and u == 'Y':
        total += 8
    if t == 'A' and u == 'Z':
        total += 3
    if t == 'B' and u == 'X':
        total += 1
    if t == 'B' and u == 'Y':
        total += 5
    if t == 'B' and u == 'Z':
        total += 9
    if t == 'C' and u == 'X':
        total += 7
    if t == 'C' and u == 'Y':
        total += 2
    if t == 'C' and u == 'Z':
        total += 6
fp.close()
print(f'Total: {total}')
