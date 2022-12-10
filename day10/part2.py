# D10P2

#fname = 'example2.txt'
fname = 'input1.txt'

x = 1  # CPU Register
cc = 0  # clock cycle
ec = 0  # execution cycle

mod = 40  # modulo thing


def raster(clock, sprite):
    print('#', end='') if sprite - 1 <= clock <= sprite + 1 else print(' ', end='')


fp = open(fname, 'r')
data = fp.read().splitlines()

print('0123456789012345678901234567890123456789')
for ins in data:
    if cc >= mod:
        if cc > mod:
            cc -= 1
        print('')
        mod += 40
        ec = 0
    if 'noop' in ins:
        raster(ec, x)
        cc += 1
        ec += 1
    elif 'addx' in ins:
        raster(ec, x)
        cc += 1
        ec += 1
        if cc >= mod:
            if cc > mod:
                cc -= 1
            print('')
            mod += 40
            ec = 0
        raster(ec, x)
        cc += 1
        ec += 1
        x += int(ins.split(' ')[1])
    else:
        print(f'Unparseable command: {ins}')

