#
# Check how I live coded this: https://youtu.be/sOG8ZXwDowQ
#

# Read input
rocks = set()
for line in open("14.in"):
    for a, b in zip(line.split()[0::2], line.split()[2::2]):
        x0, y0, x1, y1 = map(int, a.split(",") + b.split(","))
        if x0 == x1:
            dy = (y1 - y0) // abs(y1 - y0)
            rocks |= set((x0, y) for y in range(y0, y1 + dy, dy))
        elif y0 == y1:
            dx = (x1 - x0) // abs(x1 - x0)
            rocks |= set((x, y0) for x in range(x0, x1 + dx, dx))

SAND_SOURCE = (500, 0)
ABYSS = 200


def fall(x, y, floor=None):
    # Down by the abyss
    if y == ABYSS:
        return SAND_SOURCE

    # Hit the floor
    if floor and y + 1 == floor:
        return x, y

    # If we can fall 1 step
    for nx in [x, x - 1, x + 1]:
        if (nx, y + 1) not in rocks:
            return fall(nx, y + 1, floor)

    # Stay in the same place
    return x, y


def generate_sand(floor=None):
    initial_rocks = len(rocks)
    while (p := fall(*SAND_SOURCE, floor)) != SAND_SOURCE:
        rocks.add(p)
    return len(rocks) - initial_rocks


# Part 1
p1 = generate_sand()
assert p1 == 885

# Part 2
p2 = p1 + 1 + generate_sand(floor=max(y for _, y in rocks) + 2)
assert p2 == 28691

"""
Lessons learned
1. Take the last element in a generator: *_, last = generator()
2. Tuple expansion to call a function with a list: f(*[1, 2, 3])
3. Walrus operator: while (p := f()) != -1: print(p)
4. Set union with: {1, 2, 3} | {4, 5, 6} == {1, 2, 3, 4, 5, 6}. Also |=
5. zip(l[::2], l[2::2]) -> every pair of elements in a list
"""
