# Chinese Remainder Theorem code
# Copied from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# Read input
f = open('13.in')
t0 = int(next(f))
ts = [(i, int(t)) for i, t in enumerate(next(f).split(',')) if t != 'x']

# Part 1
mod, t = min([(t - t0 % t, t) for _, t in ts if t != 'x'])
print(mod*t)

# Part 2
print(chinese_remainder(*zip(*((t, t-i-1) for i, t in ts))))
