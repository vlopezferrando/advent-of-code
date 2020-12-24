import itertools

N = 20
M = 13

# Part 1
b = [[["." for _ in range(N)] for _ in range(N)] for _ in range(N)]
for i, line in enumerate(open("17.in").read().splitlines()):
    for j, c in enumerate(line):
        b[6 + i][6 + j][M // 2] = c


def neigh(i, j, k):
    return sum(
        b[i + di][j + dj][k + dk] == "#"
        for di, dj, dk in itertools.product([-1, 0, 1], repeat=3)
        if (di != 0 or dj != 0 or dk != 0)
        and i + di >= 0
        and j + dj >= 0
        and k + dk >= 0
        and i + di < N
        and j + dj < N
        and k + dk < M
    )


for _ in range(6):
    n = [[[0] * N for _ in range(N)] for _ in range(N)]
    for i, j in itertools.product(range(N), repeat=2):
        for k in range(M):
            n[i][j][k] = neigh(i, j, k)
    for i, j in itertools.product(range(N), repeat=2):
        for k in range(M):
            if b[i][j][k] == "#" and n[i][j][k] != 2 and n[i][j][k] != 3:
                b[i][j][k] = "."
            if b[i][j][k] == "." and n[i][j][k] == 3:
                b[i][j][k] = "#"

print(sum(b[i][j][k] == "#" for i, j, k in itertools.product(range(N), repeat=3)))

# Part 2
b = [[[["." for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]

for i, line in enumerate(open("17.in").read().splitlines()):
    for j, c in enumerate(line):
        b[6 + i][6 + j][M // 2][M // 2] = c


def neigh(i, j, k, l):
    return sum(
        b[i + di][j + dj][k + dk][l + dl] == "#"
        for di, dj, dk, dl in itertools.product([-1, 0, 1], repeat=4)
        if (di != 0 or dj != 0 or dk != 0 or dl != 0)
        and i + di >= 0
        and j + dj >= 0
        and k + dk >= 0
        and l + dl >= 0
        and i + di < N
        and j + dj < N
        and k + dk < M
        and l + dl < M
    )


for _ in range(6):
    n = [[[[0] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for i, j in itertools.product(range(N), repeat=2):
        for k, l in itertools.product(range(M), repeat=2):
            n[i][j][k][l] = neigh(i, j, k, l)
    for i, j in itertools.product(range(N), repeat=2):
        for k, l in itertools.product(range(M), repeat=2):
            if b[i][j][k][l] == "#" and n[i][j][k][l] != 2 and n[i][j][k][l] != 3:
                b[i][j][k][l] = "."
            if b[i][j][k][l] == "." and n[i][j][k][l] == 3:
                b[i][j][k][l] = "#"

print(sum(b[i][j][k][l] == "#" for i, j, k, l in itertools.product(range(N), repeat=4)))
