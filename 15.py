last = [-1]*30000000

# Input
l = [1, 0, 15, 2, 10, 13]
for i, n in enumerate(l):
    last[n] = i

i, n = len(l) - 1, l[-1]
while i < 30000000:
    last[n], n = i, 0 if last[n] == -1 else i-last[n]
    i += 1

    # Part 1, 2
    if i == 2019:
        print(n)
    elif i == 29999999:
        print(n)
