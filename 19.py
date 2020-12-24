# Read input
lines = open("19.in").read().splitlines()
rules = [[] for _ in range(200)]
ss = []
for i, l in enumerate(lines):
    if l == "":
        pass
    elif l[0] in "ab":
        ss.append(l)
    else:
        n, rule = int(l.split(":")[0]), l.split(":")[1].split()
        rules[n].append([])
        for c in rule:
            if c == '"a"':
                ruleA = n
            elif c == '"b"':
                ruleB = n
            elif c == "|":
                rules[n].append([])
            else:
                rules[n][-1].append(int(c))


def valid(a, b, r):
    if a == b:
        return False
    if (a, b, r) in mem:
        return mem[(a, b, r)]
    if r == ruleA:
        return b == a + 1 and s[a] == "a"
    if r == ruleB:
        return b == a + 1 and s[a] == "b"
    ret = False
    for rule in rules[r]:
        if len(rule) == 1:
            ret |= valid(a, b, rule[0])
        elif len(rule) == 2:
            r1, r2 = rule
            for i in range(a + 1, b):
                ret |= valid(a, i, r1) and valid(i, b, r2)
        elif len(rule) == 3:
            r1, r2, r3 = rule
            for i in range(a + 1, b - 1):
                for j in range(i + 1, b):
                    ret |= valid(a, i, r1) and valid(i, j, r2) and valid(j, b, r3)

    mem[(a, b, r)] = ret
    return ret


# Part 1
sol = 0
for s in ss:
    mem = {}
    if valid(0, len(s), 0):
        sol += 1
print(sol)

# Part 2
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

sol = 0
for s in ss:
    mem = {}
    if valid(0, len(s), 0):
        sol += 1
print(sol)
