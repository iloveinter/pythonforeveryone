#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fname = input('Enter file name: ')
try:
    f = open(fname)
except:
    print('unable to open file!')
    quit()
counts = dict()
for line in f:
    line = line.rstrip()
    if line.startswith('From'):
        words = line.split()
        if len(words) > 2:
            word = words[1]
            counts[word] = counts.get(word,0)+1

# output bigword and bigcount
bigword = 0
bigcount = 0
for k,v in counts.items():
    if v is None or v > bigcount:
        bigword = k
        bigcount = v

print(bigword,bigcount)

    #    print(counts)
