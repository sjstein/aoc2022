# D4P2

#fname = 'example.txt'
fname = 'input1.txt'
fp = open(fname, 'r')

# SUPER CHEESECHEAT SHIT - write a friggin parser!
stack1 = ['F', 'L', 'M', 'W']
stack2 = ['F', 'M', 'V', 'Z', 'B']
stack3 = ['Q', 'L', 'S', 'R', 'V', 'H']
stack4 = ['J', 'T', 'M', 'P', 'Q', 'V', 'S', 'F']
stack5 = ['W', 'S', 'L']
stack6 = ['W', 'J', 'R', 'M', 'P', 'V', 'F']
stack7 = ['F', 'R', 'N', 'P', 'C', 'Q', 'J']
stack8 = ['B', 'R', 'W', 'Z', 'S', 'P', 'H', 'V']
stack9 = ['W', 'Z', 'H', 'G', 'C', 'J', 'M', 'B']

data = fp.read().splitlines()[10:]  # Jump past the crate positional info. More cheese?

state = {1: stack1, 2: stack2, 3: stack3, 4: stack4, 5: stack5, 6: stack6, 7: stack7, 8: stack8, 9: stack9}

for line in data:
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


