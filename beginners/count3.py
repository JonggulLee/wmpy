
fhand = open('./data/romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
            counts[word] = counts.get(word, 0) + 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)
