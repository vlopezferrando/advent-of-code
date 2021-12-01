from collections import defaultdict


def rotate(r):
    """Rotate a square 90 degrees"""
    nr = [[""] * len(r) for _ in r]
    for i, row in enumerate(r):
        for j, c in enumerate(row):
            nr[j][len(r) - 1 - i] = c
    return ["".join(row) for row in nr]


def flip(r):
    """Horizontally flip square"""
    return ["".join(reversed(row)) for row in r]


def col(r, i):
    """Get ith column of square as a string"""
    return "".join(row[i] for row in r)


# Read input
lines = open("20.in").read().splitlines()

# Read squares and save as list of all possible rotations
rects = defaultdict(list)
for i in range(144):
    n = int(lines[i * 12][5:9])
    r = lines[i * 12 + 1 : i * 12 + 11]
    rects[n].append(r)
    rects[n].append(rotate(r))
    rects[n].append(rotate(rotate(r)))
    rects[n].append(rotate(rotate(rotate(r))))
    rects[n].append(flip(r))
    rects[n].append(rotate(flip(r)))
    rects[n].append(rotate(rotate(flip(r))))
    rects[n].append(rotate(rotate(rotate(flip(r)))))

# Index first columns and rows
first_col = defaultdict(list)
first_row = defaultdict(list)
for n, rs in rects.items():
    for i, r in enumerate(rs):
        first_row[r[0]].append((n, i))
        first_col[col(r, 0)].append((n, i))

# Part 1
n_times_alone = defaultdict(int)
for _, l in first_col.items():
    if len(l) == 1:
        n_times_alone[l[0][0]] += 1
sol = 1
for k, v in n_times_alone.items():
    if v == 4:
        sol *= k
print(sol)

# Part 2
board = [[(0, 0)] * 12 for _ in range(12)]
board[0][0] = (2693, 2)

# Fill 1st row
for j in range(1, 12):
    prev_n, prev_o = board[0][j - 1]
    prev_last_col = col(rects[prev_n][prev_o], -1)
    for n, o in first_col[prev_last_col]:
        if n != prev_n:
            board[0][j] = (n, o)
            break

# Fill rest of the board
for i in range(1, 12):
    for j in range(12):
        prev_n, prev_o = board[i - 1][j]
        prev_last_row = rects[prev_n][prev_o][-1]
        for n, o in first_row[prev_last_row]:
            if n != prev_n:
                board[i][j] = (n, o)
                break

# Create final board
v = []
for row in board:
    nrows = [""] * 8
    for n, o in row:
        for i, rrow in enumerate(rects[n][o][1:-1]):
            nrows[i] += rrow[1:-1]
    v += nrows

# Count appearances of the monster
def fill_monster(r):
    monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
    for i in range(len(r) - len(monster)):
        for j in range(len(r[0]) - len(monster[0])):
            valid = True
            for mi, mrow in enumerate(monster):
                for mj, mc in enumerate(mrow):
                    if mc == "#" and r[i + mi][j + mj] == ".":
                        valid = False
            if valid:
                for mi, mrow in enumerate(monster):
                    for mj, mc in enumerate(mrow):
                        if mc == "#":
                            l = list(r[i + mi])
                            l[j + mj] = "O"
                            r[i + mi] = "".join(l)
    return r


# Try to fill the monster in all possible rotations
v = fill_monster(v)
v = fill_monster(rotate(v))
v = fill_monster(rotate(rotate(v)))
v = fill_monster(rotate(rotate(rotate(v))))
v = fill_monster(flip(v))
v = fill_monster(rotate(flip(v)))
v = fill_monster(rotate(rotate(flip(v))))
v = fill_monster(rotate(rotate(rotate(flip(v)))))

# Part 2
print(sum(l.count("#") for l in v))
