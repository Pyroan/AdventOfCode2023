with open('day4.txt') as f:
    lines = f.readlines()
copies = [1]*len(lines)
for i,l in enumerate(lines):
    l = l.split(': ')[1].split(' | ')
    a,b=({*map(int,s.split())} for s in l)
    for j in range(i+1, i+1+len(a&b)):
        copies[j]+=copies[i]
print(sum(copies))