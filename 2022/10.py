# Read input and run simulation
XS = []
cycle, X = 1, 1
for line in open("10.in"):
    XS.append(X)
    cycle += 1

    if line.startswith("addx"):
        XS.append(X)
        cycle += 1
        X += int(line.split()[1])


# Part 1
p1 = sum(i * XS[i - 1] for i in [20, 60, 100, 140, 180, 220])
assert p1 == 17180

# Part 2
for i in range(6):
    for j in range(40):
        print("#" if abs(j - XS[i * 40 + j]) < 2 else ".", end="")
    print()
# Solution: REHPRLUB


"""
Lessons learned
1. How to create a list of lists: [["."] * WIDTH for _ in range(HEIGHT)]
2. Off-by-one errors are some of the hardest issues in computer science
3. Used % WIDTH, cycle // WIDTH, to calculate the row/column
4. You can sometimes refactor code to make it very brief
5. "X" if ..... else "Y"
6. We need to find the sweet spot between brief+hacky <--> long+verbose
"""
