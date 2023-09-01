# Python solutions to the Advent of Code

The following is a post I publish in my site [The Diligent Developer](https://www.thediligentdeveloper.com/why-solving-the-advent-of-code-is-a-great-exercise):

Title: Why solving the Advent of Code is a great exercise
Date: 2023-08-22

The [Advent of Code](https://adventofcode.com/) is a yearly challenge that consists of 25 programming problems, one each day, from December 1st to December 25th.
Hundreds of thousands of programmers participate each year, and use it as a way to improve their coding skills, learn new programming languages or just for fun.

I participated for the first time in 2020, having programmed in Python for almost a decade.
I solved all the problems on the day they were published, didn't have excessive trouble with any of them, had fun, and went on with my life.

Three or four months later, I came across the [Pytudes repository](https://github.com/norvig/pytudes) by Peter Norvig and **my mind was blown**. In case you don't know him (I didn't at the time), he is a legend in the programming world and has been the director of Google Research for many years, among other things.

The point is his solutions are brief, elegant, and use a ton of Python features that I didn't know about.

I was so baffled that I revisited all the problems, and worked on them, one by one, trying to understand his approach, and the Python features he used, and identifying the gaps in my knowledge that prevented me from solving the problems in a similar way.

> What does Peter Norvig know, that I don't, that prevents me from writing a solution like his?
>
> &mdash; <cite>me</cite>, on loop on my head

This was an inflection point for me. At the end of 2021, I participated again in the Advent of Code, but this time I focused not on solving the problems, but on *how* I solved them. I ran a small competition with a friend, trying to see who found the most elegant solution for each problem.

I'm not exactly proud of the outcome, it landed on the "hackish" side more than on the "elegant" side. E.g., for [day 8](https://adventofcode.com/2021/day/8):

```python
digits = lambda t: "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg".translate(str.maketrans(dict(zip("abcdefg", t)))).split()

fsfs = lambda x: frozenset(map(frozenset, x))
PERMS = {fsfs(digits(p)): mapt(set, digits(p)) for p in permutations("abcdefg")}
nums = lambda ds, qs: [PERMS[fsfs(ds)].index(set(q)) for q in qs]

in8: List[int] = data(8, atoms)

def day8_1(rows):
    return sum(n in [1, 4, 7, 8] for row in rows for n in nums(row[:10], row[11:]))

def day8_2(rows):
    return sum(n * 10**(3-i) for row in rows for i, n in enumerate(nums(row[:10], row[11:])))
```

Anyway, by this time, whenever I read a Python code I had written more than a year ago, I would immediately spot things that could be improved and that I would not do in the same way.
**It feels great to see how much you improved over time**.

For the 2022 edition, I went one step further and recorded myself solving some of the problems, and [uploaded the videos to YouTube](https://www.youtube.com/watch?v=war1DKS2QZE&list=PL4R7dYNzbaX0MI2HyM2IOly83f5i5EZNr). This also proved to be a great exercise, because it made me focus 100% on the problem I was solving, and also because I had to be deliberate about what I was doing.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5pD2x8rB1MI?si=yYuM4thq3Tvl-0f-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="margin-top: 40px; margin-bottom: 40px"></iframe>

In case you are curious, you can check my code at [this repository on GitHub](https://github.com/vlopezferrando/advent-of-code), which has all my solutions and can judge for yourself how good or bad they are.

## Mentoring with the Advent of Code

I've been mentoring a few developers over the last year, helping them **improve their coding and software design skills**.
I have found that the Advent of Code problems are a great subject of study, even more than the typical Leetcode problems.

Approaching the problems deliberately, trying to find the "best" solution, and not just "a" solution, is a great exercise. When you have given your best, it is the best time to come in and give you feedback on how to improve: how to simplify the algorithm, make better use of the language features, improve the readability, etc.

