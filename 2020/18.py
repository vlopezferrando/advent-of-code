def calc(s, sum_first=False):
    ns = []
    ops = []
    i = 0
    while i < len(s):
        if s[i] in "0123456789":
            ns.append(int(s[i]))
        elif s[i] in "+*":
            ops.append(s[i])
        elif s[i] == "(":
            depth = 1
            j = i + 1
            while depth > 0:
                if s[j] == "(":
                    depth += 1
                elif s[j] == ")":
                    depth -= 1
                j += 1
            ns.append(calc(s[i + 1 : j], sum_first))
            i = j
        i += 1

    if sum_first:
        while "+" in ops:
            i = ops.index("+")
            ns[i] = ns[i] + ns[i + 1]
            del ns[i + 1]
            del ops[i]

    sol = ns[0]
    for n, op in zip(ns[1:], ops):
        if op == "+":
            sol += n
        else:
            sol *= n

    return sol


# Read input
lines = open("18.in").read().splitlines()

# Part 1
print(sum(calc(l) for l in lines))

# Part 2
print(sum(calc(l, sum_first=True) for l in lines))
