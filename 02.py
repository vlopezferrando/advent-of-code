import re

sol1 = sol2 = 0
for line in open('02.in'):
    m = re.match('(\d+)-(\d+) (\w{1}): (\w+)', line.strip())
    a = int(m.group(1))
    b = int(m.group(2))
    char = m.group(3)
    s = m.group(4)
    cops = s.count(char)
    # Part 1
    if a <= cops and cops <= b:
        sol1 += 1
    # Part 2
    if bool(s[a-1] == char) != bool(s[b-1] == char):
        sol2 += 1
print(sol1)
print(sol2)
