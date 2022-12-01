# Advent of Code 2022 Day 1 Part 1
def aocinput():
    with open("input") as f:
        aoc_input = []
        for i in f:
            aoc_input.append(i.strip())
        return aoc_input


aoc_input = aocinput()

def somedict():
    elves = {}
    elf = 1
    for calories in aoc_input:
        if len(calories) == 0:
            elf += 1
        elif elf not in elves:
            elves[elf] = [int(calories)]
        else:
            elves[elf].append(int(calories))
    return elves


def elf_cal_total():
    a = somedict()
    newd = {}
    for k,v in a.items():
        newd[sum(v)] = k
    return newd

# elf with most
print(sorted(elf_cal_total().items())[-1][1])
# top 3 elves with most
print(sum(sorted(elf_cal_total())[-3:]))
