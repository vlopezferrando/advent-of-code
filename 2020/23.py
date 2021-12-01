def play(next, i, n):
    for _ in range(n):
        a = next[i]
        b = next[a]
        c = next[b]

        dest = i
        while dest in [i, a, b, c]:
            dest = (dest - 1) % len(next)

        next[i] = i = next[c]
        next[c] = next[dest]
        next[dest] = a


# Read input
l = [int(n) - 1 for n in "198753462"]

# Part 1
next = [-1] * len(l)
for i, n in enumerate(l):
    next[n] = l[(i + 1) % len(l)]

play(next, l[0], 100)

n = next[0]
while n:
    print(n + 1, end="")
    n = next[n]
print()

# Part 2
next = list(range(1, 1_000_000)) + [l[0]]
for i, n in enumerate(l[:-1]):
    next[n] = l[i + 1]
next[l[-1]] = len(l)

play(next, l[0], 10_000_000)
print((next[0] + 1) * (next[next[0]] + 1))
