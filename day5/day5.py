f = open("./input.txt", "r").read().splitlines()
rows = [x for x in range(128)]
seats = [x for x in range(8)]

def get_id(directions, columns):
    row = row_col(directions, rows)
    col = row_col(columns, seats)
    
    return ((row * 8) + col)
    

def row_col(dirs, list_in):
    low = 0
    high = len(list_in) - 1

    for x in dirs:
        if x == "F" or x == "L":
            high = ((high + low + 1) // 2) - 1
        else:
            low = (high + low + 1) // 2
    
    return low


ids = [get_id(x[:7], x[7:]) for x in f]
print(max(ids))

my_seat = [seat for seat in range(min(ids), max(ids)) if seat not in ids][0]
print(my_seat)
