fname = './data/mbox-short.txt'
fhand = open('./data/' + fname)
c = dict()
for line in fhand:
    if not line.startswith('From '): continue
    pieces = line.split()
    email = pieces[1]
    c[email] = c.get(email, 0) + 1

print(c)
