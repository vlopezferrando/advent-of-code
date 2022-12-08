#
# Check how I live coded this: https://youtu.be/Wek4cmjLNsE
#

# Read input
rounds = [line.split() for line in open("2.in")]

# Rock, Paper, Scissors game spec
R, P, S = "A", "B", "C"
WINS = {R: P, P: S, S: R}
LOOSES = {b: a for a, b in WINS.items()}


def score(a, b):
    sc = 0
    if a == b:
        sc = 3
    elif WINS[a] == b:
        sc = 6

    POINTS = {R: 1, P: 2, S: 3}
    return sc + POINTS[b]


# Part 1
DECRYPT = {"X": R, "Y": P, "Z": S}
sol_1 = sum(score(a, DECRYPT[b]) for a, b in rounds)
assert sol_1 == 10718


# Part 2
DECRYPT = {
    "X": lambda a: LOOSES[a],
    "Y": lambda a: a,
    "Z": lambda a: WINS[a],
}
sol_2 = sum(score(a, DECRYPT[b](a)) for a, b in rounds)
assert sol_2 == 14652


"""
Lessons learned
1. lambda a: a
2. Dict of lambdas: DECRYPT[b](a)
3. List comprehensions: sum(x for x, _ in l)
"""
