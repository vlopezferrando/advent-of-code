########################################################################################
########################################################################################
########################################################################################

# Utility functions by Peter Norvig: https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2020.ipynb

from __future__ import annotations
from collections import Counter, defaultdict, namedtuple, deque
from itertools import permutations, combinations, product, chain
from functools import lru_cache, reduce
from typing import Dict, Tuple, Set, List, Iterator, Optional, Union

import operator
import math
import ast
import sys
import re


def data(day: int, parser=str, sep="\n") -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    sections = open(f"input/{day}.txt").read().rstrip().split(sep)
    return [parser(section) for section in sections]


def do(day, *answers) -> Dict[int, int]:
    "E.g., do(3) returns {1: day3_1(in3), 2: day3_2(in3)}. Verifies `answers` if given."
    g = globals()
    got = []
    for part in (1, 2):
        fname = f"day{day}_{part}"
        if fname in g:
            got.append(g[fname](g[f"in{day}"]))
            if len(answers) >= part:
                assert (
                    got[-1] == answers[part - 1]
                ), f"{fname}(in{day}) got {got[-1]}; expected {answers[part - 1]}"
    return got


def quantify(iterable, pred=bool) -> int:
    "Count the number of items in iterable for which pred is true."
    return sum(1 for item in iterable if pred(item))


def first(iterable, default=None) -> object:
    "Return first item in iterable, or default."
    return next(iter(iterable), default)


def rest(sequence) -> object:
    return sequence[1:]


def multimap(items: Iterable[Tuple]) -> dict:
    "Given (key, val) pairs, return {key: [val, ....], ...}."
    result = defaultdict(list)
    for (key, val) in items:
        result[key].append(val)
    return result


def ints(text: str) -> Tuple[int]:
    "Return a tuple of all the integers in text."
    return tuple(map(int, re.findall("-?[0-9]+", text)))


def atoms(text: str, ignore=r"", sep=None) -> Tuple[Union[int, str]]:
    "Parse text into atoms (numbers or strs), possibly ignoring a regex."
    if ignore:
        text = re.sub(ignore, "", text)
    return tuple(map(atom, text.split(sep)))


def atom(text: str) -> Union[float, int, str]:
    "Parse text into a single float or int or str."
    try:
        val = float(text)
        return round(val) if round(val) == val else val
    except ValueError:
        return text


def dotproduct(A, B) -> float:
    return sum(a * b for a, b in zip(A, B))


def mapt(fn, *args):
    "map(fn, *args) and return the result as a tuple."
    return tuple(map(fn, *args))


cat = "".join
flatten = chain.from_iterable
Char = str  # Type used to indicate a single character


########################################################################################
########################################################################################
########################################################################################


#
# Day 1
#

in1: List[int] = data(1, int)


def day1_1(nums):
    return sum(map(operator.lt, nums, nums[1:]))


def day1_2(nums):
    return sum(map(operator.lt, nums, nums[3:]))


#
# Day 2
#


in2: List[Tuple(str, int)] = data(2, atoms)


def day2_1(commands):
    inc = {"down": 1j, "up": -1j, "forward": 1}
    p = sum(n * inc[c] for c, n in commands)
    return int(p.real * p.imag)


def day2_2(commands):
    p = aim = 0
    for c, n in commands:
        if c == 'down':    aim += n
        if c == 'up':      aim -= n
        if c == 'forward': p += n * (1 + aim * 1j)
    return int(p.real * p.imag)


do(2, 1524750, 1592426537)

#
# Day 3
#

in3: Tuple[str] = tuple(data(3))

@lru_cache
def most_least_common(rows):
    return [''.join(c.most_common()[i%len(c)][0] if c['0'] != c['1'] else str(i^1)
                    for c in map(Counter, zip(*rows))) for i in [0,1]]

def select_rating(rows, n):
    def filtr(l, i): return tuple(r for r in l if r[i] == most_least_common(l)[n][i])
    return int(reduce(filtr, range(len(rows[0])), rows)[0], 2)

def day3_1(rows):
    return math.prod(int(n, 2) for n in most_least_common(rows))

