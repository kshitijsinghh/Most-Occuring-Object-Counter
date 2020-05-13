from collections import Counter

ksr = open('name.txt', 'r')
zen = ksr.read()
word = zen.split()
kshitij = Counter(word)
top_three = kshitij.most_common(4)
print(top_three)
ksr.close()

