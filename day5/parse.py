# Parse crate stacks

#fname = 'example.txt'
fname = 'input1.txt'
fp = open(fname, 'r')

spaces = 0
eof = False
numlines = 0

innerlist = []
listDict = {}
state = {}


for line in fp:
    if line.strip() == '':
        print('Found empty line - create position portion complete')
        break
    else:
        numlines += 1
        for char in line.rstrip():
            if char == '1':
                eof = True
                break
            if char == ' ':
                # count number of spaces
                spaces += 1
            if char != '[' and char != ']' and char != ' ':
                while spaces >= 4:
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

print(f'{listDict}\n==============================')
localList = []
for x in range(numlines):
    for y in range(1,numlines):
        if listDict[y][x] != ' ':
            print(f'{listDict[y][x]}')
            localList.append(listDict[y][x])
    state[x+1] = localList.copy()
    localList.clear()
    print('--')

#print(f'new dict = {state}')
#print(f'len = {len(state)}')
fp.close()


