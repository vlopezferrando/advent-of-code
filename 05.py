# Part 1
ids = [
    int(l.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)
    for l in open("05.in").read().splitlines()
]
print(max(ids))

# Part 2
for i in ids:
    if i + 1 not in ids and i + 2 in ids:
        print(i + 1)
