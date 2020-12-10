l = [int(x.strip()) for x in open('01.in')]

# Part 1
for i in range(len(l)):
    for j in range(i, len(l)):
        if l[i] + l[j] == 2020:
           print(l[i] * l[j])

# Part 2
for i in range(len(l)):
    for j in range(i, len(l)):
        for k in range(j, len(l)):
            if l[i] + l[j] + l[k] == 2020:
               print(l[i] * l[j] * l[k])

