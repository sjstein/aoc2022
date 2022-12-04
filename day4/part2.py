# D4P2

#fname = 'example.txt'
fname = 'input1.txt'
fp = open(fname, 'r')

list1 = []
list2 = []
total = 0
iter = 1

for line in fp:
    e1, e2 = line.strip().split(',')
    n11, n12 = e1.split('-')
    n21, n22 = e2.split('-')
    # print(f'e1: {e1}; n11: {n11}; n12: {n12} | e2: {e2} n11: {n21}; n12: {n22} ')
    # create list 1
    print(f'Parsing line {iter}\n---------------')
    i = int(n11)
    while i <= int(n12):
        list1.append(i)
        i += 1
    print(f'List 1 = {list1}')
    # create list 2
    i = int(n21)
    while i <= int(n22):
        list2.append(i)
        i += 1
    print(f'List 2 = {list2}')
    if any(item in list1 for item in list2):
        print(f'We have a subset match 1 : {list2} is in {list1}')
        total += 1
    elif any(item in list2 for item in list1):
        print(f'We have a subset match 2 : {list1} is in {list2}')
        total += 1
    list1.clear()
    list2.clear()


print(f'Fin: total = {total}')
fp.close()
