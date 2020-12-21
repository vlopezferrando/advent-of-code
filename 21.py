words = []
candidates = {}
for line in open('21.in'):
    row, b = line.replace('(', '').replace(')', '').strip().split(' contains ')
    row = row.split()
    words += row
    for a in b.split(', '):
        candidates[a] = candidates[a] & set(row) if a in candidates else set(row)

for _ in range(200):
    for c, word in candidates.items():
        if len(word) == 1:
            for c2, word2 in candidates.items():
                if c != c2 and next(iter(word)) in word2:
                    word2.remove(next(iter(word)))

bad = [candidates[k].pop() for k in sorted(candidates.keys())]

# Part 1
print(sum(w not in bad for w in words))

# Part 2
print(','.join(bad))
