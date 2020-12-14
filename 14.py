from itertools import product
import re

# Input regular expressions
remem = re.compile(r'mem\[(\d+)\] = (\d+)')
lines = open('14.in').read().splitlines()

# Part 1
mem = {}
for line in lines:
    if line.startswith('mask'):
        mask = line.split()[-1]
        ones = int(mask.replace('X', '0'), 2)
        zeros = int(mask.replace('X', '1'), 2)
    else:
        i, n = remem.match(line).groups()
        mem[int(i)] = (int(n) & zeros) | ones
print(sum(mem.values()))

# Part 2
def expand(mask):
    for n in product(['0', '1'], repeat=mask.count('X')):
        zeros = mask.replace('0', '1')
        ones = mask
        for c in n:
            zeros = zeros.replace('X', c, 1)
            ones = ones.replace('X', c, 1)
        yield zeros, ones

mem = {}
for line in lines:
    if line.startswith('mask'):
        mask = line.split()[-1]
    else:
        i, n = remem.match(line).groups()
        for zeros, ones in expand(mask):
            mem[(int(i) & int(zeros, 2)) | int(ones, 2)] = int(n)
print(sum(mem.values()))