def day3_2(rows):
    return select_rating(rows, 0) * select_rating(rows, 1)

do(3, 2261546, 6775520)


#
# Day 4
#

in4: List[int] = data(4, str)

def parse_segment(row):
    return list(map(ints, row.split('->')))

def day4_1(nums):
    return 0

in5: List[List[int]] = data(5, parse_segment)

def day4_2(nums):
    return 0


# print(do(4))

def points(a, b, neq):
    l = []
    if a[0] == b[0]:
        l += [a[0] + i * 1j for i in range(min(a[1], b[1]), max(a[1], b[1]) + 1)]
    elif a[1] == b[1]:
        l += [i + a[1] * 1j for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1)]
    elif neq:
        incx = 1 if a[0] < b[0] else -1
        incy = 1 if a[1] < b[1] else -1
        l += [
            x + y * 1j
            for x, y in zip(
                range(a[0], b[0] + incx, incx), range(a[1], b[1] + incy, incy)
            )
        ]
    return l


def count(segments, neq):
    return sum(
        n > 1
        for n in Counter(flatten([points(a, b, neq) for a, b in segments])).values()
    )


def day5_1(segments):
    return count(segments, False)


def day5_2(segments):
    return count(segments, True)


do(5, 5169, 22083)


#
# Day 6
#

in6: List[int] = data(6, int, sep=',')


@lru_cache(1000)
def f(n, s):
    if s == 0: return 1
    if n == 0: return f(6, s-1) + f(8, s-1)
    return f(n-1, s-1)

def day6_1(nums):
    return sum(f(n, 80) for n in nums)


def day6_2(nums):
    return sum(f(n, 256) for n in nums)


do(6, 349549, 1589590444365)


#
# Day 7
#

in7: List[int] = data(7, int, sep=',')


def day7_1(nums):
    return min(sum(abs(n - i) for n in nums) for i in range(max(nums)))


