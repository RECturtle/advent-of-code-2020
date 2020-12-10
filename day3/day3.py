f = open("./input.txt", "r")
lines = list(f.read().splitlines())


def check_trees(path, right, down):
    tree_count = 0
    x = 0
    y = 0
    
    while y < len(path):
        new_x = x % 31
        if path[y][new_x] == '#':
            tree_count += 1
        x += right
        y += down
    
    return tree_count

# Part 1
print(check_trees(lines, 3, 1))

# Part 2
print(
    check_trees(lines, 1, 1) *
    check_trees(lines, 3, 1) *
    check_trees(lines, 5, 1) *
    check_trees(lines, 7, 1) *
    check_trees(lines, 1, 2)
)

