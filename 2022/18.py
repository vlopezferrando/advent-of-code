#
# Check an explanation of this code: https://youtu.be/pBdknrCFKJc
#

from collections import deque
from itertools import chain, product


# Read input
cubes = set(tuple(map(int, line.split(","))) for line in open("18.in"))
MIN, MAX = min(chain(*cubes)), max(chain(*cubes))

DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
neighbours = lambda x, y, z: [(x + dx, y + dy, z + dz) for dx, dy, dz in DIRS]
surface = lambda cubes: sum(n not in cubes for cube in cubes for n in neighbours(*cube))

# Part 1
p1 = surface(cubes)
assert p1 == 4282

# Part 2
space = set(product(range(MIN - 1, MAX + 1), repeat=3)) - cubes

Q = deque([(MIN, MIN, MIN)])
while len(Q) > 0:
    c = Q.popleft()
    if c in space:
        space.remove(c)
        Q += neighbours(*c)

p2 = surface(cubes | space)
assert p2 == 2452

"""
Lessons learned:
1. Use deque for faster BFS
2. itertools.chain to join all coordinates in a single list
3. itertools.product for compact generation of all (x, y, z)
4. c = Q.popleft() as a simple alternative to c, *Q = Q
5. Simple algorithm: create a space bigger than the object, and do a BFS starting from the
   edge to only leave without visit the cubes inside the object.
6. Important use of tubples for creating sets.
"""
