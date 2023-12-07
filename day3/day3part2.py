import re
numbers = []
gears = []
grid = []
total = 0

def is_symbol(c):
    return c not in '0123456789.'

def bordered_numbers(gear):
    y,x = gear
    hits = []
    for n in numbers:
        ny, nx = n[1]
        for j in range(max(y-1,0),min(y+2,len(grid))):
            for i in range(max(x-1,0), min(x+2, len(grid[0]))):
                # efficiency is for cowards
                if j == ny and i in range(nx,nx+len(n[0])):
                    hits += [int(n[0])]
                    break

    return hits

with open('day3.txt') as f:
    # store the value & location of each number (this might be fun actually)
    for i,l in enumerate(f):
        l = l.strip()
        for m in re.finditer(r'(\d+)',l):
            numbers.append([m[0],(i, m.start())]) 
        for m in re.finditer(r'\*',l):
            gears.append((i,m.start()))
        grid.append(l)

for g in gears:
    b = bordered_numbers(g)
    if len(b) == 2:
        total += b[0]*b[1]
print('Total:',total)