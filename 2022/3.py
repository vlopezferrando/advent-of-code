import string

lines = open("3.in").read().splitlines()


def priority(type_):
    return 1 + (string.ascii_lowercase + string.ascii_uppercase).index(type_)


# Part 1
def intersect_halves(s):
    middle = len(s) // 2
    h1, h2 = s[:middle], s[middle:]
    return next(iter(set(h1) & set(h2)))


sol_1 = sum(map(priority, map(intersect_halves, lines)))
assert sol_1 == 7831


# Part 2
def intersect(s1, s2, s3):
    return next(iter(set(s1) & set(s2) & set(s3)))


sol_2 = sum(
    map(priority, [intersect(*lines[i : i + 3]) for i in range(0, len(lines), 3)])
)
assert sol_2 == 2683

"""
Lessons learned
1. string module: ascii_lowercase, ascii_uppercase
2. index function: get the index of an element in a list
3. range slices: s[:2], s[2:]
4. set intersections: {1, 2, 3} & {3, 4, 5}
5. iter() -> convert to an iterator
6. next() -> get the next element in iterator
7. range(0, len(lines), 3) -> range(start, end, step)
8. f(a, b, c)    --- l = [1, 2, 3]; f(*l)
"""
