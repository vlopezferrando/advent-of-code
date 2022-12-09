#
# Check how I live coded this: https://youtu.be/HOEXhmmdMxY
#

# Read input
moves = [(line[0], int(line[2:])) for line in open("09.in")]

DIR = {"L": -1, "R": 1, "U": -1j, "D": 1j}


def tail_positions(knots):
    for d, steps in moves:
        for _ in range(steps):
            # Move head in direction d
            knots[0] += DIR[d]

            # Move each knot if necessary
            for i, (h, t) in enumerate(zip(knots, knots[1:])):
                if abs(h.real - t.real) == 2 or abs(h.imag - t.imag) == 2:
                    if h.real != t.real:
                        t += (h.real - t.real) / abs(h.real - t.real)
                    if h.imag != t.imag:
                        t += 1j * (h.imag - t.imag) / abs(h.imag - t.imag)
                    knots[i + 1] = t

            # Yield tail position
            yield knots[-1]


# Part 1
assert len(set(tail_positions([0, 0]))) == 6311

# Part 2
assert len(set(tail_positions([0] * 10))) == 2482

"""
Lessons learned
1. Use complex numbers (1+1j) to represent coordinates in a grid
   c = 1+1j
   c.real -> real component
   c.imag -> imaginary component
2. abs -> absolute value
3. To iterate consecutive pairs in a list: [1, 2, 3, 4] -> (1, 2), (2, 3), (3, 4)
   for prev, next in zip(knots, knots[1:]):
4. yield -> make a function a generator
5. [0] * 10 -> create a list of 10 equal elements
   [[1, 2, 3]]*10 CAREFUL!
   Usually, you want to do: l = [[1, 2, 3] for _ in range(10)]
6. (h.real - t.real) / abs(h.real - t.real) to move one unit in the real direction
"""
