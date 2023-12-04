import re

G = open("03.in").read().splitlines()

numbers = [
    ((i, m.span()), int(m.group()))
    for i, line in enumerate(G)
    for m in re.finditer(r"(\d+)", line)
]


def neighbours(i, j):
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if 0 <= i + di < len(G) and 0 <= j + dj < len(G[0]):
                yield G[i + di][j + dj], (i + di, j + dj)


def symbol_around(i, j):
    return any(not c.isdigit() and c != "." for c, _ in neighbours(i, j))


# Part 1
sol_1 = sum(n for (i, js), n in numbers if any(symbol_around(i, j) for j in range(*js)))
assert sol_1 == 539637

# Part 2
number_in = {(i, j): number for (i, js), number in numbers for j in range(*js)}
asterisks = [(i, j) for i, line in enumerate(G) for j, c in enumerate(line) if c == "*"]
sol_2 = 0
for i, j in asterisks:
    numbers_around = list(
        set(number_in[pos] for _, pos in neighbours(i, j) if pos in number_in)
    )
    if len(numbers_around) == 2:
        sol_2 += numbers_around[0] * numbers_around[1]
assert sol_2 == 82818007