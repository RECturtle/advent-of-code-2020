f = open("./input.txt", "r")
lines = list(f.read().split("\n\n"))
group_answers = [line.splitlines() for line in lines]


def answer_count(answers):
    count = 0
    for ans in answers:
        temp_str = ""
        for person in ans:
            temp_str += person
        count += len(set(temp_str))
    print(count)


def all_answered(group_answer):
    count = 0
    for ans in group_answers:
        if len(ans) == 1:
            count += len(set(ans[0]))
        else:
            temp_set = set(ans[0]).intersection(*ans[1:])
            count += len(temp_set)
    print(count)


answer_count(group_answers)
all_answered(group_answers)

