counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')

for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

jjj = {'chunk':1, 'fred':42, 'jan':100}
print(list(jjj))
print(jjj.key())
print(jjj.value())
print(jjj.items())
for k,v in jjj.items() :
    print(k,v)


name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
