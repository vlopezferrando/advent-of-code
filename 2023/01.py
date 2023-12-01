lines = open("01.in").read().splitlines()

DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def digits(s, spelled_out_digits):
    for i, c in enumerate(s):
        if c.isdigit():
            yield int(c)
        for j, d in enumerate(DIGITS):
            if spelled_out_digits and s[i:].startswith(d):
                yield j + 1


def line_number(s, spelled_out_digits):
    ds = list(digits(s, spelled_out_digits))
    return 10 * ds[0] + ds[-1]


# Part 1
sol_1 = sum(line_number(line, False) for line in lines)
assert sol_1 == 57346

# Part 2
sol_2 = sum(line_number(line, True) for line in lines)
assert sol_2 == 57345
