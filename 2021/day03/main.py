# Advent of Code 2021 Day 3 Part 1
# Answer 2640986


#  0                   1                   2                   3
#  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
# +-+-+-+-+-+
# |0 0 1 0 0|
# |1 1 1 1 0|
# |1 0 1 1 0|
# |1 0 1 1 1|
# |1 0 1 0 1|
# |0 1 1 1 1|
# |0 0 1 1 1|
# |1 1 1 0 0|
# |1 0 0 0 0|
# |1 1 0 0 1|
# |0 0 0 1 0|
# |0 1 0 1 0|
# +-+-+-+-+-+
#
# Gamma rate is the most common number by column, convert from binary to decimal.
#
# Epsilon rate is the least common number by column (inverse gamma) convert
# from binary to decimal.
#
# This is just begging for some ANDing
# Or ZIP
#
# As it turned out zip() didn't really suit for the way I tackled this because
# it was nested.


from dataclasses import dataclass


def aocinput():
    with open("input") as f:
        aoc_input = []
        for i in f:
            aoc_input.append(i.strip())
    return aoc_input


aoc_input = aocinput()


@dataclass
class Position:
    gamma: int = 0
    epsilon: int = 0
    aim: int = 0


# should get better with list comprehensions

transformed = {}


def dict_maker():
    # Assumes data is clean & creates a dict the size of the first value
    # So if the string has 4 characters, this will make a dict with 4 keys
    positions = range(len(aoc_input[0]))
    d = dict(zip(positions, [None] * len(positions)))
    # For the first value it'll need to replace the None value
    # After that values should be appeneded.
    return d


def row_builder():
    d = dict_maker()
    for binary in aoc_input:
        for k, v in enumerate(binary):
            if d[k] is not None:
                # Append a value to the string
                d[k] += v
            else:
                # replace the initialised None with a value
                d[k] = v
    # Don't want to deal with a dict type so return a list
    # make me a list comp
    l = []
    for k, v in d.items():
        l.append(v)
    return l


def frequency():
    l = row_builder()
    counts = []
    # this is binary so
    for i in l:
        one = 0
        zero = 0
        for v in i:
            if int(v) > 0:
                one += 1
            else:
                zero += 1
        counts.append([one, zero])
    return counts


def power_consumption():
    significance = frequency()
    epsilon = ""
    gamma = ""
    for zero, one in significance:
        if one < zero:
            epsilon += "1"
            gamma += "0"
        else:
            epsilon += "0"
            gamma += "1"
    return int(gamma, 2) * int(epsilon, 2)


print(power_consumption())

#
# Advent of Code 2021 Day 3 Part 1
#
