#
# Check how I live coded this: https://youtu.be/N2Oj7guh9Oc
#

import copy

STACKS = [
    list("WBDNCFJ"),
    list("PZVQLST"),
    list("PZBGJT"),
    list("DTLJZBHC"),
    list("GVBJS"),
    list("PSQ"),
    list("BVDFLMPN"),
    list("PSMFBDLR"),
    list("VDTR"),
]

# Read instructions
instructions = []
for line in open("05.in"):
    _, n, _, from_, _, to = line.split()
    n, from_, to = int(n), int(from_) - 1, int(to) - 1
    instructions.append((n, from_, to))


# Part 1
stacks = copy.deepcopy(STACKS)
for n, from_, to in instructions:
    for i in range(n):
        stacks[to].append(stacks[from_].pop())
sol_1 = "".join(s[-1] for s in stacks)
assert sol_1 == "LBLVVTVLP"

# Part 2
stacks = copy.deepcopy(STACKS)
for n, from_, to in instructions:
    stacks[to] += stacks[from_][-n:]
    stacks[from_] = stacks[from_][:-n]
sol_2 = "".join(s[-1] for s in stacks)
assert sol_2 == "TPFFBDRJD"

"""
Lessons learned
1. Modify the input to ease reading
2. We ignored some elements with _
3. Used import copy; copy.deepcopy()
4. [1, 2, 3].pop() -> returns the last element and removes it from the list
5. Slice ranges [1, 2, 3, 4][:-3]
"""
