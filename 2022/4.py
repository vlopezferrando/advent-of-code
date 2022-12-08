# Read input

ranges = [list(map(int, line.split())) for line in open("4.in")]


# Part 1


def contains(a1: int, a2: int, b1: int, b2: int):
    """Check if interval [a1,a2] contains interval [b1,b2]"""
    assert a1 <= a2
    assert b1 <= b2
    return a1 <= b1 and a1 <= b2 and b1 <= a2 and b2 <= a2


sol_1 = sum(
    [contains(a1, a2, b1, b2) or contains(b1, b2, a1, a2) for a1, a2, b1, b2 in ranges]
)
assert sol_1 == 453

# Part 2


def overlap(a1: int, a2: int, b1: int, b2: int):
    """Check if there is any overlap between intervals [a1,a2] and [b1,b2]"""
    assert a1 <= a2
    assert b1 <= b2
    return a2 >= b1 and b2 >= a1


sol_2 = sum(overlap(*r) for r in ranges)
assert sol_2 == 919

"""
Lessons learned:
1. Lost some time for not converting numbers to ints
   Ways in which we could have prevented this:
       - Add type hints in the function parameters e.g. f(n: int)
       - Use asserts
2. We modified the input before parsing
3. Sums of booleans: sum([True, False, True])
4. Used tuple unpacking (*r) to make a function call and list comprehension shorter
"""
