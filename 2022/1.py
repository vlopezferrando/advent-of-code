# Read the input, sum the groups and sort
sums = sorted(
    [sum(map(int, g.splitlines())) for g in open("1.in").read().split("\n\n")]
)

# Part 1
sol_1 = sums[-1]
assert sol_1 == 70369

# Part 2
sol_2 = sum(sums[-3:])
assert sol_2 == 203002

"""
Lessons learned:
1. split \n\n
2. splitlines()
3. map(int, [])
4. max(), sum(), sorted()
5. assert
6. sums[-1], sums[-3:]
"""
