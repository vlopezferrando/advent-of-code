#
# Check how I live coded this: https://youtu.be/JxkRP8fV-aA
#

import math


def read_monkeys():
    return [
        {
            "items": [56, 52, 58, 96, 70, 75, 72],
            "op": lambda n: n * 17,
            "next": lambda n: 3 if n % 11 else 2,
        },
        {
            "items": [75, 58, 86, 80, 55, 81],
            "op": lambda n: n + 7,
            "next": lambda n: 5 if n % 3 else 6,
        },
        {
            "items": [73, 68, 73, 90],
            "op": lambda n: n * n,
            "next": lambda n: 7 if n % 5 else 1,
        },
        {
            "items": [72, 89, 55, 51, 59],
            "op": lambda n: n + 1,
            "next": lambda n: 7 if n % 7 else 2,
        },
        {
            "items": [76, 76, 91],
            "op": lambda n: n * 3,
            "next": lambda n: 3 if n % 19 else 0,
        },
        {
            "items": [88],
            "op": lambda n: n + 4,
            "next": lambda n: 4 if n % 2 else 6,
        },
        {
            "items": [64, 63, 56, 50, 77, 55, 55, 86],
            "op": lambda n: n + 8,
            "next": lambda n: 0 if n % 13 else 4,
        },
        {
            "items": [79, 58],
            "op": lambda n: n + 6,
            "next": lambda n: 5 if n % 17 else 1,
        },
    ]


def simulate(rounds, limiting_function):
    """Simulate the monkeys' behaviour and return the number of inspections they did"""
    monkeys = read_monkeys()

    inspections = [0] * len(monkeys)
    for _ in range(rounds):
        for i, m in enumerate(monkeys):
            for item in m["items"]:
                inspections[i] += 1
                new = limiting_function(m["op"](item))
                monkeys[m["next"](new)]["items"].append(new)
            m["items"] = []
    return inspections


# Part 1
inspections = simulate(20, lambda n: n // 3)
p1 = math.prod(sorted(inspections)[-2:])
assert p1 == 98280

# Part 2
inspections = simulate(10000, lambda n: n % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19))
p2 = math.prod(sorted(inspections)[-2:])
assert p2 == 17673687232

"""
Lessons learned:
1. Copied the input instead of parsing
2. Used dictionaries of lambdas
3. Used math.prod
4. %(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19) keeps the result equal for %11, %3
5. Need to copy the input twice (copy.deepcopy())
"""
