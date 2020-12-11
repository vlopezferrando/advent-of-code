import copy

# Read input
board = [list(line.strip()) for line in open('11.in')]

d_i = [-1, -1, -1, 0, 1, 1, 1, 0]
d_j = [-1, 0, 1, 1, 1, 0, -1, -1]

def next(v, max_neigh, count_neigh):
    nv = copy.deepcopy(v)
    for i, row in enumerate(v):
        for j, seat in enumerate(row):
            neigh = count_neigh(v, i, j)
            if seat == 'L' and neigh == 0:
                nv[i][j] = '#'
            elif seat == '#' and neigh >= max_neigh:
                nv[i][j] = 'L'
    return nv

def next_until_equal(v, max_neigh, count_neigh):
    while True:
        prev = str(v)
        v = next(v, max_neigh, count_neigh)
        if str(v) == prev:
            return v

# Part 1
def adjacent_neighbours(v, i, j):
    return sum(v[i+Ai][j+Aj] == '#'
               for Ai, Aj in zip(d_i, d_j)
               if i+Ai >= 0 and i+Ai < len(v) and j+Aj >= 0 and j+Aj < len(v[0]))
print(sum(row.count('#') for row in next_until_equal(board, 4, adjacent_neighbours)))

# Part 2
def far_neighbours(v, i, j):
    n = 0
    for Ai, Aj in zip(d_i, d_j):
        ni = i + Ai
        nj = j + Aj
        while ni >= 0 and ni < len(v) and nj >= 0 and nj < len(v[0]):
            if v[ni][nj] == '#':
                n += 1
                break
            elif v[ni][nj] == 'L':
                break
            ni += Ai
            nj += Aj
    return n
print(sum(row.count('#') for row in next_until_equal(board, 5, far_neighbours)))
