
def valid():
    valid_e = {'hcl':False,
               'ecl':False,
               'hgt':False,
               'byr':False,
               'pid':False,
               'eyr':False,
               'iyr':False}
    c = valid_e.copy()
    good = 0
    with open("star6.txt") as f:
        for line in f.readlines():
            if line == "\n":
                if all(c.values()): good += 1
                c = valid_e.copy()
            for option in c.keys():
                if f'{option}:' in line:
                    c[option] = True
        if all(c.values()): good += 1
    return good
print(valid())