# Read input
games = [line.split(":")[1].split("|") for line in open("04.in")]
wins = [len(set(winning.split()) & set(have.split())) for winning, have in games]

# Part 1
sol_1 = sum(2 ** (n - 1) for n in wins if n)
assert sol_1 == 23941

# Part 2
n_cards = [1] * len(wins)
for i, n in enumerate(wins):
    for j in range(n):
        n_cards[i + j + 1] += n_cards[i]
sol_2 = sum(n_cards)
assert sol_2 == 5571760