# Advent of Code 2021 Day 1 Part 1

def aocinput():
    with open('input') as f:
        b = f
        return b

def part1():
    total = -1
    pre = 0
    input = aocinput()
    for i in input:
        b = int(i.strip())
        if pre < b:
            total += 1
            pre = b 
        elif pre > b:
            pre = b
    print(total)

# Advent of Code 2021 Day 1 Part 2

total = -1
aoc_input = []
with open('input') as f:
    for i in f:
        aoc_input.append(int(i.strip()))
    pre = 0
    for i in enumerate(list(aoc_input)):
        b = sum(i)
        if pre < b:
            total += 1
            pre = b 
        elif pre > b:
            pre = b
    print(total)