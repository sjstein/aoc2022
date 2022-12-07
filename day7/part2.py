# D7P2

#fname = 'example.txt'
fname = 'input1.txt'

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

minsize = 70000000 - filemap['/']   # Root directory
reqspace = 30000000 - minsize
for size in filemap.values():
    if reqspace <= size < minsize:
        minsize = size

print(f'Part 2 total = {minsize}')
