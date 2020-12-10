from collections import defaultdict
from itertools import chain

# Read input
G = defaultdict(list)
R = defaultdict(dict)
for row in [line.strip().split() for line in open('07.in')]:
    a = row[0] + ' ' + row[1]
    for i in range(4, len(row), 4):
        if row[i] != 'no':
            b = row[i+1] + ' ' + row[i+2]
            G[b].append(a)
            R[a][b] = int(row[i])

# Part 1
visited = set()
def children(node):
    visited.add(node)
    return [node] + list(chain(*chain(children(n) for n in G[node] if n not in visited)))
print(len(children('shiny gold')) - 1)

# Part 2
def count(node):
    return 1 + sum(n*count(neigh) for neigh, n in R[node].items())
print(count('shiny gold') - 1)
