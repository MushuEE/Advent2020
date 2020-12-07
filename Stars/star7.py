import re
from functools import partial

def validate(s, e, a):
    if not a: return False
    return s <= int(a.group('val')) <= e

def validate_h(a):
    if not a: return False
    t,val = a.group('type'), a.group('val')
    opts = {'in':[59,76], 'cm':[150,193]}
    return opts[t][0] <= int(val) <= opts[t][1]

def tru(a):
    if not a: return False
    return True

ALL = {"byr": [re.compile(r'byr:(?P<val>\d+)'), False, partial(validate,1920,2002)],
"iyr": [re.compile(r'iyr:(?P<val>\d+)\s'), False, partial(validate,2010,2020)],
"eyr": [re.compile(r'eyr:(?P<val>\d+)\s'), False, partial(validate,2020,2030)],
"hgt": [re.compile(r'hgt:(?P<val>\d+)(?P<type>cm|in)\s'), False, validate_h],
"hcl": [re.compile(r'hcl:#(?P<val>[a-z|0-9]{6})'), False, tru],
"ecl": [re.compile(r'ecl:(?P<val>amb|blu|brn|gry|grn|hzl|oth)'), False, tru],
"pid": [re.compile(r'pid:(?P<val>\d{9})'), False, tru],}

# def reset(d):


def valid():
    good = 0
    with open("test.txt") as f:
        for line in f.readlines():
            if line == "\n":
                if all([i[1] for i in ALL.values()]): good += 1
                for vals in ALL.values():
                    vals[1] = False
            for k, val in ALL.items():
                regex, truth, f = val
                m = regex.search(line)
                ALL[k][1] = truth or f(m)
            print([(i,j[1]) for i,j in ALL.items()], "\n")

        if all([i[1] for i in ALL.values()]): good += 1
    return good
print(valid())

