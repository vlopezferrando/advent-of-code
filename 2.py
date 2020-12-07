import re

# Part 1
sol = 0
for line in open('input'):
    m = re.match('(\d+)-(\d+) (\w{1}): (\w+)', line.strip())
    a = int(m.group(1))
    b = int(m.group(2))
    char = m.group(3)
    s = m.group(4)
    cops = s.count(char)
    if a <= cops and cops <= b:
        sol += 1
print(sol)

# Part 2
sol = 0
for line in open('input'):
    m = re.match('(\d+)-(\d+) (\w{1}): (\w+)', line.strip())
    a = int(m.group(1))
    b = int(m.group(2))
    char = m.group(3)
    s = m.group(4)
    cops = s.count(char)
    if bool(s[a-1] == char) != bool(s[b-1] == char):
        sol += 1
print(sol)

