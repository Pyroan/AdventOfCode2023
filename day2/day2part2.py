with open('day2.txt') as f:
    totes = 0
    for l in f:
        maxes = {'red':0,'green':0,'blue':0}
        game = l.split(': ')[1].split('; ')
        for pull in game:
            pull = pull.split(', ')
            for s in pull:
                s = s.split()
                v,k = int(s[0]), s[1]
                if v > maxes[k]: maxes[k] = v
        totes += maxes['red']*maxes['green']*maxes['blue']
    print(totes)


