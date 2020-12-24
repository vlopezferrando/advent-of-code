from collections import defaultdict


def coord(x, y, s):
    if s == 'e':
        return x + 1, y
    if s == 'w':
        return x - 1, y
    if s == 'ne':
        return x + y % 2, y + 1
    if s == 'se':
        return x + y % 2, y - 1
    if s == 'nw':
        return x - (y + 1) % 2, y + 1
    if s == 'sw':
        return x - (y + 1) % 2, y - 1


def coords(x, y, s):
    while s:
        if s[0] in 'ew':
            x, y = coord(x, y, s[0])
            s = s[1:]
        else:
            x, y = coord(x, y, s[:2])
            s = s[2:]
    return x, y


def neigh(x, y):
    for d in ['e', 'se', 'sw', 'w', 'nw', 'ne']:
        yield coord(x, y, d)


def next(b):
    nn = defaultdict(int)
    for c in b:
        for nc in neigh(*c):
            nn[nc] += 1
    return set([c for c, n in nn.items() if (c in b and n == 1) or n == 2])


# Part 1
d = defaultdict(bool)
for line in open('24.in'):
    c = coords(0, 0, line.strip())
    d[c] = not d[c]
print(sum(d.values()))

# Part 2
b = set([k for k, v in d.items() if v])
for _ in range(100):
    b = next(b)
print(len(b))
