# Read input
rows = [[l.split()[0], int(l.split()[1])] for l in open('08.in')]

# Part 1
def run():
    seen = set()
    i = acc = 0
    while i < len(rows) and i not in seen:
        seen.add(i)
        acc += rows[i][1] if rows[i][0] == 'acc' else 0
        i += rows[i][1] if rows[i][0] == 'jmp' else 1
    return acc, i

print(run()[0])

# Part 2
FLIP = {'jmp': 'nop', 'nop': 'jmp', 'acc': 'acc'}
for row in rows:
    row[0] = FLIP[row[0]]
    acc, last_i = run()
    if last_i == len(rows):
        print(acc)
    row[0] = FLIP[row[0]]
