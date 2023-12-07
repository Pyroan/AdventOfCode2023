with open('day1.txt') as f:
    n = []
    for l in f:
        i = list(filter(lambda x: x in '0123456789', l))
        n.append(int(i[0]+i[-1]))
    print(sum(n))