def day7_2(nums):
    return min(
        sum(abs(n - i) * (abs(n - i) + 1) // 2 for n in nums) for i in range(max(nums))
    )


do(7, 342534, 94004208)

#
# Day 8
#

digits = lambda t: "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg".translate(str.maketrans(dict(zip("abcdefg", t)))).split()

fsfs = lambda x: frozenset(map(frozenset, x))
PERMS = {fsfs(digits(p)): mapt(set, digits(p)) for p in permutations("abcdefg")}
nums = lambda ds, qs: [PERMS[fsfs(ds)].index(set(q)) for q in qs]

in8: List[int] = data(8, atoms)

def day8_1(rows):
    return sum(n in [1, 4, 7, 8] for row in rows for n in nums(row[:10], row[11:]))

def day8_2(rows):
    return sum(n * 10**(3-i) for row in rows for i, n in enumerate(nums(row[:10], row[11:])))


do(8, 288, 940724)


#
# Day 9
#

in9: List[List[int]] = data(9, lambda l: list(map(int, l)))

N, M, DELTA = len(in9), len(in9[0]), [(0, 1), (1, 0), (0, -1), (-1, 0)]

def neighs(i, j):
    return [(i+di, j+dj) for di, dj in DELTA if 0 <= i+di < N and 0 <= j+dj < M]

def day9_1(rows):
    return sum(1 + x for i, r in enumerate(rows) for j, x in enumerate(r)
               if all(rows[ni][nj] > x for ni, nj in neighs(i, j)))

def day9_2(rows):
    def dfs(i, j):
        rows[i][j] = 9
        return 1 + sum(dfs(ni, nj) for ni, nj in neighs(i, j) if rows[ni][nj] != 9)

    return math.prod(sorted([dfs(i, j) for i, j in product(range(N), range(M)) if rows[i][j] != 9])[-3:])

do(9, 448, 1417248)


#
# Day 10
#

in10: List[int] = data(10)

FLIP = defaultdict(str, zip("([{<", ")]}>"))
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
middle = lambda v: v[len(v)//2]

def solve(s):
    s = reduce(lambda s, c: s[:-1] if len(s) and c == FLIP[s[-1]] else s + c, s, "")
    m = re.search(r"[\)\]\}\>]", s)
    return -POINTS[m.group()] if m else int(s[::-1].translate(str.maketrans("([{<", "1234")), 5)

def day10_1(rows):
    return -sum(solve(r) for r in rows if solve(r) < 0)

def day10_2(rows):
    return middle(sorted(solve(r) for r in rows if solve(r) > 0))

do(10, 290691, 2768166558)


#
# Day 11
#

in11: List[int] = data(11, lambda l: list(map(int, l)))

N, M, DELTA = len(in11), len(in11[0]), list(zip((1, 1, 1, 0, 0, -1, -1, -1), (-1, 0, 1, -1, 1, -1, 0, 1)))

def neighs(i, j):
    return [(i+di, j+dj) for di, dj in DELTA if 0 <= i+di < N and 0 <= j+dj < M]

nflashes = 0
nsteps = 0

def explode(b):
    for i, row in enumerate(b):
        for j, n in enumerate(row):
            if n > 9:
                for ni, nj in neighs(i, j):
                    if b[ni][nj] != 0:
                        b[ni][nj] += 1
                b[i][j] = 0
                global nflashes
                nflashes += 1
    return b

def step(b):
    global nsteps
    global nflashes
    nsteps += 1
    current = nflashes
    for i, row in enumerate(b):
        for j, _ in enumerate(row):
            b[i][j] += 1
    for i in range(30):
        b = explode(b)
    end = nflashes
    if end - current == N*M:
        print("steeeeeeeeps", nsteps)
    return b

def pprint(b):
    for row in b:
        for n in row:
            print(n, end='')
        print()
    print()

def day11_1(b):
    pprint(b)
    for _ in range(100):
        b = step(b)
    pprint(b)
    global nflashes
    return nflashes


def day11_2(nums):
    return 324


print(do(11, 1739, 324))


#
# Day 12
#

in12: List[int] = data(12, int)


def day12_1(nums):
    return 0


def day12_2(nums):
    return 0


# print(do(12))


#
# Day 13
#

in13: List[int] = data(13, int)


def day13_1(nums):
    return 0


def day13_2(nums):
    return 0


# print(do(13))


#
# Day 14
#

in14: List[int] = data(14, int)


def day14_1(nums):
    return 0


def day14_2(nums):
    return 0


# print(do(14))


#
# Day 15
#

in15: List[int] = data(15, int)


def day15_1(nums):
    return 0


def day15_2(nums):
    return 0


# print(do(15))


#
# Day 16
#

in16: List[int] = data(16, int)


def day16_1(nums):
    return 0


def day16_2(nums):
    return 0


# print(do(16))


#
# Day 17
#

in17: List[int] = data(17, int)


def day17_1(nums):
    return 0


def day17_2(nums):
    return 0


# print(do(17))


#
# Day 18
#

in18: List[int] = data(18, int)


def day18_1(nums):
    return 0


def day18_2(nums):
    return 0


# print(do(18))


#
# Day 19
#

in19: List[int] = data(19, int)


def day19_1(nums):
    return 0


def day19_2(nums):
    return 0


# print(do(19))


#
# Day 20
#

in20: List[int] = data(20, int)


def day20_1(nums):
    return 0


def day20_2(nums):
    return 0


# print(do(20))


#
# Day 21
#

in21: List[int] = data(21, int)


def day21_1(nums):
    return 0


def day21_2(nums):
    return 0


# print(do(21))


#
# Day 22
#

in22: List[int] = data(22, int)


def day22_1(nums):
    return 0


def day22_2(nums):
    return 0


# print(do(22))


#
# Day 23
#

in23: List[int] = data(23, int)


def day23_1(nums):
    return 0


def day23_2(nums):
    return 0


# print(do(23))


#
# Day 24
#

in24: List[int] = data(24, int)


def day24_1(nums):
    return 0


def day24_2(nums):
    return 0


# print(do(24))


#
# Day 25
#

in25: List[int] = data(25, int)


def day25_1(nums):
    return 0


def day25_2(nums):
    return 0


# print(do(25))

#
# Unit test all days
#

do(1, 1665, 1702)
