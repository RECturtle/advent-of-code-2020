f = open("./input.txt", "r")
lines = list(f.read().split("\n\n"))
new_lines = [x.replace("\n", " ") for x in lines]
split_lines = [x.split() for x in new_lines]

def pass_to_dict(pass_list):
    pass_dict = {}

    for entry in pass_list:
        new_entry = entry.split(":")
        key = new_entry[0]
        value = new_entry[1]
        pass_dict[key] = value

    return pass_dict

def valid_fields(passport):
    birth = "byr" in passport
    issue = "iyr" in passport
    expire = "eyr" in passport
    height = "hgt" in passport
    hair = "hcl" in passport
    eye = "ecl" in passport
    port = "pid" in passport

    return (
        birth and
        issue and
        expire and
        height and
        hair and
        eye and
        port
    )

def valid_entries(passport):
    birth = 1920 <= int(passport["byr"]) <= 2002
    issue = 2010 <= int(passport["iyr"]) <= 2020
    expire = 2020 <= int(passport["eyr"]) <= 2030
    
    height = False
    if passport["hgt"][-2:] == 'cm':
        height = 150 <= int(passport["hgt"][:-2]) <= 193
    if passport["hgt"][-2:] == 'in':
        height = 59 <= int(passport["hgt"][:-2]) <= 76
    hair = False
    if passport["hcl"][0] == "#" and len(passport["hcl"]) == 7:
        hair = check_chars(passport["hcl"][1:])
    eye = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    port = False
    if len(passport["pid"]) == 9:
        port = check_pid(passport["pid"])

    return (
        birth and
        issue and
        expire and
        height and
        hair and
        eye and
        port
    )

def check_chars(hair_color):
    valid = True
    for x in hair_color:
        if x not in 'abcdef0123456789':
            valid = False
            break
    
    return valid

def check_pid(passport_id):
    valid = True
    for x in passport_id:
        if x not in "0123456789":
            valid = False
            break
    
    return valid

passports = [pass_to_dict(x) for x in split_lines]

valid_count = [passport for passport in passports if valid_fields(passport)]
print(len(valid_count))

validate_count = [passport for passport in valid_count if valid_entries(passport)]
print(len(validate_count))
