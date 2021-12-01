# Read input
lines = open("03.in").read().splitlines()

# Part 1
print(sum(line[(3 * i) % len(line)] == "#" for i, line in enumerate(lines)))

# Part 2
sol = 1
for (si, sj) in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    sol *= sum(
        lines[i][(i // si * sj) % len(lines[i])] == "#"
        for i in range(0, len(lines), si)
    )
print(sol)
