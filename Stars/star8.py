
def valid():
    set_ = {i*8 + j for i in range(128) for j in range(8)}
    with open("star8.txt") as f:
        for line in f.readlines():
            line=line.strip()
            row = int(''.join([ '1' if _ == "B" else '0' for _ in line [:7] ]),2)
            col = int(''.join([ '1' if _ == "R" else '0' for _ in line [7:] ]),2)
            set_.remove(row*8+col)
    print(set_)
    for i in set_:
        if i+1 not in set_ and i-1 not in set_:
            return i

print(valid())