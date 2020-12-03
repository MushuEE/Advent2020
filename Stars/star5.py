

def trees(right, down):
    
   trees = None
   with open("star5.txt") as f:
       trees = [list(i)[:-1] for i in f.readlines()]
   hit = 0
   row, col = 0, 0
   while row < len(trees) - 1:
       row = (row + down)
       col = (col + right) % len(trees[0])
       if trees[row][col] == '#':
       	   trees[row][col] = "X"
           hit +=1
   return hit

S = 1
for r,d in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    S *= trees(r,d)
print(S)



