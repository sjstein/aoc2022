# D4P2

#fname = 'example.txt'
fname = 'input1.txt'

# PARSE file header for crate positions and populate dictionary
fp = open(fname, 'r')
spaces = 0
eof = False
numlines = 0
innerlist = []
listDict = {}
state = {}

for line in fp:
    numlines += 1
    for char in line.rstrip():
        if char == '1':     # Indicates end of header / crate position info
            eof = True
            break
        if char == ' ':
            # count number of spaces
            spaces += 1
        if char != '[' and char != ']' and char != ' ':
            while spaces >= 4:  # Account for spaces inbetween crate stacks
                innerlist.append(' ')
                spaces -= 4
            innerlist.append(char)
            spaces = 0
    if eof:
        break
    listDict[numlines] = innerlist.copy()
    innerlist.clear()
    spaces = 0

print(f'parsed {numlines-1} lines')
# So now there is a dictionary with keys representing rows and a list of the entries on that row
# Need to transpose to state dictionary showing the crates in their proper columns

localList = []
for x in range(numlines):
    for y in range(1, numlines):
        if listDict[y][x] != ' ':
            localList.append(listDict[y][x])
    state[x+1] = localList.copy()
    localList.clear()
print(f'State dictionary created.\n---------------\nStarting crane ops')

fp.readline()   # flush empty line
for line in fp:
    qty = int(line.split(" ")[1])
    fstack = int(line.split(" ")[3])
    tstack = int(line.split(" ")[5])
    rstack = state[fstack][:qty]
    state[tstack][:0] = rstack
    del state[fstack][:qty]

endposition = ''
i = 1
for j in state.items():
    endposition += state[i][0]
    i += 1

fp.close()

print(f'End state : {endposition}')
