# D10P1

#fname = 'example2.txt'
fname = 'input1.txt'

x = 1   # CPU Register
c = 0   # clock

tadd = 2    # number of clock cycles an "add" command takes
tnop = 1    # number of clock cycles a "nop" command takes
mod = 20    # modulo thing
strsum = 0

fp = open(fname, 'r')
data = fp.read().splitlines()
print(data)

for ins in data:
    if 'noop' in ins:
        c += tnop
    elif 'addx' in ins:
        c += tadd
        x += int(ins.split(' ')[1])
    else:
        print(f'Unparseable command: {ins}')
    if c >= mod:
        print(f'At break {mod}, clock = {c}, x = {x}, last cmd = {ins}')
        # if mod - c != 0:
        if 'addx' in ins:
            adjx = x - int(ins.split(" ")[1])
            #print(f'Adjusted x = {adjx}')
            print(f'Adj Signal str = {mod * adjx}')
            strsum += mod * adjx
        else:
            print(f'Signal str = {mod * x}')
            strsum += mod * x
        mod += 40


print(strsum)


