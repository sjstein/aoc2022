# D9P1

#fname = 'example.txt'
fname = 'input1.txt'

hx, hy = 0, 0
tx, ty = 0, 0
visited = []


def is_adj(headx, heady, tailx, taily):
    if abs(headx - tailx) <= 1 and abs(heady - taily) <= 1:
        return True
    return False


def adj_tail(headx, heady, tailx, taily):
    if headx != tailx and heady != taily:    # diagonal move
        if headx > tailx and heady > taily:     # upper right move
            return 1, 1
        elif headx > tailx and heady < taily:   # lower right move
            return 1, -1
        elif headx < tailx and heady < taily:   # lower left move
            return -1, -1
        elif headx < tailx and heady > taily:   # upper left move
            return -1, 1
    if headx != tailx:      # horizontal move
        if headx > tailx:
            return 1, 0
        else:
            return -1, 0
    else:                   # vertical move
        if heady > taily:
            return 0, 1
        else:
            return 0, -1


fp = open(fname, 'r')
data = fp.read().splitlines()
print(data)
visited.append([0, 0])

for coord in data:
    move = coord.split(' ')
    m = int(move[1])
    j = 0
    print('-----------')
    if move[0] == 'L':
        print(f'Moving LEFT {m} spaces')
        while j < m:
            j += 1
            hx -= 1
            print(f'New head position: {hx}, {hy}')
            if not is_adj(hx, hy, tx, ty):
                print('Tail not in range, adjusting')
                cx, cy = adj_tail(hx, hy, tx, ty)
                tx += cx
                ty += cy
                print(f'new tail pos: {tx}, {ty}')
                visited.append([tx, ty])
    elif move[0] == 'R':
        print(f'Moving RIGHT {m} spaces')
        while j < m:
            j += 1
            hx += 1
            print(f'New head position: {hx}, {hy}')
            if not is_adj(hx, hy, tx, ty):
                print('Tail not in range, adjusting')
                cx, cy = adj_tail(hx, hy, tx, ty)
                tx += cx
                ty += cy
                print(f'new tail pos: {tx}, {ty}')
                visited.append([tx, ty])

    elif move[0] == 'D':
        print(f'Moving DOWN {m} spaces')
        while j < m:
            j += 1
            hy -= 1
            print(f'New head position: {hx}, {hy}')
            if not is_adj(hx, hy, tx, ty):
                print('Tail not in range, adjusting')
                cx, cy = adj_tail(hx, hy, tx, ty)
                tx += cx
                ty += cy
                print(f'new tail pos: {tx}, {ty}')
                visited.append([tx, ty])

    elif move[0] == 'U':
        print(f'Moving UP {m} spaces')
        while j < m:
            j += 1
            hy += 1
            print(f'New head position: {hx}, {hy}')
            if not is_adj(hx, hy, tx, ty):
                print('Tail not in range, adjusting')
                cx, cy = adj_tail(hx, hy, tx, ty)
                tx += cx
                ty += cy
                print(f'new tail pos: {tx}, {ty}')
                visited.append([tx, ty])


print(visited)
new_set = [ x for i, x in enumerate(visited) if x not in visited[:i]]
print("No of unique items in the list are:", len(new_set))


