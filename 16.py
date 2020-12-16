fields = []
fields_names = []

# Read input
lines = open('16.in').read().splitlines()
for i, line in enumerate(lines):
    if ' or ' in line:
        a, b, c, d = line.split(' ')[-3].split('-') + line.split(' ')[-1].split('-')
        fields.append((int(a), int(b), int(c), int(d)))
        fields_names.append(line.split(':')[0])
    elif 'your ticket' in line:
        my = [int(n) for n in lines[i+1].split(',')]
    elif 'nearby tickets' in line:
        all_tickets = [[int(n) for n in l.split(',')] for l in lines[i+1:]]

# Part 1
sol = 0
tickets = all_tickets.copy()
for  t in all_tickets:
    for n in t:
        if all(n < a or (b < n and n < c) or d < n for a, b, c, d in fields):
            sol += n
            tickets.remove(t)
print(sol)

# Part 2
candidates = {
    i: [name for (a, b, c, d), name in zip(fields, fields_names)
        if all((a <= t[i] and t[i] <= b) or (c <= t[i] and t[i] <= d) for t in tickets)]
    for i in range(len(my))
}

fields_removed = []
for _ in range(len(my)):
    for i, cs in candidates.items():
        if len(cs) == 1 and cs[0] not in fields_removed:
            fields_removed.append(cs[0])
            for j, cs2 in candidates.items():
                if j != i and cs[0] in cs2:
                    cs2.remove(cs[0])

sol = 1
for i, cs in candidates.items():
    if 'departure' in cs[0]:
        sol *= my[i]
print(sol)
