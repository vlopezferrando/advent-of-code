# Read input
v = sorted([int(l) for l in open("10.in")])
v = [0] + v + [v[-1] + 3]

# Part 1
print(
    sum(b - a == 1 for a, b, in zip(v, v[1:]))
    * sum(b - a == 3 for a, b, in zip(v, v[1:]))
)

# Part 2
ways = [1] + [0] * v[-1]
for n in v:
    for m in range(max(n - 3, 0), n):
        ways[n] += ways[m]
print(ways[-1])
