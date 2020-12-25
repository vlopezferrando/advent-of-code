i, n, a, b, M = 0, 1, 3469259, 13170438, 20201227
while n != a:
    n = (n * 7) % M
    i += 1
# Python 3.8:
# while (n := (n * 7) % M) != a: i += 1
print(pow(b, i, M))
