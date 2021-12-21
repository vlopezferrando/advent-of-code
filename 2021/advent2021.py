########################################################################################
########################################################################################
########################################################################################

# Utility functions by Peter Norvig: https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2020.ipynb

from __future__ import annotations
from collections import Counter, defaultdict, namedtuple, deque
from itertools import permutations, combinations, product, chain, islice, accumulate, count
from functools import lru_cache, reduce
from typing import Dict, Tuple, Set, List, Iterator, Optional, Union, no_type_check_decorator

import operator
import math
import ast
import sys
import re

from numpy.lib.financial import nper
from numpy.lib.shape_base import column_stack


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

#
# Day 4
#

in4 = data(4, sep='\n\n')

nums4 = list(map(int, in4[0].split(',')))
boards4 = [[ints(l) for l in board.splitlines()] for board in in4[1:]]

def solve4():
    return sorted([
        next((i, sum(set(flatten(b)) - set(nums4[:i]))*nums4[i-1])
        for i, _ in enumerate(nums4)
        if any(set(nums4[:i]).issuperset(l) for l in b + list(zip(*b)))
    ) for b in boards4])

def day4_1(nums):
    return solve4()[0][1]

def day4_2(nums):
    return solve4()[-1][1]


#
# Day 5
#

def parse_segment(row):
    return list(map(ints, row.split('->')))

in5: List[List[int]] = data(5, parse_segment)

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

def count2(segments, neq):
    return sum(
        n > 1
        for n in Counter(flatten([points(a, b, neq) for a, b in segments])).values()
    )

def day5_1(segments):
    return count2(segments, False)


def day5_2(segments):
    return count2(segments, True)

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


#
# Day 11
#

in11: List[int] = data(11, lambda l: list(map(int, l)))

N, M, DELTA = len(in11), len(in11[0]), list(zip((1, 1, 1, 0, 0, -1, -1, -1), (-1, 0, 1, -1, 1, -1, 0, 1)))
neighs = lambda i, j: [(i+di, j+dj) for di, dj in DELTA if 0 <= i+di < N and 0 <= j+dj < M]

def explode(b, nflashes=0):
    for i, j in product(range(N), range(M)):
        if b[i][j] > 9:
            b[i][j] = 0
            for ni, nj in neighs(i, j):
                b[ni][nj] += b[ni][nj] != 0
            nflashes += 1
    return b, nflashes

step = lambda b: reduce(lambda p, _: explode(*p), range(N*M), ([[n+1 for n in r] for r in b], 0))
steps = lambda b: accumulate(count(), lambda p, _: step(p[0]), initial=(b, 0))

def day11_1(b):
    return sum(n for _, n in islice(steps(b), 101))

def day11_2(b):
    return next(i for i, (_, n) in enumerate(steps(b)) if n == N*M)

#
# Day 12
#

in12 = data(12, lambda l: l.split('-'))

G = defaultdict(list)
for a, b in in12:
    G[a].append(b)
    G[b].append(a)

def dfs(current, visited, can_repeat):
    return 0 if str.islower(current) and current in visited and (not can_repeat or current == 'start') else sum(dfs(n, visited + [current], can_repeat and not (str.islower(current) and current in visited)) if n != 'end' else 1 for n in G[current])

def day12_1(edges):
    return dfs('start', [], False)

def day12_2(edges):
    return dfs('start', [], True)


#
# Day 13
#

def parse_input(coordinates, folds):
    return set(mapt(ints, coordinates)), [(f.split('=')[0][-1], int(f.split('=')[1])) for f in folds]

in13  = parse_input(*data(13, str.splitlines, sep='\n\n'))

foldc = lambda x, n: x if x < n else n - (x - n)
fold = lambda coords, f: set([(foldc(x, f[1]), y) if f[0] == 'x' else (x, foldc(y, f[1])) for x, y in coords])

def day13_1(data):
    return len(fold(data[0], data[1][0]))

def day13_2(data):
    coords = reduce(fold, data[1], data[0])
    print('\n'.join(''.join('#' if (x, y) in coords else '.' for x in range(max(x for x, _ in coords)+1)) for y in range(max(y for _, y in coords)+1)))
    return "HLBUBGFR"

#
# Day 14
#

def parse_input14(initial, rules):
    return initial[0], {
        rule.split()[0]: (rule.split()[0][0] + rule.split()[2], rule.split()[2] + rule.split()[0][1])
        for rule in rules
    }

in14  = parse_input14(*data(14, str.splitlines, sep='\n\n'))

def solve(s, G, N):
    # Reverse graph
    R = {k: list(flatten([[kk for vv in v if vv == k] for kk, v in G.items()])) for k in G}
    
    # Initialize count of each pair
    d = {k: s.count(k) for k in G}

    # Update N times the count of each pair
    for _ in range(N):
        d = {k: sum(d[x] for x in R[k]) for k in G}
    
    # Count letter frequency
    freqs = [sum(n * k.count(c) for k, n in d.items()) for c in set(flatten(d.keys()))]

    # Return max minus min divided by two
    return math.floor(max(freqs)/2 - min(freqs)/2)

