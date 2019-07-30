# open and print
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

# open and counting lines
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# reading the whole file
fhand = open('mbox-short.txt')
inp = fhan.read()
print(len(inp))
print(inp[:20])

# Searching through a file
# In this situation, blank line will occur. Use rstrip() to delete '\n'
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)

# Searching through a file
# In this situation, blank line will occur. Use rstrip() to delete '\n'
fhand = open('mbox-short.txt')
for line in fhand:
# delete right blank at each line(such as \n )
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)


# Searching through a file
# Same like upper one, but better
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# using in to select lines
# find all lines including '@uct.ac.za'
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line
        continue
    print(line)

# input filename
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

#Bad file names
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:' fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
