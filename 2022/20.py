#
# Check how I live coded this: https://youtu.be/dz9LkjhQGxc
#

from collections import deque

# Read input
coordinates = list(map(int, open("20.in").read().splitlines()))


def solve(l, steps=1):
    d = deque(enumerate(l))
    for _ in range(steps):
        for p in enumerate(l):
            index = d.index(p)
            d.remove(p)
            d.insert((index + p[1]) % len(d), p)

    d.rotate(-d.index((l.index(0), 0)))
    return d[1000][1] + d[2000][1] + d[3000][1]


# Part 1
p1 = solve(coordinates)
assert p1 == 2827


# Part 2
p2 = solve([n * 811589153 for n in coordinates], 10)
assert p2 == 7834270093909

"""
Lessons learned
1. Heavy use of deque: popleft, rotate, index, remove, insert
2. Enumerate to pair each n with its index (0, x), (1, x1), etc.
3. Modular arithetics: (n+i)%len(d). Works for negative values
4. It is possible to get very short solutions
"""
