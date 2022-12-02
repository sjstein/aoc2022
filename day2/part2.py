# D2P2

fname = 'input1.txt'
fp = open(fname, 'r')
# Input format:
#  A = Rock (1 point)
#  B = Paper (2 points)
#  C = Scissors (3 points)
# Response format:
#  X = lose, Y = draw, Z = win
# Scoring:
#  Lose : 0, Draw : 3, Win : 6
# Win matrix:
#  A B
#  B C
#  C A
# Lose matrix:
#  A C
#  B A
#  C B

a = 1
b = 2
c = 3
lose = 0
draw = 3
win = 6

total = 0

for line in fp:
    t, u = line.strip().split(' ')  # (t)hem, (u)s
    print(f'Them={t}, Us={u}')
    if t == "A" and u == "X":   # Lose
        total += c+lose
    if t == 'A' and u == 'Y':   # Draw
        total += a+draw
    if t == 'A' and u == 'Z':   # Win
        total += b+win
    if t == 'B' and u == 'X':
        total += a+lose
    if t == 'B' and u == 'Y':
        total += b+draw
    if t == 'B' and u == 'Z':
        total += c+win
    if t == 'C' and u == 'X':
        total += b+lose
    if t == 'C' and u == 'Y':
        total += c+draw
    if t == 'C' and u == 'Z':
        total += a+win
fp.close()
print(f'Total: {total}')
