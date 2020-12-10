# Read input
groups = [[]]
for line in open('06.in').read().splitlines():
    if line == '':
        groups.append([])
    else:
        groups[-1].append(line)

# Part 1
print(sum(len(set(''.join(g))) for g in groups))

# Part 2
print(sum(sum(all(letter in g for g in group) for letter in group[0]) for group in groups))
