# Advent of Code 2021 Day 2 Part 1
from dataclasses import dataclass

@dataclass
class Position:
    forward: int = 0
    depth: int = 0

with open('input') as f:
    for i in f:
        direction = i.strip().split()
        match direction:
            case ['forward', str]:
                Position.forward += int(direction[1])
            case ['down', str]:
                Position.depth += int(direction[1])
            case ['up', str]:
                Position.depth -= int(direction[1])

int(Position.forward) * int(Position.depth)

# Advent of Code 2021 Day 1 Part 2

