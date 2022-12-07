# D7P1

fname = 'example.txt'
#fname = 'input1.txt'

fp = open(fname, 'r')
data = fp.read().splitlines()


def dir_sizes(dlist):
    dirs = {}
    path = []
    for line in dlist:
        cmd = line.split(' ')
        fsize = 0
        if not ('dir' in cmd or 'ls' in cmd):
            if 'cd' in cmd:
                if '..' in cmd:
                    path.pop()      # Moving up a directory
                else:
                    try:
                        if path[-1] == '/':
                            delim = ''
                        else:
                            delim = '/'
                        path.append(f'{path[-1]}{delim}{cmd[2]}')
                    except IndexError:
                        path.append(cmd[2])
            else:
                fsize = int(cmd[0])     # Name of file is ignored
            if fsize > 0:
                for dir in path:
                    dirs[dir] = dirs.get(dir, 0) + fsize    # Sum file sizes for directory rollup
    return dirs


filemap = dir_sizes(data)
print(filemap)
total = 0
for size in filemap.values():
    if size <= 100000:
        total += size
print(f'Part 1 total = {total}')

