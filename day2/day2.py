def test_game(l):
    for g in l:
        g = g.split(', ')
        for s in g:
            s = s.split()
            if int(s[0]) > 12 and s[1] == 'red':
                return False
            elif int(s[0]) > 13 and s[1] == 'green':
                return False
            elif int(s[0]) > 14 and s[1] == 'blue':
                return False
    return True

with open('day2.txt') as f:
    totes = 0
    for i,l in enumerate(f):
        l = l.split(': ')[1].split('; ')
        if test_game(l):
            totes += i+1
    print(totes)


