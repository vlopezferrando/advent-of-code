#
# Check how I live coded this: https://youtu.be/UgJ4k3oNdtc
#

from functools import cmp_to_key

# Read input
PS = [eval(line) for line in open("13.in") if line.strip()]


def comp(a, b):
    if type(a) == type(b) == int:
        return a - b
    if type(a) == int:
        return comp([a], b)
    if type(b) == int:
        return comp(a, [b])
    if len(a) > 0 and len(b) > 0:
        return comp(a[0], b[0]) if comp(a[0], b[0]) else comp(a[1:], b[1:])
    return len(a) - len(b)


# Part 1
p1 = sum(i + 1 for i, (a, b) in enumerate(zip(PS[::2], PS[1::2])) if comp(a, b) < 0)
assert p1 == 4821


# Part 2
PS = sorted(PS + [[[2]], [[6]]], key=cmp_to_key(comp))
p2 = (PS.index([[2]]) + 1) * (PS.index([[6]]) + 1)
assert p2 == 21890

"""
Lessons learned:
1. cmp(a, b) function:
    - negative if a < b
    - 0 if a == b
    - positive if a > b

    In summary: a - b (if these were integers)
2. functools.key=cmp_to_key, used as key parameter in sorted(), .sort()
3. Check the variable type with type(x) == int==, or isinstance(x, int)
4. Iterate pairs of elements in a list with zip(l[::2], l[1::2])
5. l.index(x) -> find the index of element x in a list
6. eval() -> evaluate a string as python
7. Builtins: sum, sorted, enumerate, zip, len, eval, open
"""
