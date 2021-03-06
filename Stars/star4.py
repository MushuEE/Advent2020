import re

def get_ok():
    ok = 0
    with open("star3.txt") as f:
        for line in f.readlines():
            print(line)
            r = re.compile(r'(?P<low>\d+)-(?P<high>\d+) (?P<letter>[a-z]): (?P<pass>[a-z]+)')
            m = r.search(line)
            low = m.group('low')
            high = m.group('high')
            letter = m.group('letter')
            password = m.group('pass')

            if bool(password[int(low)-1] == letter) != bool(password[int(high)-1] == letter):
                ok += 1

    return ok
print(get_ok())