# D11P2

#fname = 'example.txt'
fname = 'input1.txt'

worryfactor = 1


class Monkey:

    def __init__(self, nbr, items, oper, test, true_monkey, false_monkey):
        self.number = nbr
        self.items = items
        self.operation = oper
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspections = 0

    def print_info(self):
        print(f'Monkey      # {self.number}\n'
              f'Inspections : {self.inspections}\n'
              f'items       : {self.items}\n'
              f'opr         : {self.operation}\n'
              f'test        : {self.test}\n'
              f'true monkey : {self.true_monkey}\n'
              f'false monkey: {self.false_monkey}')

    def new_item(self, inum):
        opr = self.operation.split(' ')[0]
        if self.operation.split(' ')[1] == 'old':
            if opr == '*':
                return (inum * inum) // worryfactor
            elif opr == '/':
                return (inum / inum) // worryfactor
            elif opr == '+':
                return (inum + inum) // worryfactor
            elif opr == '-':
                return (inum - inum) // worryfactor
        else:
            mag = int(self.operation.split(' ')[1])
            if opr == '*':
                return (inum * mag) // worryfactor
            elif opr == '/':
                return (inum / mag) // worryfactor
            elif opr == '+':
                return (inum + mag) // worryfactor
            elif opr == '-':
                return (inum - mag) // worryfactor

    def throw_item(self, inum):
        if inum % int(self.test) == 0:
            return self.true_monkey
        else:
            return self.false_monkey


fp = open(fname, 'r')
data = fp.read().splitlines()
monkeys = {}
lnum = 0
litems = []
loper = ''
ltest = ''
ltrue = 0
lfalse = 0

for entry in data:
    print(f'parsing : {entry}')
    if 'Monkey' in entry:
        lnum = int(entry.split(" ")[1].strip(":"))
    elif 'Starting' in entry:
        litems = entry.split(': ')[1].split(', ')
    elif 'Operation' in entry:
        loper = entry.split('new = old ')[1]
    elif 'Test' in entry:
        ltest = int(entry.split('by ')[1])
    elif 'true' in entry:
        ltrue = int(entry.split('monkey ')[1])
    elif 'false' in entry:
        lfalse = int(entry.split('monkey ')[1])
    else:
        monkeys[lnum] = Monkey(lnum, litems, loper, ltest, ltrue, lfalse)
        monkeys[lnum].print_info()

print(f'Parsed {len(monkeys)} monkeys\n------------------')

magicdiv = 1
for monkey in monkeys.values():
    magicdiv *= monkey.test

for round in range(10000):
    print(f'Round {round}\n--------------------')
    for monkey in monkeys.values():
        for item in monkey.items:
            newitem = monkey.new_item(int(item))
            print(f'Monkey {monkey.number} is throwing {newitem} to monkey : {monkey.throw_item(newitem)}')
            monkeys[monkey.throw_item(newitem)].items.append(newitem % magicdiv)
        monkey.inspections += len(monkey.items)
        print(f"Monkey {monkey.number} has done {monkey.inspections} inspections so far")
        monkey.items.clear()    # All items thrown

numinspect = []
for monkey in monkeys.values():
    print('+++++++')
    monkey.print_info()
    myinspect = int(monkey.inspections)
    numinspect.append(myinspect)

numinspect.sort(reverse=True)
print(f'Monkeybusiness value = {numinspect[0] * numinspect[1]}')
