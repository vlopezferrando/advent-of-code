from itertools import combinations

# Read input
v = [int(l) for l in open('09.in')]

# Part 1
for i, x in enumerate(v[25:]):
    if all(sum(c) != x for c in combinations(v[i:i+25], 2)):
        invalid = x
        break
print(invalid)

# Part 2
for i in range(len(v)-2):
    for j in range(i+2, len(v)):
        if sum(v[i:j]) == invalid:
            print(min(v[i:j]) + max(v[i:j]))
