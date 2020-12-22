p1, p2 = open('22.in').read().split('\n\n')
p1 = [int(x) for x in p1.splitlines()[1:]]
p2 = [int(x) for x in p2.splitlines()[1:]]


def game(p1, p2, recursive=False):
    seen = set()
    while len(p1) > 0 and len(p2) > 0:
        signature = str(p1) + str(p2)
        if signature in seen:
            return 1, p1 + p2
        seen.add(signature)

        if recursive and len(p1) > p1[0] and len(p2) > p2[0]:
            winner, _ = game(p1[1 : p1[0] + 1], p2[1 : p2[0] + 1])
        elif p1[0] > p2[0]:
            winner = 1
        else:
            winner = 2

        if winner == 1:
            p1 = p1[1:] + [p1[0], p2[0]]
            p2 = p2[1:]
        else:
            p2 = p2[1:] + [p2[0], p1[0]]
            p1 = p1[1:]

    return winner, p1 + p2


_, sol = game(p1.copy(), p2.copy())
print(sum((i + 1) * x for i, x in enumerate(reversed(sol))))


_, sol = game(p1, p2, True)
print(sum((i + 1) * x for i, x in enumerate(reversed(sol))))
