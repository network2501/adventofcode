# Advent of Code 2021 Day 1 Part 1

from dataclasses import dataclass
import itertools


def aocinput():
    with open("input") as f:
        aoc_input = []
        for i in f:
            aoc_input.append(int(i.strip()))
        return aoc_input


aoc_input = aocinput()


def part1():
    total = -1
    pre = 0
    for i in aoc_input:
        b = int(i.strip())
        if pre < b:
            total += 1
            pre = b
        elif pre > b:
            pre = b
    print(f"Part 1 {total}")


# Advent of Code 2021 Day 1 Part 2


# I just want to grab 3 things from the list at a time
# then I can assign one to a buffer, and compare the incoming
# to the buffer.


@dataclass(frozen=True)
class Window:
    size: int = 3


def d1p2() -> int:
    answer = 0
    ws = Window.size
    for i, v in enumerate(aoc_input):
        buffer = sum(aoc_input[i : i + ws])
        i += 1
        buffer2 = sum(aoc_input[i : i + ws])
        if buffer < buffer2:
            answer += 1
    print(answer)


d1p2()
