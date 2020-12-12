# Read input
steps = [(l[0], int(l[1:])) for l in open('12.in')]

# Part 1
x, y, dx, dy = 0, 0, 1, 0
for c, n in steps:
    if c == 'E':
        x += n
    elif c == 'W':
        x -= n
    elif c == 'N':
        y += n
    elif c == 'S':
        y -= n
    elif c == 'R':
        for _ in range(n//90):
            dx, dy = dy, -dx
    elif c == 'L':
        for _ in range(n//90):
            dx, dy = -dy, dx
    elif c == 'F':
        x += n * dx
        y += n * dy
print(abs(x) + abs(y))

# Part 2
x, y, wx, wy = 0, 0, 10, 1
for c, n in steps:
    if c == 'E':
        wx += n
    elif c == 'W':
        wx -= n
    elif c == 'N':
        wy += n
    elif c == 'S':
        wy -= n
    elif c == 'R':
        for _ in range(n//90):
            wx, wy = wy, -wx
    elif c == 'L':
        for _ in range(n//90):
            wx, wy = -wy, wx
    elif c == 'F':
        x += n * wx
        y += n * wy
print(abs(x) + abs(y))
