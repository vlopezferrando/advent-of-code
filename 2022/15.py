#
# Check how I live coded this: https://youtu.be/B_kNGCvHZ7g
#

import collections

# Read input
sensors = []
beacons_in_row = collections.defaultdict(set)
for line in open("15.in"):
    row = line.split()
    sx, sy, bx, by = map(int, (row[2][2:-1], row[3][2:-1], row[8][2:-1], row[9][2:]))
    sensors.append((sx, sy, abs(sx - bx) + abs(sy - by)))
    beacons_in_row[by].add(bx)


def union(intervals):
    intervals.sort()
    current = intervals[0]
    for ivl in intervals[1:]:
        if current[1] < ivl[0]:
            yield current
            current = ivl
        elif ivl[1] > current[1]:
            current[1] = ivl[1]
    yield current


def intersect_with(intervals, ivl):
    return [[max(iv[0], ivl[0]), min(iv[1], ivl[1])] for iv in intervals]


def empty_intervals_in_line(Y):
    return [[x - d + vd, x + d - vd] for x, y, d in sensors if (vd := abs(Y - y)) <= d]


# Part 1
Y = 2_000_000
p1 = sum(
    x1 - x0 + 1 - sum(x0 <= bx <= x1 for bx in beacons_in_row[Y])
    for x0, x1 in union(empty_intervals_in_line(Y))
)
assert p1 == 4560025

# Part 2
def part2(maxY, startY):
    for Y in range(startY, maxY + 1):
        intervals = list(union(intersect_with(empty_intervals_in_line(Y), [0, maxY])))
        if len(intervals) == 2:
            assert intervals[0][1] + 2 == intervals[1][0]
            return maxY * (intervals[0][1] + 1) + Y


p2 = part2(4_000_000, 2_634_000)
assert p2 == 12480406634249

"""
Lessons learned
1. Thousands divider: 4_000_000
2. collections.defaultdict(set)
3. Walrus operator in for loops: [sq for x in range(10) if (sq := x**2) < 100]
4. assert to make sure we are on track
"""
