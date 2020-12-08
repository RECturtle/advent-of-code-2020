f = open("./input.txt", "r")
lines = list(f.read().splitlines())
new_lines = [x.replace(':', '').replace('-', ' ').split() for x in lines]


def check_if_valid(password):
    count_one = 0
    count_two = 0
    for x in password:
        small = int(x[0])
        big = int(x[1])
        letter = x[2]
        word = x[3]
        appear = word.count(letter)
        # Challenge one
        if appear <= big and appear >= small:
            count_one += 1
        
        # Challenge two
        if word[small - 1] == letter and word[big - 1] != letter:
            count_two += 1
        if word[big -1] == letter and word[small -1] != letter:
            count_two += 1

    print(count_one)
    print(count_two)


check_if_valid(new_lines)