def day14_1(data):
    return solve(*data, 10)

def day14_2(data):
    return solve(*data, 40)

#
# Day 15
#

in15: List[int] = data(15, lambda l: mapt(int, list(l)))

import heapq
DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
Visit = namedtuple('Visit', ['dist', 'x', 'y'])

def dijkstra(board):
    N = len(board)
    seen = [[False]*N for _ in range(N)]
    l = [Visit(0, 0, 0)]
    while v := heapq.heappop(l):
        if v.x == v.y == N-1:
            return v.dist
        for di, dj in DELTA:
            ni, nj = v.x + di, v.y + dj
            if 0 <= ni < N and 0 <= nj < N and not seen[ni][nj]:
                seen[ni][nj] = True
                heapq.heappush(l, Visit(v.dist + board[ni][nj], ni, nj))

def day15_1(board):
    return dijkstra(board)

def day15_2(board):
    N = len(board)
    return dijkstra([[(board[i%N][j%N] + i//N + j//N - 1) % 9 + 1 for j in range(5*N)] for i in range(5*N)])


#
# Day 16
#

in16: List[int] = data(16)

NUM_RE = re.compile(r'([01]{3})100' + r'(?:1([01]{4}))?'*20 + r'(?:0([01]{4}))')
OP_RE = re.compile(r'([01]{3})([01]{3})(?:(0)([01]{15})|(1)([01]{11}))')

def one_packet(s):
    if m := NUM_RE.match(s):
        ver, num = m.groups()[0], ''.join(g for g in m.groups()[1:] if g)
        return {'num': int(num, 2), 'ver': int(ver, 2)}, s[m.span()[1]:]
    elif m := OP_RE.match(s):
        s = s[m.span()[1]:]
        ver, code, is_nbits, nbits, is_npackets, npackets = m.groups()
        if is_nbits:
            nbits = int(nbits, 2)
            return {'op': int(code, 2), 'ver': int(ver, 2), 'ops': packets(s[:nbits])}, s[nbits:]
        elif is_npackets:
            npackets = int(npackets, 2)
            l = []
            for _ in range(npackets):
                p, s = one_packet(s)
                l.append(p)
            return {'op': int(code, 2), 'ver': int(ver, 2), 'ops': l}, s

def packets(s):
    while s != '':
        p, s = one_packet(s)
        yield p

to_bin = lambda s: bin(int(s, 16))[2:].zfill(len(s)*4)
sum_ver = lambda d: d['ver'] + (sum(map(sum_ver, d['ops'])) if 'ops' in d else 0)

star = lambda f: lambda r: f(*r)
OPS = [sum, math.prod, min, max, None, star(operator.gt), star(operator.lt), star(operator.eq)]
calc = lambda d: d['num'] if 'num' in d else OPS[d['op']](map(calc, d['ops']))

def day16_1(n):
    return sum_ver(one_packet(to_bin(n[0]))[0])

def day16_2(n):
    return calc(one_packet(to_bin(n[0]))[0])

#
# Day 17
#

in17: List[int] = data(17)

x0, x1, y0, y1 = 269, 292, -68, -44

def points(vx, vy, x=0, y=0):
    while y0 <= y and x <= x1:
        yield x, y
        x, y, vx, vy = x+vx, y+vy, max(0, vx-1), vy-1

solutions = [v for v in product(range(1000), range(-300, 300))
             if any(x0 <= x <= x1 and y0 <= y <= y1 for x, y in points(*v))]

def day17_1(_):
    return max(vy*(vy+1)//2 for _, vy in solutions)

def day17_2(_):
    return len(solutions)

#
# Day 18
#

in18: List[int] = data(18, eval)

def split(s):
    if isinstance(s, int):
        return (s, False) if s < 10 else ([s//2, math.ceil(s/2)], True)
    L, splitted = split(s[0])
    if splitted:
        return [L, s[1]], True
    R, splitted = split(s[1])
    return [L, R], splitted

add_right = lambda s, n: s+n if isinstance(s, int) else [s[0], add_right(s[1], n)]
add_left =  lambda s, n: s+n if isinstance(s, int) else [add_left(s[0], n), s[1]]

def explode(s, depth=0):
    if isinstance(s, int):
        return s, False, 0, 0
    if depth == 4:
        return 0, True, s[0], s[1]
    L, exploded, suml, sumr = explode(s[0], depth+1)
    if exploded:
        return [L, add_left(s[1], sumr)], True, suml, 0
    R, exploded, suml, sumr = explode(s[1], depth+1)
    if exploded:
        return [add_right(s[0], suml), R], True, 0, sumr
    return [L, R], False, 0, 0

def reduce_snails(s):
    s, exploded, _, _ = explode(s)
    if exploded:
        return reduce_snails(s)
    s, splitted = split(s)
    if splitted:
        return reduce_snails(s)
    return s

def sum_snails(s, r):
    return reduce_snails([s, r])

def magnitude(s):
    if isinstance(s, int):
        return s
    return 3*magnitude(s[0]) + 2*magnitude(s[1])

def day18_1(snails):
    return magnitude(reduce(sum_snails, snails[1:], snails[0]))

def day18_2(snails):
    return max(magnitude(sum_snails(a, b)) for a in snails for b in snails)

#
# Day 19
#

import numpy as np

in19 = data(19, lambda s: mapt(ints, s.splitlines()[1:]), sep='\n\n')

ROTATIONS = [mat for a, b, c in product(((1,0,0), (-1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)), repeat=3)
    if all([a[i], b[i], c[i]].count(0) == 2 for i in range(3)) and np.linalg.det(mat := np.array((a,b,c))) == 1]

def normalize(scans, candidates, normalized, positions=[(0, 0, 0)]):
    if len(scans) == len(normalized): return positions, normalized
    for i, cs in candidates.items():
        if i in normalized:
            for j in cs:
                if j not in normalized:
                    ps = [(mapt(int, (p - rot @ np.array(q)).tolist()), rot)
                            for p, q in product(normalized[i], scans[j]) for rot in ROTATIONS]
                    if (mc := Counter([c for c, _ in ps]).most_common(1)[0])[1] == 12:
                        rotation = next(rot for pos, rot in ps if pos == mc[0])
                        normalized[j] = [list(map(int, (rotation@np.array(s) + mc[0]).tolist())) for s in scans[j]]
                        return normalize(scans, candidates, normalized, positions + [mc[0]])

dist = lambda p, q: sum(map(abs, [p[0]-q[0], p[1]-q[1], p[2]-q[2]]))

def candidates(scans):
    dists = [set(dist(p, q) for p in s for q in s) for s in scans]
    return {
        i: [j for j in range(len(scans)) if i != j and (len(dists[i] & dists[j]) > 60)]
        for i in range(len(scans))
    }

positions, normalized = normalize(in19, candidates(in19), {0: in19[0]})

def day19_1(_):
    return len(set([str(list(s)) for s in flatten(normalized.values())]))

def day19_2(_):
    return max(dist(*pq) for pq in product(positions, repeat=2))

#
# Day 20
#

in20: List[int] = data(20, str.splitlines, sep='\n\n')
rep = lambda s: s.replace('.', '0').replace('#', '1')
LINE, B, N = rep(in20[0][0]), [list(rep(s)) for s in in20[1]], len(in20[1])

DELTA = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
neighs = lambda x, y: [(x+dx, y+dy) for dx, dy in DELTA]

change = lambda board: [[LINE[int(''.join(board[ni][nj] for ni, nj in neighs(i, j)), 2)] if 0 < i < len(board)-1 and 0 <= j < len(row)-1 else '0'
            for j, _ in enumerate(row)] for i, row in enumerate(board)]
with_margin = lambda b, M: [['0']*(N + 2*M) for _ in range(M)] + [['0']*M + row + ['0']*M for row in b] +[['0']*(N + 2*M) for _ in range(M)]
count_lights = lambda b, I: sum(r[I:-I].count('1') for r in b[I:-I])
run = lambda n: count_lights(reduce(lambda b, _: change(b), range(n), with_margin(B, 2*n)), n)

def day20_1(_):
    return run(2)

def day20_2(_):
    return run(50)


#
# Day 21
#

in21 = [4, 6]

def winner(sa, sb, a, b, i, steps):
    return (sa, steps) if sb >= 1000 else winner(sb, sa + (a+3*i+3)%10+1, b, (a+3*i+3)%10, i+3, steps+3)

def day21_1(inp):
    return math.prod(winner(0, 0, inp[0]-1, inp[1]-1, 1, 0))

RESULTS = Counter([sum(x) for x in product([1,2,3], repeat=3)])

@lru_cache(100000)
def wins(sa, sb, a, b):
    return (0, 1) if sb >= 21 else list(map(sum, zip(*[
        (times * wp[1], times * wp[0])
        for n, times in RESULTS.items() if (wp := wins(sb, sa + (a + n) % 10 + 1, b, (a + n) % 10))
    ])))

def day21_2(inp):
    return max(wins(0, 0, inp[0]-1, inp[1]-1))


#
# Unit test all days
#

do(1, 1665, 1702)
do(2, 1524750, 1592426537)
do(3, 2261546, 6775520)
do(4, 33348, 8112)
do(5, 5169, 22083)
do(6, 349549, 1589590444365)
do(7, 342534, 94004208)
do(8, 288, 940724)
do(9, 448, 1417248)
do(10, 290691, 2768166558)
do(11, 1739, 324)
do(12, 4970, 137948)
do(13, 810, "HLBUBGFR")
do(14, 2435, 2587447599164)
do(15, 604, 2907)
do(16, 969, 124921618408)
do(17, 2278, 996)
do(18, 3675, 4650)
do(19, 396, 11828)
do(20, 5395, 17584)
do(21, 888735, 647608359455719)
