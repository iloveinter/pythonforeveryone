#8.5 Open the file mbox-short.txt and read it line by line.
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('Please input a valid file name!')
    quit()

 count = 0
for line in fh:
    if line.startswith('From:'):
        line = line.rstrip()
        words = line.split()
        print(words[1])
        count = count + 1

print('There were', count, 'lines in the file with From as the first word')


# another example
for l in fh:
    l = l.rstrip()
    wds = l.split()
    print(wds)

    if len(wds) < 3 or wds[0] != 'From:':
        continue
    print(wds[2])
