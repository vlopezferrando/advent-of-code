# Part 1
lines = [l.strip() for l in open('input')]

sol = 0
for i, line in enumerate(lines):
    if line[(3*i) % len(line)] == '#':
        sol += 1
print(sol)

# Part 2
sols = []
for (si, sj) in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    i = j = sol = 0
    while i < len(lines):
        if lines[i][j % len(lines[i])] == '#':
            sol += 1
        i += si
        j += sj
    sols.append(sol)
from functools import reduce
print(reduce((lambda x, y: x * y), sols))
