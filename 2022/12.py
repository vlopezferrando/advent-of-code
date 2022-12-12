# Read the grid and save as a dict
grid = {i + j * 1j: c for i, l in enumerate(open("12.in")) for j, c in enumerate(l)}

# Find start and end positions, and replace with "a", "z"
S = {v: k for k, v in grid.items()}["S"]
E = {v: k for k, v in grid.items()}["E"]
grid[S], grid[E] = "a", "z"

# Create graph
NEIGHBOURS = {
    pos: [
        pos + d
        for d in [1, -1, 1j, -1j]
        if pos + d in grid and ord(grid[pos + d]) - ord(grid[pos]) <= 1
    ]
    for pos in grid
}


# Breath First Search until we find the end position
def bfs(start, end):
    steps = {pos: 0 for pos in start}
    Q1, Q2 = start, []
    while len(Q1) > 0:
        if end in steps:
            return steps[end]
        for pos in Q1:
            for neigh in NEIGHBOURS[pos]:
                if neigh not in steps:
                    steps[neigh] = steps[pos] + 1
                    Q2.append(neigh)
        Q1, Q2 = Q2, []
    return -1


# Part 1
p1 = bfs([S], E)
assert p1 == 394

# Part 2
p2 = bfs([k for k, v in grid.items() if v == "a"], E)
assert p2 == 388


"""
Lessons learned
1. BFS algorithm. Q1, Q2
2. Used complex numbers to represent coordinates in a grid
3. ord() to get the ascii code of a character
4. Generated a graph
5. Transtaled the grid to a dictionary to simplify the code
"""
