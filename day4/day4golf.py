c=[i:=1]*len(n:=[*open('day4.txt')])
for l in n:
 for j in range(len({*l[l.find(':'):(p:=l.find('|'))].split()}&{*l[p:].split()})):c[i+j]+=c[i-1]
 i+=1
print(sum(c))