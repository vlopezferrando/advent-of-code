import re

max_rgb = lambda line: [
    max([int(x) for x in re.findall(rf"(\d+) {c}", line)])
    for c in ["red", "green", "blue"]
]

games = [(i + 1, max_rgb(line)) for i, line in enumerate(open("02.in"))]

# Part 1
sol_1 = sum(game_id for game_id, (r, g, b) in games if r < 13 and g < 14 and b < 15)
assert sol_1 == 2632

# Part 2
sol_2 = sum(r * g * b for _, (r, g, b) in games)
assert sol_2 == 69629