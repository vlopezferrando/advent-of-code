#
# Check how I live coded this: https://youtu.be/jn50frM7a0o
#

from math import inf


class Node:
    def __init__(self, commands=None):
        self.dirs = {}
        self.files = {}

        if commands:
            self.build_tree(commands)
            self.compute_sizes()

    def build_tree(self, commands):
        while len(commands) > 0:
            cmd, *commands = commands
            if cmd.startswith("cd"):
                _, child_dir = cmd.split()
                if child_dir == "..":
                    return commands
                commands = self.dirs[child_dir].build_tree(commands)
            elif cmd.startswith("ls"):
                for row in cmd.splitlines()[1:]:
                    size_dir, name = row.split()
                    if size_dir == "dir":
                        self.dirs[name] = Node()
                    else:
                        self.files[name] = int(size_dir)
        return commands

    def compute_sizes(self):
        self.size = sum(self.files.values()) + sum(
            child.compute_sizes() for child in self.dirs.values()
        )
        return self.size

    def sum_dir_sizes_below_threshold(self, threshold):
        return (self.size if self.size < threshold else 0) + sum(
            child.sum_dir_sizes_below_threshold(threshold)
            for child in self.dirs.values()
        )

    def min_dir_size_over_threshold(self, threshold):
        return min(
            [self.size if self.size >= threshold else inf]
            + [
                child.min_dir_size_over_threshold(threshold)
                for child in self.dirs.values()
            ]
        )


# Read input
commands = open("07.in").read().split("$ ")

# Build the tree with the commands
root = Node(commands)

# Part 1
sol_1 = root.sum_dir_sizes_below_threshold(1e5)
assert sol_1 == 1845346

# Part 2
space_needed = 3e7 - (7e7 - root.size)
assert root.min_dir_size_over_threshold(space_needed) == 3636703


"""
Lessons learned
1. Edited the input to remove the first line, and "$ " in the second line
2. Splitted the input with "$ "
3. Used a class, with __init__(self).
4. Recursivity for tree traversal
5. from math import inf
6. sum, min, map... with list comeprehensions
7. .values() method of dicts
8. cmd, *commands = commands; takes the first element in the list, and keeps a list with the rest
"""
