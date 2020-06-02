from collections import Counter

ksr = open('text.txt', 'r')
zen = ksr.read()
word = zen.split()
worddictionary={}
for kv in word:
    if kv in worddictionary:
        worddictionary[kv] += 1
    else:
        worddictionary[kv]=1
for p,r in worddictionary.items():
    print(p , str(r))

kshitij = Counter(word)
top_three = kshitij.most_common(4)
print(top_three)
ksr.close()

