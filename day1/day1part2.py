with open('day1.txt') as f:
    n = []
    digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for l in f:
        # this is hilariously hacky: subverting having to worry about searching in order by just copying the extra characters on either side of the digit we find <3
        for i,d in enumerate(digits):
            l = l.replace(d,d+str(i)+d)
        i = list(filter(lambda x: x in '0123456789', l))
        n.append(int(i[0]+i[-1]))
    print(sum(n))