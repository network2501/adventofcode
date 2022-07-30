# Advent of Code 2021 Day 2 Part 1
from dataclasses import dataclass


def aocinput():
    with open("input") as f:
        aoc_input = []
        for i in f:
            aoc_input.append(i.strip().split())
    return aoc_input


aoc_input = aocinput()


@dataclass
class Position:
    horizontal_position: int = 0
    depth: int = 0
    aim: int = 0


p1p = Position()


def part1():
    for move in aoc_input:
        tick = int(move[1])
        match move:
            case ["forward", str]:
                p1p.horizontal_position += tick
            case ["down", str]:
                p1p.depth += tick
            case ["up", str]:
                p1p.depth -= tick


part1()
print(f"Day 2 Part 1 Answer: \n{int(p1p.horizontal_position) * int(p1p.depth)}\n")
print(f"aim \t{p1p.aim}\ndepth \t{p1p.depth}\nHP \t{p1p.horizontal_position}")

# Advent of Code 2021 Day 1 Part 2


p2p = Position()


def part2():
    for move in aoc_input:
        tick = int(move[1])
        match move:
            case ["forward", str]:
                p2p.horizontal_position += tick
                p2p.depth += tick * p2p.aim
            case ["down", str]:
                p2p.aim += tick
            case ["up", str]:
                p2p.aim -= tick


part2()


print(f"\nDay 2 Part 1 Answer: \n{int(p2p.horizontal_position) * int(p2p.depth)}\n")
print(f"aim \t{p2p.aim}\ndepth \t{p2p.depth}\nHP \t{p2p.horizontal_position}")
