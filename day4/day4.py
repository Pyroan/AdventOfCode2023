total = 0
with open('day4.txt') as f:
    for l in f:
        l = l.split(': ')[1].split(' | ')
        a,b=({*map(int,s.split())} for s in l)
        total += int(2**(len(a&b)-1))
    print(total)