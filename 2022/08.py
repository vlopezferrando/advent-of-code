#
# Check how I live coded this: https://youtu.be/fTNdCiz3NKk
#

from math import prod

# Read input
grid = open("08.in").read().splitlines()
N = len(grid)

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def trees_in_direction(i, j, d):
    i, j = i + d[0], j + d[1]
    while 0 <= i < N and 0 <= j < N:
        yield grid[i][j]
        i, j = i + d[0], j + d[1]


def visible_from_direction(i, j, d):
    """Tree in position (i, j) is taller than all other trees in direction d"""
    return all(grid[i][j] > t for t in trees_in_direction(i, j, d))


def visible_from_outside(i, j):
    """Tree in position (i, j) is visible from some of the 4 directions"""
    return any(visible_from_direction(i, j, d) for d in DIRS)


def viewing_distance(i, j, d):
    ret = 0
    for tree in trees_in_direction(i, j, d):
        ret += 1
        if tree >= grid[i][j]:
            break
    return ret


def scenic_score(i, j):
    return prod([viewing_distance(i, j, d) for d in DIRS])


# Part 1
p1 = sum(visible_from_outside(i, j) for i in range(N) for j in range(N))
assert p1 == 1690

# Part 2
p2 = max(scenic_score(i, j) for i in range(N) for j in range(N))
assert p2 == 535680

"""
Lessons learned
1. itertools: takewhile, product, repeat, combination
2. math.prod
3. any(), all()     . max(), range()
4. List comprehensions
5. List of DIRS (increments) to move around the grid
6. yield: create a generator
7. Compare three values in a single expression: 0 < 3 < 4
8. Create small functions with clear names as a way to better explain the code
"""
