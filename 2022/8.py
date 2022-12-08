from math import prod

# Read input
grid = open("8.in").read().splitlines()
N = len(grid)

INCS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def trees_in_dir(i, j, inc):
    ni, nj = i + inc[0], j + inc[1]
    while ni >= 0 and ni < N and nj >= 0 and nj < N:
        yield grid[ni][nj]
        ni, nj = ni + inc[0], nj + inc[1]


def viewing_distance(i, j, inc):
    ret = 0
    for tree in trees_in_dir(i, j, inc):
        ret += 1
        if tree >= grid[i][j]:
            break
    return ret


# Part 1
p1 = sum(
    any(all(tree < grid[i][j] for tree in trees_in_dir(i, j, inc)) for inc in INCS)
    for i in range(N)
    for j in range(N)
)
assert p1 == 1690

# Part 2
p2 = max(
    prod([viewing_distance(i, j, inc) for inc in INCS])
    for i in range(N)
    for j in range(N)
)
assert p2 == 535680

"""
Lessons learned
1. itertools: takewhile, product, repeat, combination
2. math.prod
3. any(), all()     . max(), range()
4. List comprehensions
5. List of INCS (increments) to move around the grid
6. yield: create a generator
"""
