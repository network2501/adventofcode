# --- Day 2: Rock Paper Scissors ---
# The Elves begin to set up camp on the beach. To decide whose tent
# gets to be closest to the snack storage, a giant Rock Paper Scissors
# tournament is already in progress.
# Rock Paper Scissors is a game between two players. Each game contains
# many rounds; in each round, the players each simultaneously choose
# one of Rock, Paper, or Scissors using a hand shape. Then, a winner
# for that round is selected:
# Rock defeats Scissors,
# Scissors defeats Paper, and
# Paper defeats Rock.
#
# If both players choose the same shape, the round instead ends in a draw.
# Appreciative of your help yesterday, one Elf gives you an encrypted
# strategy guide (your puzzle input) that they say will be sure to help you win.
# "The first column is what your opponent is going to play:
#
# A for Rock,
# B for Paper, and
# C for Scissors.
#
# The second column--" Suddenly, the Elf is called away to help with someone's tent.
#
# X         X maybe rock?   (1 point, loss 0)
# Y         Y maybe paper?  (2 points, win 6)
# Z         Z maybe scissor?(3 points, draw 3)
#
#
# asdf


def aocinput():
    with open("input") as f:
        aoc_input = []
        for i in f:
            aoc_input.append(i.strip())
        return aoc_input


unstructured_games = aocinput()

# so i could parse this data and normalise it so ABC and XYZ represent what we believe them to be
# A Rock, B Paper, C Scissor and then X Rock, Y Paper, Z Scissor.
#
# That would make comparing elements easier because the comparison for a draw would be one function.
# A win would need still some specific functions written but.. the possabilities could also be done
# as a nest dictionary where the first value is looked up as a key and then inside is another
# dict and the hand played is the nested key used to look up a win or lose
#
# {rock:{rock:draw, paper:lose, scissor:win},
# paper:{rock:win, paper:draw, scissor:lose},
# scissor:{rock:lose, paper:win, scissor:draw}}
#
#  which could be drawn like this
#
#
#           Opposition
#
#        │   R   P   S
#      ──┼────────────
#        │
#  P   R │   D   L   W
#  L     │
#  A     │
#  Y   P │   W   D   L
#  E     │
#  R     │
#      S │   L   W   D
#        │


# if the points change it'll be nice to have this as a variable

win = 6
lose = 0
draw = 3

# actually i don't have to parse the original input and rename things if i'm
# already creating keys, the original values can just be keys with the
# hand's score being another dict. Possible hands look like.


# I realise why i don't like nested dicts, even within this small space i'm not really excited
# about writing nested dictionary code


def day2p1():

    pos = {
        # X is Rock
        "X": {"A": draw, "B": lose, "C": win, "pts": 1},
        # Y is Paper
        "Y": {"A": win, "B": draw, "C": lose, "pts": 2},
        # Z is Scissor
        "Z": {"A": lose, "B": win, "C": draw, "pts": 3},
    }

    score = 0
    for g in unstructured_games:
        you = g[2]
        them = g[0]
        score += pos[you][them] + pos[you]["pts"]
    return score


print(f"Part 1 - {day2p1()}")

# --- Part Two ---

# The Elf finishes helping with the tent and sneaks back over to you.
# "Anyway, the second column says how the round needs to end: X means you need to lose,
# Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

# The total score is still calculated in the same way, but now you need to figure out
# what shape to choose so the round ends as indicated. The example above now goes like this:

# A Y
# B X
# C Z

#     In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y),
#     so you also choose Rock. This gives you a score of 1 + 3 = 4.
#     In the second round, your opponent will choose Paper (B), and you choose Rock so you lose
#     (X) with a score of 1 + 0 = 1.
#     In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.
# Following the Elf's instructions for the second column,
# what would your total score be if everything goes exactly according to your strategy guide?

# ok maybe normalising the output would have been better

#           Opposition
#
#        │   R   P   S
#      ──┼────────────
#        │
#  P   R │   D   L   W
#  L     │
#  A     │
#  Y   P │   W   D   L
#  E     │
#  R     │
#      S │   L   W   D
#        │


r = 1
p = 2
s = 3


def day2p2():

    pos = {
        # lose
        "X": {"A": s, "B": r, "C": p, "pts": 0},
        # draw
        "Y": {"A": r, "B": p, "C": s, "pts": 3},
        # win
        "Z": {"A": p, "B": s, "C": r, "pts": 6},
    }

    score = 0
    for g in unstructured_games:
        res = g[2]
        them = g[0]
        score += pos[res][them] + pos[res]["pts"]
    return score


# C X
# C X
# C X
# A Z


print(f"Part 2 - {day2p2()}")
