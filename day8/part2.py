# D8P2

#fname = 'example.txt'
fname = 'input1.txt'


def print_grid(grid):
    for a in range(0, len(grid)):
        for b in range(0, len(grid[0])):
            print(f'{grid[a][b]}', end='')
        print()


def print_left(grid, x, y):
    for a in range(y, -1, -1):
        print(f'{grid[x][a]}', end='')
    print(f'\n')


def print_right(grid, x, y):
    for a in range(y, len(grid[0])):
        print(f'{grid[x][a]}', end='')
    print()


def print_up(grid, x, y):
    for a in range(x, -1, -1):
        print(f'{grid[a][y]}', end='')
    print()


def print_down(grid, x, y):
    for a in range(x, len(grid)):
        print(f'{grid[a][y]}', end='')
    print()


def print_all(grid, x, y):
    print_up(grid, x, y)
    print_down(grid, x, y)
    print_left(grid, x, y)
    print_right(grid, x, y)


def check_left(grid, x, y):
    dist = 0
    for a in range(y - 1, -1, -1):
        dist += 1
        if grid[x][y] <= grid[x][a]:
            return dist
    return dist


def check_right(grid, x, y):
    dist = 0
    for a in range(y + 1, len(grid[0])):
        dist += 1
        if grid[x][y] <= grid[x][a]:
            return dist
    return dist


def check_up(grid, x, y):
    dist = 0
    for a in range(x - 1, -1, -1):
        dist += 1
        if grid[x][y] <= grid[a][y]:
            return dist
    return dist


def check_down(grid, x, y):
    dist = 0
    for a in range(x + 1, len(grid)):
        dist += 1
        if grid[x][y] <= grid[a][y]:
            return dist
    return dist


def check_los(grid, x, y):
    return check_left(grid, x, y) * check_right(grid, x, y) * check_up(grid, x, y) * check_down(grid, x, y)


fp = open(fname, 'r')
data = fp.read().splitlines()
width = len(data[0])
height = len(data)

print(f'grid is {height} tall by {width} wide')
print_grid(data)
print('')

maxscore = 0
for i in range(1, width - 1):
    for j in range(1, height - 1):
        if check_los(data, i, j) > maxscore:
            maxscore = check_los(data, i, j)
        print(f'tree at ({i},{j}) [{data[i][j]}] has scenic score: {check_los(data, i, j)}')

print(f'result = {maxscore}')
