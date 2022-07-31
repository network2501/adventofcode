# Advent of Code 2021 Day 3 Part 1
# Answer 2640986

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
    oxygen_generator_rating: int = 0
    CO2_scrubber_rating: int = 0


def dict_maker():
    positions = range(len(aoc_input[0]))
    d = dict(zip(positions, [None] * len(positions)))
    return d


def row_builder():
    d = dict_maker()
    for binary in aoc_input:
        for k, v in enumerate(binary):
            if d[k] is not None:
                d[k] += v
            else:
                d[k] = v
    l = []
    for k, v in d.items():
        l.append(v)
    return l


def frequency():
    l = row_builder()
    counts = []
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
