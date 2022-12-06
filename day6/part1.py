# D5P1

#fname = 'example.txt'
fname = 'input1.txt'


def find_duplicate(substr):
    # print(f'substr: {substr}')
    for c in substr:
        if substr.count(c) > 1:
            # print(f'found dup char: {c}')
            return substr.rfind(c)
    return 0


clen = 4   # number of chars to process
cpos = 0   # char position

fp = open(fname, 'r')
data = fp.readlines()
fp.close()

while find_duplicate(data[0][cpos:cpos+clen]) > 0:
    cpos += 1

print(cpos+clen)




