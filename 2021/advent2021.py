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
    return [''.join(c.most_common()[i%len(c)][0] if c['0'] != c['1'] else str((i+1)%2)
                    for c in map(Counter, zip(*rows))) for i in [0,1]]

def select_rating(rows, n):
    def filtr(l, i): return tuple(r for r in l if r[i] == most_least_common(l)[n][i])
    return int(reduce(filtr, range(len(rows[0])), rows)[0], 2)

def day3_1(rows):
    return math.prod(int(n, 2) for n in most_least_common(rows))

def day3_2(rows):
    return select_rating(rows, 0) * select_rating(rows, 1)

print(do(3, 2261546, 6775520))


#
# Day 4
#

in4: List[int] = data(4, int)


def day4_1(nums):
    return 0


def day4_2(nums):
    return 0


# print(do(4))


#
# Day 5
#

in5: List[int] = data(5, int)


def day5_1(nums):
    return 0


def day5_2(nums):
    return 0


# print(do(5))


#
# Day 6
#

in6: List[int] = data(6, int)


def day6_1(nums):
    return 0


def day6_2(nums):
    return 0


# print(do(6))


#
# Day 7
#

in7: List[int] = data(7, int)


def day7_1(nums):
    return 0


def day7_2(nums):
    return 0


# print(do(7))


#
# Day 8
#

in8: List[int] = data(8, int)


def day8_1(nums):
    return 0


def day8_2(nums):
    return 0


# print(do(8))


#
# Day 9
#

in9: List[int] = data(9, int)


def day9_1(nums):
    return 0


def day9_2(nums):
    return 0


# print(do(9))


#
# Day 10
#

in10: List[int] = data(10, int)


def day10_1(nums):
    return 0


def day10_2(nums):
    return 0


# print(do(10))


#
# Day 11
#

in11: List[int] = data(11, int)


def day11_1(nums):
    return 0


def day11_2(nums):
    return 0


# print(do(11))


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
