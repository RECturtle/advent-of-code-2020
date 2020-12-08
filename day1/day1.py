from itertools import combinations


f = open("./input.txt", "r")
lines = f.read().splitlines()
line_ints = [int(x) for x in lines]
two_combos = list(combinations(line_ints, 2))
three_combos = list(combinations(line_ints, 3))


def sum_of_2(combos):
    for x in combos:
        if sum(x) == 2020:
            print(x[0] * x[1])


def sum_of_3(combos):
    for x in combos:
        if sum(x) == 2020:
            print(x[0]*x[1]*x[2])


sum_of_2(two_combos)
sum_of_3(three_combos)
