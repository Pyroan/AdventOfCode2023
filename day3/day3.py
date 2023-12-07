import colorama
colorama.just_fix_windows_console()
import re
p = re.compile(r'(\d+)')
numbers = []
grid = []
total = 0

def is_symbol(c):
    return c not in '0123456789.'

def borders_symbol(n):
    y,x = n[1]
    for j in range(max(y-1,0),min(y+2,len(grid))):
        for i in range(max(x-1,0), min(x+len(n[0])+1, len(grid[0]))):
            if is_symbol(grid[j][i]): return True
    return False

with open('day3.txt') as f:
    # store the value & location of each number (this might be fun actually)
    for i,l in enumerate(f):
        l = l.strip()
        for m in p.finditer(l):
            numbers.append([m[0],(i, m.start())]) 
        grid.append(l)
for n in numbers:
    if borders_symbol(n):
        total += int(n[0])
print('Total:',total)

# fancy visualization because i'm losing my mind
# newgrid=grid[:]
# for l in newgrid:
#     re.split(r'()',l)