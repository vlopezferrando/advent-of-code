#
# Check how I live coded this: https://youtu.be/m7ZMhMhYYpg
#


def index_where_first_sequence_of_distinct_characters_is_detected(s, n):
    for i in range(len(s) - n):
        if len(set(s[i : i + n])) == n:
            return i + n
    assert False


# Read input
message = open("06.in").read().strip()

# Part 1
assert index_where_first_sequence_of_distinct_characters_is_detected(message, 4) == 1816

# Part 2
assert (
    index_where_first_sequence_of_distinct_characters_is_detected(message, 14) == 2625
)

"""
Lessons learned
1. Pasting the input in the python code was fast
2. Check that all elements in a list are different: len(set(l)) == len(l)
3. assert False: making sure that some part of the code is not reached
"""
